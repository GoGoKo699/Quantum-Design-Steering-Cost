# Quantum Design Steering Cost

A quantum measurement can prepare random pure states on an entangled partner that it never touches. This project determines the minimum phase coherence that a finite measuring apparatus must supply to make those states an exact 2-design while conserving charge.

Let $A$ have dimension $D$ and charge $Q_A$, and start with a maximally entangled pair $AB$ of fixed total charge. The apparatus acts only on $B$ and an independent reference $R$. Each measurement effect conserves $Q_B+Q_R$, the classical record is neutral, and every outcome is retained. With

$$
V_A=\mathrm{Var}_{I/D}(Q_A),
$$

the exact optimum is

$$
\boxed{
\min_{\text{allowed exact design protocols}}F_Q(\rho_R,Q_R)
=4D V_A.
}
$$

The minimum is attained by a finite conserving measurement for every finite charge spectrum, including degeneracies. Here $F_Q$ is SLD quantum Fisher information, normalized to four times the charge variance on pure states. The optimization is over some weighted exact complex projective state 2-design; the reference may be consumed.

For $m$ qubits with total excitation charge, $D=2^m$ and $V_A=m/4$, so the exact cost is **$m2^m$**. This is a QFI cost. Circuit complexity, locality, apparatus dimension, and mean energy are separate resources.

## Results and their conditions

| Target or quantity | Supported result |
| --- | --- |
| Exact state 2-design on untouched $A$ | Minimum reference QFI $4DV_A$, attained by a finite apparatus |
| Arbitrary mixed conditional outputs | Average output QFI at most $4V_AF_R/(4V_A+F_R)$ |
| Conserving construction with integer $K\geq1$ | Cost $4(K-1)V_A$; exact design at $K=D+1$ |
| Fixed positive additive moment error $\delta$ | A construction with cost at most $4V_A/\delta$ |
| Fixed positive multiplicative moment error | A balanced two-charge counterexample with cost independent of $D$ |
| Two-sided relative Fisher isotropy, exact rank-one effects | A lower bound of order $DV_A$ with a construction at most $4V_A$ above it |

The exact result follows from a reference-information converse and a matching count-and-phase construction. The lower-bound machinery is established finite-reference metrology. The construction satisfies the complete design tensor and the conservation-sector constraints at that bound. The [related-work account](references/RELATED_WORK.md) credits the inherited methods and compares the physical optimization with nearby measurement and projected-ensemble models.

Accuracy is part of the claim. Fixed additive moment error is substantially cheaper than exact design preparation. The usual multiplicative moment condition and relative Fisher isotropy also differ. The results therefore distinguish exact ensemble formation, nearly isotropic rank-one measurements, and general statistical usefulness.

## Read the science

Start with the [scientific overview](science/README.md) or go directly to the [model and exact theorem](science/model.md).

| To inspect | Read |
| --- | --- |
| Mixed-reference converse and exact lower bound | [Reference information](science/reference_bound.md) |
| Count sectors, finite phases, conserving unitary, and reference compression | [Conserving construction](science/conserving_construction.md) |
| Additive and multiplicative error, impurity, and counterexamples | [Accuracy](science/accuracy.md) |
| Tight informational completeness and Fisher symmetry | [Measurement geometry](science/measurement_geometry.md) |
| Output coherence, direct control, qubit scaling, and interpretation | [Physical meaning](science/interpretation.md) |
| Primary comparisons and bibliographic records | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Finite calculations and their limits | [Verification](verification/README.md) |

The design/measurement equivalence is established work: weighted projective 2-designs correspond to tight rank-one informationally complete POVMs, and their local Fisher information at $I/D$ is symmetric. The present optimization assigns a physical reference cost to implementing some measurement in that class.

## Learn the project

The single educational anchor is John Watrous's *The Theory of Quantum Information* (2018), using the author's posted pre-publication manuscript. The [Watrous bridge](learning/WATROUS_BRIDGE.md) identifies the relevant sections, translates notation, and supplies the steps from quantum measurements and Haar moments to the conserving-reference problem.

The [30-milestone understanding map](learning/MILESTONES.md) follows the project's scientific story through 13 background/preliminaries milestones and 17 narrative/innovation milestones. Each milestone states a central question, an understanding target, earlier dependencies, a conceptual connection, and source pointers. Use the bridge alongside the map; the topic-based scientific pages remain authoritative for complete statements and proofs.

| Reading intention | Starting route |
| --- | --- |
| Understand the physical question and the result | [Scientific overview](science/README.md), then [physical interpretation](science/interpretation.md) |
| Build the required foundations and follow the argument | [Watrous bridge](learning/WATROUS_BRIDGE.md) with [M01–M30](learning/MILESTONES.md) |
| Audit the exact optimum | [Operational model](science/model.md), [converse](science/reference_bound.md), and [attaining construction](science/conserving_construction.md) |
| Assess approximate or statistical claims | [Accuracy and purity](science/accuracy.md), then [measurement geometry](science/measurement_geometry.md) |

The [reading guide](llms.txt) maps scientific questions to their canonical files. Primary research sources remain available for attribution and proof dependencies alongside the one educational anchor.

## Reproduce the finite checks

From the repository root:

~~~bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
~~~

The suite checks exact occupation moments and charge-sector identities, explicit finite POVMs, mixed-reference examples, and the approximation and Fisher formulas. The [verification guide](verification/README.md) gives the expected results and explains the scope of each check. Finite calculations do not replace the general proofs or establish literature priority.

## Scope

The input reference is independent, every initial asymmetry resource is counted, and all outcomes are kept. The apparatus can use arbitrary collective conserving interactions and neutral classical randomness. The target is an optimized weighted design, with no claim of the same finite realization for every prescribed SIC, MUB measurement, or Haar ensemble.

General real charge spectra are treated through their generated time translations. A compact $U(1)$ description requires a common charge lattice for the system and apparatus after scalar shifts; the attaining reference shares the system lattice whenever one exists. Efficient local implementation, reference return, and other resource minima are outside the stated QFI optimization. The accuracy and purity conditions remain attached to the corresponding claims.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
