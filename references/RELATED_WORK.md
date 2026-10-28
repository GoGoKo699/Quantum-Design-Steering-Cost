# Related work and attribution

## Contribution and operational scope

The result developed here is an exact, attained reference cost for a specified steering task. Let $A$ and $B$ have dimension $D$, let $Q_A|i\rangle=q_i|i\rangle$, and take $Q_B=-Q_A^T$. The initial state is

$$
|\Omega\rangle_{AB}=\frac{1}{\sqrt D}\sum_i|i\rangle_A|i\rangle_B.
$$

An independent finite reference $R$ may be in any mixed state. Every measurement effect on $BR$ must commute with $Q_B+Q_R$. The protocol leaves $A$ untouched, retains every outcome, and produces a weighted exact complex projective 2-design on $A$. With

$$
\mu=\frac{\mathrm{Tr}Q_A}{D},\qquad
V_A=\frac{\mathrm{Tr}(Q_A-\mu I)^2}{D},
$$

the optimum is

$$
\min F_Q(\rho_R,Q_R)=4DV_A.
$$

Here $F_Q$ is the symmetric logarithmic derivative quantum Fisher information, normalized so that $F_Q(|r\rangle,Q_R)=4\mathrm{Var}_r(Q_R)$. The minimum is attained with a finite pure reference and a finite conserving measurement. The spectrum may contain arbitrary finite real charges and degeneracies. A compact $U(1)$ description requires a common system-apparatus charge lattice after scalar shifts; the theorem itself only needs additive charge conservation.

The optimization allows arbitrary collective invariant POVMs, a finite neutral pointer, classical randomness, and consumption of the reference. All initially coherent helpers belong to $R$. It charges neither circuit complexity nor apparatus dimension, energy, measurement-outcome count, or reference restoration. It optimizes over the design rather than promising the same optimum for every prescribed SIC, set of mutually unbiased bases, or continuous Haar ensemble.

The established ingredients and the conclusion built from them are distinct:

