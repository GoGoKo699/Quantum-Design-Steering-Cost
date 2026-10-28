#!/usr/bin/env python3
"""Finite certificates for the exact design-steering cost and its boundaries.

Rational checks and explicit matrix contractions complement the written proofs.
They do not certify an arbitrary-dimensional theorem or literature priority.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import comb
from pathlib import Path
import platform

import numpy as np

from multinomial_checks import counts, exact_check, multinomial, povm_check

TOLERANCE = 1e-12


def qfi(rho: np.ndarray, charge: np.ndarray) -> float:
    """SLD QFI computed from the spectral formula, including zero eigenvalues."""
    eigenvalues, eigenvectors = np.linalg.eigh(rho)
    if eigenvalues.min() < -TOLERANCE:
        raise AssertionError("Input is not positive semidefinite")
    eigenvalues = np.maximum(eigenvalues, 0.0)
    generator = eigenvectors.conj().T @ charge @ eigenvectors
    result = 0.0
    for a, ra in enumerate(eigenvalues):
        for b, rb in enumerate(eigenvalues):
            if ra + rb > TOLERANCE:
                result += 2 * (ra - rb) ** 2 / (ra + rb) * abs(generator[a, b]) ** 2
    return float(result)


def mixed_reference_check(coherence: F) -> dict:
    """Contract an invariant four-effect measurement with a mixed qubit reference."""
    c = float(coherence)
    charge_a = np.diag([0.0, 1.0])
    charge_b = -charge_a
    charge_r = -charge_a
    rho_r = np.array([[0.5, c], [c, 0.5]], dtype=complex)
    total_charge = np.kron(charge_b, np.eye(2)) + np.kron(np.eye(2), charge_r)
    basis = np.eye(4, dtype=complex)
    vectors = [
        basis[:, 0], basis[:, 3],
        (basis[:, 1] + basis[:, 2]) / np.sqrt(2),
        (basis[:, 1] - basis[:, 2]) / np.sqrt(2),
    ]
    effects = [np.outer(v, v.conj()) for v in vectors]
    assert np.max(abs(sum(effects) - np.eye(4))) < TOLERANCE
    assert max(np.max(abs(m @ total_charge - total_charge @ m)) for m in effects) < TOLERANCE
    omega = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    joint = np.kron(np.outer(omega, omega.conj()), rho_r).reshape(2, 2, 2, 2, 2, 2)
    mean_state = np.zeros((2, 2), complex)
    output_qfi = variance_means = impurity = total_probability = 0.0
    for effect in effects:
        # Effect-only partial trace: X[a,b,r,c,t,u] M[t,u,b,r].
        tau = np.einsum("abrctu,tubr->ac", joint, effect.reshape(2, 2, 2, 2))
        probability = float(np.trace(tau).real)
        state = tau / probability
        assert np.max(abs(state - state.conj().T)) < TOLERANCE
        mean_state += tau
        total_probability += probability
        mean = float(np.trace(charge_a @ state).real)
        variance_means += probability * (mean - 0.5) ** 2
        impurity += probability * (1 - float(np.trace(state @ state).real))
        output_qfi += probability * qfi(state, charge_a)
    reference_qfi = qfi(rho_r, charge_r)
    assert abs(total_probability - 1) < TOLERANCE
    assert np.max(abs(mean_state - np.eye(2) / 2)) < TOLERANCE
    assert abs(reference_qfi - float(4 * coherence**2)) < TOLERANCE
    assert abs(output_qfi - float(2 * coherence**2)) < TOLERANCE
    harmonic_bound = reference_qfi / (1 + reference_qfi)
    purity_lhs = variance_means + impurity / 2
    purity_rhs = (0.25**2) / (0.25 + reference_qfi / 4)
    assert output_qfi <= harmonic_bound + TOLERANCE
    assert purity_lhs + TOLERANCE >= purity_rhs
    return {
        "off_diagonal_reference_coherence": str(coherence),
        "reference_qfi": reference_qfi,
        "average_output_qfi": output_qfi,
        "harmonic_upper_bound": harmonic_bound,
        "charge_mean_variance": variance_means,
        "average_impurity": impurity,
        "purity_corrected_lhs": purity_lhs,
        "purity_corrected_lower_bound": purity_rhs,
    }


def hermitian_basis(d: int) -> list[np.ndarray]:
    """Hilbert-Schmidt orthonormal traceless basis: diagonal, then off-diagonal."""
    result = []
    for k in range(1, d):
        values = np.zeros(d)
        values[:k] = 1
        values[k] = -k
        result.append(np.diag(values / np.sqrt(k * (k + 1))))
    for i in range(d):
        for j in range(i + 1, d):
            symmetric = np.zeros((d, d), complex)
            antisymmetric = np.zeros((d, d), complex)
            symmetric[i, j] = symmetric[j, i] = 1 / np.sqrt(2)
            antisymmetric[i, j] = -1j / np.sqrt(2)
            antisymmetric[j, i] = 1j / np.sqrt(2)
            result.extend([symmetric, antisymmetric])
    return result


def fisher_frame_check(d: int, k: int) -> dict:
    """Build the complete Fisher quadratic form from finite ensemble states."""
    basis = hermitian_basis(d)
    dimension = d * d - 1
    frame = np.zeros((dimension, dimension))
    for n in counts(k, d):
        probability = float(multinomial(n)) / (3 ** (d - 1))
        for tail in product(range(3), repeat=d - 1):
            phases = np.exp(2j * np.pi * np.array((0,) + tail) / 3)
            psi = np.sqrt(np.array(n) / k) * phases
            means = np.array([np.vdot(psi, h @ psi).real for h in basis])
            frame += probability * np.outer(means, means)
    target = np.diag(
        [1 / (k * d)] * (d - 1)
        + [(k - 1) / (k * d * d)] * (d * (d - 1))
    )
    defect = float(np.max(abs(frame - target)))
    assert defect < TOLERANCE
    return {
        "D": d, "K": k, "frame_defect": defect,
        "diagonal_eigenvalue": str(F(1, k * d)),
        "off_diagonal_eigenvalue": str(F(k - 1, k * d * d)),
        "relative_diagonal": str(F(d + 1, k)),
        "relative_off_diagonal": str(F((d + 1) * (k - 1), k * d)),
    }


def balanced_block_check(dimension: int, k: int) -> dict:
    """Derive block weights by exact binomial enumeration before spectral comparison."""
    assert dimension % 2 == 0 and dimension >= 2
    d = dimension // 2
    same_weight = cross_weight = mean_square = F(0)
    for n_plus in range(k + 1):
        probability = F(comb(k, n_plus), 2**k)
        plus = F(n_plus, k)
        minus = 1 - plus
        same_weight += probability * plus**2
        cross_weight += probability * 2 * plus * minus
        mean_square += probability * (plus - minus) ** 2
    same_rank = d * (d + 1) // 2
    cross_rank = d * d
    same_eigenvalue = same_weight / same_rank
    cross_eigenvalue = cross_weight / cross_rank
    haar = F(2, dimension * (dimension + 1))
    relative_error = max(abs(same_eigenvalue / haar - 1), abs(cross_eigenvalue / haar - 1))
    half_trace_error = (
        2 * same_rank * abs(same_eigenvalue - haar)
        + cross_rank * abs(cross_eigenvalue - haar)
    ) / 2
    assert 2 * same_weight + cross_weight == 1
    assert mean_square == F(1, k)
    assert relative_error == F(abs(dimension + 1 - k), dimension * k)
    assert half_trace_error == abs(F(1, k) - F(1, dimension + 1)) / 2
    return {
        "D": dimension, "K": k, "V_A": "1", "reference_qfi": 4 * (k - 1),
        "multiplicative_error": str(relative_error),
        "half_trace_error": str(half_trace_error),
    }


def run() -> dict:
    exact = []
    spectra = ([0], [2, 2], [0, 1], [0, 1, 2], [0, 2, 5], [0, 0, 1, 1], [0, 1, 1, 2])
    for q in spectra:
        for k in sorted({1, 2, 3, len(q) + 1, len(q) + 2}):
            exact.append(exact_check(list(q), k))
    explicit = [
        povm_check(q, k) for q, k in [
            ([0], 2), ([2, 2], 3), ([0, 1], 2), ([0, 1], 3),
            ([0, 1, 2], 4), ([0, 2, 5], 4), ([0, 0, 1], 4),
        ]
    ]
    mixed = [mixed_reference_check(c) for c in (F(0), F(1, 8), F(1, 4), F(1, 2))]
    frames = [fisher_frame_check(d, k) for d, k in [(2, 1), (2, 3), (3, 2), (3, 4), (3, 5)]]
    blocks = [
        balanced_block_check(d, k)
        for d in (2, 4, 8)
        for k in sorted({1, 2, 3, d + 1, d + 2})
    ]
    return {
        "status": "passed",
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "floating_tolerance": TOLERANCE,
        "counts": {
            "exact_multinomial_cases": len(exact),
            "explicit_povm_cases": len(explicit),
            "mixed_reference_cases": len(mixed),
            "fisher_frame_cases": len(frames),
            "balanced_block_cases": len(blocks),
        },
        "exact_results": exact, "povm_results": explicit,
        "mixed_reference_results": mixed, "fisher_results": frames,
        "balanced_block_results": blocks,
        "scope": "Finite normalization, conservation-sector feasibility, conditional states, mixed-reference bounds, second moments and Fisher frames. General optimality follows from the written proofs; no priority or expert-review certification is implied.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the complete JSON report to this path")
    args = parser.parse_args()
    report = run()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "counts": report["counts"],
        "floating_tolerance": TOLERANCE,
        "max_povm_defect": max(x["povm_defect"] for x in report["povm_results"]),
        "max_steering_defect": max(x["steering_defect"] for x in report["povm_results"]),
        "max_moment_defect": max(x["moment_defect"] for x in report["povm_results"]),
        "max_fisher_defect": max(x["frame_defect"] for x in report["fisher_results"]),
    }, indent=2))
