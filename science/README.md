# Scientific account

This account derives the exact reference-coherence cost of generating a state 2-design by measuring only the entangled partner of an untouched system. The result is a minimum over finite conserving apparatuses and some weighted exact design:

$$
F_{Q,\min}=4D\,\mathrm{Var}_{I/D}(Q_A).
$$

The proof combines an established finite-reference information bound with a finite count-and-phase measurement that attains it. The accuracy analysis states which approximations preserve the dimension factor and which do not.

## Reading route

| Question | Authoritative page |
| --- | --- |
| What is supplied, allowed, retained, and charged? | [Model and exact optimum](model.md) |
| Why must the reference have this QFI, even when mixed? | [Reference information bound](reference_bound.md) |
| How is the exact design produced by a finite conserving apparatus? | [Conserving construction](conserving_construction.md) |
| What changes under additive error, multiplicative error, or mixed outputs? | [Accuracy and purity](accuracy.md) |
| How does the result describe tight IC measurements and Fisher isotropy? | [Measurement geometry](measurement_geometry.md) |
| Why do remote access, exactness, and resource accounting matter? | [Physical interpretation](interpretation.md) |

For a direct theorem audit, read the operational model, Theorem 1 and Theorem 3 in the reference-bound page, then Sections 2–7 of the construction. The resulting law is exact for arbitrary finite charge spectra, including degeneracies. The construction's unrestricted collective interactions and consumable reference are part of the model.

The second-moment error and relative Fisher error are different objects. Their distinction is necessary for assessing the strength of any approximate statement. The balanced-charge example in the accuracy page supplies an explicit counterexample to a universal fixed-multiplicative-error dimension factor.

The [source comparison](../references/RELATED_WORK.md) identifies inherited methods and the matched apparatus optimization. The [verification guide](../verification/README.md) documents exact rational checks and finite matrix calculations. These calculations support the formulas and implementation; the general results rest on the written proofs.