| Ingredient | Primary antecedent | Role here |
| --- | --- | --- |
| QFI loss under an imperfect reference and its covariance form | [Šafránek, Ahmadi, and Fuentes](https://arxiv.org/html/1404.6421v1), Theorem III.2, Eq. (30) | Supplies the finite-reference metrological obstruction. |
| Ensemble decompositions realized by measurements on a purification | [Hughston, Jozsa, and Wootters](https://doi.org/10.1016/0375-9601(93)90880-9) | Converts each feasible charge-sector decomposition into a measurement. |
| Positive effect blocks constrained by battery populations | [Navascués and Popescu](https://arxiv.org/html/1211.2101v3), Appendix B.3 | Gives the relevant structure of conserving measurement feasibility. |
| Coherence and unsharpness constraints on measurement | [Mohammady, Miyadera, and Loveridge](https://arxiv.org/html/2110.11705v3), Appendix G | Places the task within quantitative conservation-limited measurement theory. |
| Weighted 2-design, tight frame, and Fisher-symmetry equivalences | [Scott](https://arxiv.org/html/quant-ph/0604049v6), Proposition 13; [Zhu and Hayashi](https://arxiv.org/html/1709.06112v2), Proposition 1 | Supplies the measurement interpretation of the target. |
| Construction of state designs from amplitudes and phases | [Iosue et al.](https://arxiv.org/html/2311.13479v3), Section 4.1 | Supplies the design architecture. |
| Optimizing and attaining the independent reference cost | This work | Matches the design moments to a charge-convolution reference, attaining $4DV_A$ with a finite count-and-phase measurement. |

Bibliographic keys below refer to [references.bib](references.bib). Comparisons concern the stated models and results; they do not assert an exhaustive absence of other related literature.

## Finite-reference metrology

Quantum Fisher information quantifies local statistical distinguishability, with the measurement optimization developed by Braunstein and Caves ([`Braunstein1994`](https://doi.org/10.1103/PhysRevLett.72.3439)). Its monotonicity under a parameter-independent channel supplies the converse here. For any real $\lambda$, use the input generator

$$
G_\lambda=Q_A+\lambda(Q_B+Q_R).
$$

Invariance of the measurement makes every choice of $\lambda$ induce the same family of conditional states on $A$. The input QFI is $4(1-\lambda)^2V_A+\lambda^2F_R$, where $F_R=F_Q(\rho_R,Q_R)$. Minimization therefore gives

$$
\sum_xp_xF_Q(\rho_x,Q_A)
\leq \frac{4V_AF_R}{4V_A+F_R}.
$$

This parameter-gauge argument is an application of established finite-reference and QFI methods. In particular, Šafránek, Ahmadi, and Fuentes derive the pure-state QFI remaining after a reference-frame twirl as the initial variance minus a sum of squared covariances. Their Theorem III.2, Eq. (30), followed by a classical regression bound, already supplies the pure-reference obstruction used here ([`Safranek2015`](https://arxiv.org/html/1404.6421v1)). The mixed-reference extension can also be obtained from the convex-roof identity $F_Q/4=\min\sum_jw_j\mathrm{Var}_{r_j}(Q_R)$ proved by Yu ([`Yu2013`](https://arxiv.org/abs/1302.5311v1)). The gauge proof handles mixed references directly. Neither QFI monotonicity, gauge optimization, the twirl-covariance identity, nor the convex-roof identity is claimed as a new metrological principle.

For pure conditional states with mean $I/D$, write $v=\mathrm{Var}_x\langle Q_A\rangle_x$. The bound becomes

$$
v\geq\frac{V_A^2}{V_A+F_R/4}.
$$

The design target fixes $v=V_A/(D+1)$, giving $F_R\geq4DV_A$. This substitution is elementary once the inherited bound is available. The substantive additional task is to attain it while satisfying the entire second-moment identity and every charge-sector measurement constraint. Exact equality of the second moment to the Haar second moment already forces conditional purity: its SWAP expectation is one, so every nonzero-weight conditional state has purity one.

The public [Quantum Control Coherence](https://github.com/GoGoKo699/Quantum-Control-Coherence/tree/6e1f9c966b98602c30c6d747eafe96d467b76112) repository provides a related conserving-controller comparison (`QuantumControlCoherence2026`). At the pinned revision it optimizes entropic coherence and controller dimension for a fixed unitary acting on an unknown input, in the limit of vanishing implementation error. Its leading coefficient is controlled by the rational rank of active transition frequencies. The present task optimizes QFI for a measurement-defined ensemble, has a finite exact endpoint, and can vary the target within the class of 2-designs. The resource measures, operations, and asymptotic questions differ. Both models allow a finite mixed controller without requiring its return.

## Conservation-limited measurements

Navascués and Popescu formulate measurement restrictions using an explicit energy battery ([`Navascues2014`](https://arxiv.org/html/1211.2101v3)). Appendix B.3, “Extension to multi-level systems,” describes the effective POVM through positive blocks whose sums are fixed by battery populations. This is the structural antecedent of the sectorwise feasibility condition used here. Their displayed multilevel treatment assumes nondegenerate system and battery spectra. The construction here allows system degeneracies and coincident charge sums by keeping system basis labels distinct and combining equal reference charges. Appendix B.3 is the stable locator because equation numbering differs between available renderings.

Mohammady, Miyadera, and Loveridge establish measurement-disturbance and conservation bounds for general observables, including unsharp measurements ([`Mohammady2023`](https://arxiv.org/html/2110.11705v3)). Appendix G, Proposition G.1, relates effect commutators to apparatus QFI. Its stronger unsharpness-dependent Eq. (38) additionally assumes an extremal observable. A redundant rank-one design POVM need not satisfy that extremality assumption. These results establish the relevance of apparatus coherence and effect unsharpness; the optimized ensemble-wide factor $D$ and a matching finite implementation are separate conclusions requiring the design constraint.

Tajima and Nagaoka study the coherence cost of approximately measuring a prescribed sharp observable, using a root-mean-square error criterion and a Yanase-compatible pointer ([`Tajima2019`](https://arxiv.org/abs/1909.02904v1)). Their small-error measurement-cost analysis is a close antecedent for resource optimization under conservation. An exact unsharp design measurement optimized over its effects poses a different endpoint. Broader symmetry, irreversibility, and resource-cost inequalities appear in Tajima, Takagi, and Kuramochi, especially their main trade-off and supplementary approximate-measurement analysis ([`Tajima2022Tradeoff`](https://arxiv.org/html/2206.11086v2)), and in the general-resource channel framework of Tajima, Yamaguchi, Takagi, and Kuramochi ([`Tajima2025Tradeoff`](https://arxiv.org/html/2507.23760v1)). The present converse belongs to this established family of resource constraints; the claimed optimum additionally requires constructive saturation for the specified target.

### Finite realization and the role of ensemble steering

The Hughston-Jozsa-Wootters theorem realizes any finite ensemble decomposition of a density operator by a suitable measurement on its purification ([`Hughston1993`](https://doi.org/10.1016/0375-9601(93)90880-9)). Applying it separately inside fixed total-charge sectors gives a conserving measurement whenever the desired ensemble has the correct sectorwise average. HJW does not by itself choose a reference whose sectors support a 2-design at minimum QFI.

The construction here makes that choice explicitly. For integer $K\geq1$, take $K-1$ independent uniform charge samples $-q_i$ and coherently encode their sum in a finite reference. If $r_s$ is the resulting probability distribution, then

$$
|r\rangle=\sum_s\sqrt{r_s}|s\rangle,
\qquad F_R=4(K-1)V_A.
$$

Draw $N\sim\mathrm{Multinomial}(K;1/D,\ldots,1/D)$ and independent third-root phases $\phi_i$. The output vectors are

$$
|\psi_{N,\phi}\rangle
=\sum_i\sqrt{N_i/K}\,e^{i\phi_i}|i\rangle.
$$

For the total external charge $t=-\sum_jq_jN_j$, exchangeability gives

$$
\mathbb E\left[\frac{N_i}{K}
\mathbf1_{\{-\sum_jq_jN_j=t\}}\right]
=\frac{r_{t+q_i}}{D}.
$$

This identity supplies exactly the diagonal weights required in every charge sector. Phase averaging supplies the vanishing off-diagonal entries. A direct count measurement followed by a finite phase POVM implements these decompositions and verifies completeness, so finite realization does not depend on an unexplained appeal to HJW. At $K=D+1$, the multinomial second moments equal the Haar moments and the cost is $4DV_A$. This simultaneous match of the design and conservation constraints is the constructive content of the optimum.

## State designs and tomography

Scott proves that tight rank-one informationally complete POVMs are precisely weighted complex projective 2-designs, with the appropriate normalization ([`Scott2006`](https://arxiv.org/html/quant-ph/0604049v6), Proposition 13 and Eq. (61)). Zhu and Hayashi identify the corresponding Fisher-symmetric measurement condition at the maximally mixed state ([`Zhu2018`](https://arxiv.org/html/1709.06112v2), Proposition 1 and Supplement V, Eqs. (S56)-(S59)). This is the single-copy, maximally mixed-state statement; their paper also treats distinct collective-measurement questions. The information trade-offs underlying Fisher symmetry belong to the established Gill-Massar framework ([`Gill2000`](https://doi.org/10.1103/PhysRevA.61.042312)).

For the steering ensemble, the effective POVM on $B$ is $E_x=Dp_x\rho_x^T$. For a traceless Hermitian $H$, the local statistical model $\sigma_\theta=e^{\theta H}/\mathrm{Tr}(e^{\theta H})$ has classical Fisher information

$$
J_H(0)=\sum_xp_x\big[\mathrm{Tr}(H\rho_x^T)\big]^2.
$$

An exact 2-design gives $J_H(0)=\mathrm{Tr}(H^2)/[D(D+1)]$. Consequently the reference optimum also applies to the class of tight rank-one informationally complete measurements implemented in this conserving model. The design/frame/Fisher equivalence is inherited; the optimized physical reference cost is the result supplied here.

### Amplitude and phase constructions

Iosue, Mooney, Ehrenberg, and Gorshkov develop projective toric designs and explain how a simplex design for squared amplitudes combines with a phase design to give a complex projective state design ([`Iosue2024Toric`](https://arxiv.org/html/2311.13479v3), Section 4.1). Their factorization of Fubini-Study integration supplies the relevant architecture. The finite third-root phase average and multinomial amplitudes used here are a concrete second-moment realization of that architecture. The additional physical identity is their compatibility with an independent charge-convolution reference in every sector. Neither the amplitude-phase decomposition nor the general production of finite state designs is claimed as new.

### Accuracy changes the resource question

Let $S$ be SWAP and $\Pi_{\rm diag}=\sum_i|ii\rangle\langle ii|$. The count-and-phase family has

$$
M_K=\frac{K-1}{KD^2}(I+S)
+\frac{D+1-K}{KD^2}\Pi_{\rm diag},
\qquad M_H=\frac{I+S}{D(D+1)}.
$$

Its additive error, using half the trace norm, is exactly

$$
\delta_K=\frac12\|M_K-M_H\|_1
=\frac{D-1}{D}\left|\frac1K-\frac1{D+1}\right|.
$$

Thus fixed positive additive error is attainable with $K=O(1/\delta)$ and reference QFI $O(V_A/\delta)$, with no additional factor of $D$. Low-resource additive designs already occur in other operational settings. Lee, Hhan, Cho, and Kwon construct approximate designs with low entanglement, magic, and coherence and give shallow preparation circuits ([`Lee2026`](https://arxiv.org/html/2507.17871v3)). Their Eq. (6) uses additive moment trace distance, and Theorem 1 gives resources independent of the number of qubits at fixed design order and error. Those resources concern directly prepared states and circuits, rather than an independent reference implementing a conserving remote measurement. The relevant addition here is the explicit conserving realization and its QFI accounting, not the general possibility of inexpensive additive approximate designs.

A stronger operational criterion is two-sided relative Fisher isotropy. For rank-one effects, impose, for every traceless $H$,

$$
(1-\varepsilon)\frac{\mathrm{Tr}(H^2)}{D(D+1)}
\leq J_H(0)\leq
(1+\varepsilon)\frac{\mathrm{Tr}(H^2)}{D(D+1)},
\qquad 0\leq\varepsilon<1.
$$

The charge direction and the converse yield

$$
F_R\geq4V_A\left[\frac{D+1}{1+\varepsilon}-1\right].
$$

For the count-and-phase family, the Fisher eigenvalues relative to the exact-design value are $(D+1)/K$ on traceless diagonal operators and $(D+1)(K-1)/(KD)$ on operators with zero diagonal. Choosing $K=\lceil(D+1)/(1+\varepsilon)\rceil$ satisfies the criterion at cost at most $4V_A$ above the displayed lower bound, with a strict inequality when $V_A>0$. This is a controlled corollary, without a claim to the exact noninteger cost frontier.

The qualification matters physically. Extra information in a charge direction is not itself detrimental to tomography. With $K=O(1/\varepsilon)$, this same family already achieves a competitive one-sided lower Fisher bound in every direction, while enhancing diagonal information. Exact rank one and two-sided isotropy are therefore essential to the stated large cost. The theorem does not establish an exponential resource requirement for useful tomography, mixed-effect approximate measurements, or ordinary additive approximate designs. Nor does a positive-semidefinite multiplicative sandwich for the state moment automatically imply the required relative charge-variance estimate: the witness $(Q_A-\mu I)\otimes(Q_A-\mu I)$ is indefinite.

The distinction from direct preparation is also explicit. Starting with $|u\rangle=D^{-1/2}\sum_i|i\rangle$, diagonal Kraus operators $K_x=\sqrt{Dp_x}\mathrm{diag}(\psi_{x1},\ldots,\psi_{xD})$ prepare any pure ensemble with average $I/D$. They commute with $Q_A$, and the input has QFI $4V_A$. This is a direct-preparation upper bound with initial coherence on the prepared system. The steering theorem fixes that system initially at $I/D$ and permits operations only on its partner and an independent reference.

## Projected ensembles and deep thermalization

Cotler and collaborators established the emergence of state-design ensembles by measuring part of a many-body wave function ([`Cotler2023`](https://doi.org/10.1103/PRXQuantum.4.010311)). This provides the projected-ensemble setting in which design moments capture information beyond the ordinary reduced state. It already connects conditional pure-state ensembles, random-state moments, and many-body dynamics.

Symmetry and measurement basis are central in subsequent work. Varikuti and Bandyopadhyay give conditions for design emergence in symmetric systems, including the $U(1)$ case in Section 5.3 ([`Varikuti2024`](https://arxiv.org/html/2402.08949v3)). Chang, Shrotriya, Ho, and Ippoliti analyze charge-conserving deep thermalization, including charge-revealing and charge-nonrevealing measurements and the corresponding generalized Scrooge ensembles ([`Chang2025`](https://arxiv.org/html/2408.15325v2), Sections III-V). These results determine how initial charge statistics and a prescribed measurement basis shape a projected ensemble. They do not optimize a separately modeled, finite measurement reference by its initial QFI.

Two 2026 works make the resource connection more explicit. Varikuti, Bandyopadhyay, and Hauke use deep thermalization to measure quantum resources ([`Varikuti2026Resources`](https://arxiv.org/html/2512.09999v3), Theorems 1-2 and the coherence analysis in the supplement; published 26 October 2026). Their resource-generating-power and projected-ensemble relations already preclude treating a general connection between designs and quantum resources as a new contribution here. The independent, finite apparatus and its exact optimized QFI are additional model choices in the present task.

Feng, Liu, Cheng, Ho, and Ippoliti develop a framework for quantum-resource localizability in deep thermalization ([`Feng2026`](https://arxiv.org/html/2606.08756v1)). Section II.2 explicitly counts resource injection through the initial state and measurement basis. Section V.2 studies asymmetry using Wigner-Yanase skew information, which reduces to charge variance on pure states. Their allowed asymmetry-preserving dynamics include block transpositions $Q\leftrightarrow N-Q$; these need not conserve the numerical charge. Appendix D studies a threshold for nonlocal initial states within that framework. This is a substantive antecedent for resource constraints on projected ensembles. Its thermodynamic localizability question and operation class differ from the exact conservation and independent-reference optimization posed here.

The present model isolates a measurement-resource question from that broader dynamical setting: even when the initial pair has sharp total charge and exactly maximally mixed marginals, which finite independent reference permits its conditional ensemble to have the exact second Haar moment? The theorem answers this question for the maximally entangled pair and optimized invariant measurement. It does not assign the same cost to generic many-body initial states, local measurement circuits, finite-time deep thermalization, or approximate ensembles without checking their distinct assumptions.

## Source versions and limits of the comparison

The linked arXiv versions fix the section and equation references above. Journal metadata in [references.bib](references.bib) follow the publisher records, including the October 2026 resource-measurement paper and the April 2026 low-resource-design paper. Preprints are labeled as such. The pinned controller repository is cited as a scientific repository rather than a journal publication.

The central attribution is consequently narrow and testable: established finite-reference metrology supplies the lower-bound machinery; established ensemble, measurement, and design theory supplies the framework; the result here is the attained $4DV_A$ optimum, its finite conserving realization, and the explicit separation between exact design cost, additive moment accuracy, and rank-one relative Fisher isotropy.
