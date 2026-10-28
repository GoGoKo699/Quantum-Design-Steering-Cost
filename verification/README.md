# Verification

The written proofs establish the all-spectrum reference bound, finite attainment, and accuracy statements. The calculations here check their finite formulas and implementation against direct occupation enumeration, explicit POVM matrices, conditional-state contractions, and complete Fisher frames.

## Run

From the repository root, with Python 3.12:

~~~bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
~~~

The numerical dependency is pinned to NumPy 2.3.5. Exact occupation and block-moment calculations use Python's standard-library rational arithmetic. No network access, credentials, quantum hardware, or external data are needed during the checks.

To produce the complete report:

~~~bash
python3 verification/run_all.py --output verification/results.json
~~~

The committed [results.json](results.json) was generated with Python 3.12.14 and NumPy 2.3.5. The command prints a compact summary and exits unsuccessfully if a checked identity or tolerance fails. Floating-point residuals can vary slightly across numerical libraries and platforms; the pass criterion is the stated tolerance, not bitwise equality with the committed residuals.

## What is checked

| Calculation | Method | Scientific failure mode addressed |
| --- | --- | --- |
| Occupation moments and reference charge distribution | Exact rational enumeration | Missing multiplicities, wrong normalization, or an incorrect QFI scale |
| Charge-sector compatibility | Exact rational sector sums | A target ensemble that cannot be produced by the proposed conserving apparatus |
| Full finite POVMs on the compressed reference | Direct matrix sums and conditional contractions | Incomplete effects, mishandled degenerate charges, or wrong steered amplitudes |
| Mixed-reference information and purity bounds | Spectral SLD QFI and direct partial traces | Confusing mixed-state variance with QFI or using the wrong conditional-state normalization |
| Fisher quadratic form | Finite phase enumeration in a full traceless Hermitian basis | Missing directions, incorrect transpose conventions, or a factor error in the isotropy scale |
| Balanced-charge multiplicative counterexample | Exact binomial block weights and spectral ratios | Confusing additive and multiplicative errors or claiming an unsupported dimension factor |

The finite set includes a one-dimensional system, scalar charge, repeated charge values, unequal charge gaps, and values of $K$ on both sides of the exact design point.

### Exact charge-sector check

For a count vector $N$, the script constructs its multinomial probability directly from factorials. The reference distribution is the negative sum of $K-1$ uniform charge samples, with colliding charges combined. It then verifies, for every occupied total charge $t$ and system label $i$,

$$
\sum_{N:\,-\sum_jq_jN_j=t}
\Pr(N)\frac{N_i}{K}
=\frac{r_{t+q_i}}{D}.
$$

This identity is the compressed-reference feasibility condition. The rational check also verifies the first moment, every amplitude second moment, the reference variance, and the conditional charge-mean variance.

### Explicit compressed POVM

In each total-charge block, use basis vectors $(i,s)$ with $s-q_i=t$. For an outcome $(N,\phi)$ of probability $p_{N,\phi}$, the measurement bra has coefficient

$$
\sqrt{\frac{D\,p_{N,\phi}\,N_i}{K\,r_s}}\,e^{i\phi_i}
$$

on that basis vector. The script sums the effects to the identity within each block and contracts the bra with the actual input amplitudes. It also constructs the entire two-copy moment from the resulting state vectors. A redundant global phase is fixed; this leaves all state rays and moment averages unchanged.

### Mixed reference

The reference is the qubit state with diagonal entries $1/2$ and real off-diagonal entry $c$, for $c=0,1/8,1/4,1/2$. The measurement resolves the extreme external charges and the symmetric/antisymmetric combinations in the middle charge sector. The script evaluates QFI from the spectral definition and obtains the conditional states by an effect-only partial trace. It checks both the harmonic bound and the impurity correction, including pure and mixed endpoints.

## Recorded result

The suite passes:

| Group | Cases |
| --- | ---: |
| Exact multinomial and sector calculations | 31 |
| Explicit finite POVMs | 7 |
| Mixed reference examples | 4 |
| Complete Fisher frames | 5 |
| Balanced-charge block moments | 14 |

The floating-point tolerance is $10^{-12}$. In the committed run, the largest POVM-completeness residual is below $8\times10^{-16}$, the largest conditional-amplitude residual below $7\times10^{-17}$, and the moment and Fisher residuals below $4\times10^{-16}$.

These are finite certificates for the implemented examples. They do not prove arbitrary-dimensional optimality, validate every possible apparatus, establish efficient gate synthesis, or certify the literature comparison. Those questions are addressed, at their stated scope, by the [scientific account](../science/README.md) and [primary-source attribution](../references/RELATED_WORK.md).
