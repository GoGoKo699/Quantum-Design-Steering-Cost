# From Watrous to the reference cost of design steering

A Bell pair has maximally mixed marginals, yet measuring one qubit can prepare pure states on the other. The conditional state depends on the measurement outcome; averaging over all outcomes restores the original marginal. This project asks what a finite measuring apparatus must supply when every operation conserves charge and the remote system is never touched.

The selected educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. Section references below use the author's **2018 prepublication manuscript**, whose preface is dated January 2018. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies publication of the book in April 2018 and provides the [complete manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf) and [contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf). The manuscript is linked rather than reproduced here.

Watrous supplies the finite-dimensional state, channel, measurement, and Haar-integration framework. The bridge below adds the reference-resource model, quantum Fisher information, and the connections needed for the exact cost theorem. The [30-milestone map](MILESTONES.md) organizes these connections; the [scientific model](../science/model.md) fixes the theorem's full assumptions.

## Targeted reading

Use the relevant sections as the corresponding objects arise. The route does not require reading the whole book first.

| Milestones and purpose | Watrous manuscript pointers | Foundation used here |
| --- | --- | --- |
| M01–M02: states and composites | [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Density operators, partial trace, and purification. |
| M03–M04: measurements and steering | [Sections 2.3.1–2.3.3 and Exercise 2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | POVMs and ensembles; Exercise 2.2 is the HJW steering statement, attributed in Section 2.5. |
| M08 and M20: channels and implementation | [Sections 2.2.1–2.2.2 and 2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Channel representations; Theorem 2.42 and its following corollary give measurement dilation. |
| M09–M10: the moment target | [Sections 7.1.1–7.1.2 and 7.2.1–7.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Symmetric tensors and Haar averages; Lemma 7.24, Eq. (7.159), gives the normalized symmetric-projector moment. |
| M12 and M22–M24: error and purity | [Section 1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and [Section 3.1.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Operator norms and state distinguishability. |

The charge restriction, QFI data processing, comparison-generator argument, finite count-and-phase construction, and Fisher-isotropy results are supplied below and in the linked scientific pages. They are not presented as theorems from Watrous.

## Notation and conventions

| Watrous notation | Notation here | Meaning |
| --- | --- | --- |
| $`u,u^*,uu^*`$ | $`\lvert\psi\rangle,\langle\psi\rvert,\lvert\psi\rangle\langle\psi\rvert`$ | Vector, adjoint, and pure-state projector. |
| $`\mathcal X,\mathcal Y`$ | $`\mathcal H_A,\mathcal H_B,\mathcal H_R`$ | Finite Hilbert spaces. |
| $`\mu(x)`$ | $`M_x`$ or $`E_x`$ | An effect on the apparatus space $BR$, or its effective effect on $B$. |
| $`\eta(x)`$ | $`\tau_x=p_x\rho_x`$ | An unnormalized ensemble member. |
| $`\mathrm{Tr}_{\mathcal Y}`$ | $`\mathrm{Tr}_B`$, for example | Ordinary partial trace, without a dimension-normalizing factor. |
| $`\lVert X\rVert_1`$ | The same trace norm | Moment distance here includes the factor $`1/2`$. |

Here $`D=\dim\mathcal H_A=\dim\mathcal H_B`$. The charge $`Q_A`$ is Hermitian, with eigenvalues $`q_i`$, and

```math
\mu=\frac{\mathrm{Tr}Q_A}{D},\qquad
H_A=Q_A-\mu I,\qquad
V_A=\frac{\mathrm{Tr}H_A^2}{D}.
```

Thus $`V_A`$ is the variance of charge in the maximally mixed state. The symbol $`F_Q`$ denotes symmetric logarithmic derivative quantum Fisher information, with $`F_Q(|\psi\rangle,Q)=4\mathrm{Var}_{\psi}(Q)`$. It is distinct from the fidelity function in Watrous Chapter 3. Charge units remain fixed; scaling every charge by $`a`$ scales both $`V_A`$ and $`F_Q`$ by $`a^2`$.

When $`V_A=0`$, the system charge is scalar and the optimal reference cost is zero. A reference-bound fraction with both numerator and denominator zero is defined to be zero throughout this guide.

## Steering from a fixed average

For M02–M04, begin with

```math
|\Omega\rangle_{AB}
=\frac1{\sqrt D}\sum_{i=1}^D|i\rangle_A|i\rangle_B.
```

Each marginal is $`I/D`$. An apparatus initialized independently of $AB$ induces some effective POVM $`\{E_x\}`$ on $B$. Expanding the entangled state in its paired basis gives

```math
\tau_x=\mathrm{Tr}_B[(I\otimes E_x)|\Omega\rangle\langle\Omega|]
=\frac{E_x^{\mathsf T}}{D},\qquad
p_x=\frac{\mathrm{Tr}E_x}{D},\qquad
E_x=Dp_x\rho_x^{\mathsf T}.
```

The transpose is a consequence of the paired basis, not a physical transpose operation. An effect of rank one produces a pure conditional state. Completeness, $`\sum_xE_x=I`$, fixes the average:

```math
\sum_xp_x\rho_x=I/D.
```

Different measurements can therefore produce different pure decompositions of the same mixed marginal. The outcome tells us which conditional state was prepared. No signal changes the unconditional state of $A$.

Watrous's Exercise 2.2 provides the general purification-to-ensemble connection. The restriction introduced here is that the measurement itself must have a conserving implementation using a counted reference. This turns an ensemble-existence statement into a physical resource question. The [effective-POVM derivation](../science/measurement_geometry.md#1-from-remote-preparation-to-a-povm) treats the correspondence precisely.

The target ensemble has second moment

```math
M_2=\sum_xp_x\rho_x\otimes\rho_x
=M_{\mathrm H}:=\frac{I+S}{D(D+1)},
```

where $`S`$ swaps the two copies. Every vector $`|\psi\rangle^{\otimes2}`$ lies in the symmetric subspace. Its projector is $`(I+S)/2`$, with dimension $`D(D+1)/2`$; Haar invariance and trace normalization give the displayed average. A weighted state 2-design reproduces this average with finitely many states and probabilities.

This condition determines fluctuations of every expectation value. For the centered charge,

```math
v:=\sum_xp_x[\mathrm{Tr}(H_A\rho_x)]^2
=\mathrm{Tr}[(H_A\otimes H_A)M_{\mathrm H}]
=\frac{V_A}{D+1}.
```

The first equality uses the fixed mean. The last uses $`\mathrm{Tr}H_A=0`$ and $`\mathrm{Tr}[(X\otimes Y)S]=\mathrm{Tr}(XY)`$. These small fluctuations of conditional charge means will determine the reference cost.

## Conservation and an independent reference

M05–M06 and M13 specify the physical model. Pair the system charge with

```math
Q_B=-Q_A^{\mathsf T},\qquad
(Q_A+Q_B)|\Omega\rangle=0.
```

The source has sharp total charge, even though each marginal has charge fluctuations. Supply a finite reference $R$ in an arbitrary state $`\rho_R`$, independently of $AB$. The allowed effects on $BR$ obey

```math
M_x\geq0,\qquad \sum_xM_x=I_{BR},\qquad
[M_x,T]=0,\qquad T=Q_B+Q_R.
```

The last condition says that an effect never connects different eigenspaces of total external charge. It can contain coherent superpositions within one such eigenspace. This distinction lets the apparatus compare phases relationally without breaking total charge conservation.

Each outcome label is neutral: the symmetry leaves it fixed. Every outcome is retained. Postselecting a subset can change the ensemble average and is outside this all-outcome task. A neutral random choice can be part of the record, while every initially asymmetric helper belongs to $R$. If an accessible flag identifies which coherent reference state was prepared, that flag remains part of the state whose QFI is charged.

The apparatus may consume the reference. Arbitrary collective invariant measurements and a finite neutral pointer are allowed. The optimized quantity is initial reference QFI; the [model](../science/model.md) separately identifies uncharged quantities such as apparatus dimension, energy, locality, and circuit size. Arbitrary finite real charges and degeneracies are permitted. Calling the symmetry compact $U(1)$ additionally requires a common charge lattice after scalar shifts.

## Quantum Fisher information as the reference cost

M07–M08 add a statistical tool to the channel framework. Consider a family

```math
\rho_\theta=e^{-i\theta Q}\rho e^{i\theta Q}.
```

For an observed distribution $`p_x(\theta)`$, classical Fisher information is $`\sum_x[p_x'(\theta)]^2/p_x(\theta)`$. It measures local sensitivity to a small parameter change. Maximizing this sensitivity over measurements on the state gives the SLD QFI. Equivalently, choose a Hermitian $`L_\theta`$ satisfying

```math
\frac{L_\theta\rho_\theta+\rho_\theta L_\theta}{2}
=\frac{d\rho_\theta}{d\theta},\qquad
F_Q(\rho_\theta)=\mathrm{Tr}(\rho_\theta L_\theta^2).
```

For a pure family, the component of $`d|\psi_\theta\rangle/d\theta`$ parallel to the state only changes its phase. Removing that component gives

```math
F_Q=4\left(\langle\dot\psi|\dot\psi\rangle
-|\langle\psi|\dot\psi\rangle|^2\right)
=4\mathrm{Var}_{\psi}(Q).
```

Mixed-state variance has an additional classical contribution. For a qubit with $`Q=|1\rangle\langle1|`$, both $`|+\rangle`$ and $`I/2`$ have variance $`1/4`$. The former has QFI one; the latter has QFI zero because the rotation leaves it unchanged. This is why the resource is $`F_R=F_Q(\rho_R,Q_R)`$, including mixed references, rather than four times an arbitrary apparatus variance.

Three properties connect this definition to the proof. First, a parameter-independent channel cannot increase QFI: any measurement of its output is also a possible measurement strategy on its input, obtained by preceding that measurement with the channel. Second, QFI adds for independent product families. Their SLDs add, and the cross term vanishes because each SLD has zero expectation. Third, a retained classical flag with parameter-independent probabilities gives

```math
F_Q\!\left(\sum_xp_x|x\rangle\langle x|\otimes\rho_{x,\theta}\right)
=\sum_xp_xF_Q(\rho_{x,\theta}).
```

The flag makes the conditional sensitivities accessible. If its probabilities depended on the parameter, an additional classical Fisher term would appear. The [reference-bound proof](../science/reference_bound.md) supplies the exact finite-dimensional argument and research attribution for these QFI ingredients.

## The comparison generator and the bound

M14–M16 use conservation to sharpen ordinary QFI monotonicity. Let $`\mathcal M`$ be the channel that measures $BR$, keeps the outcome and $A$, and discards the apparatus. For any real $`\lambda`$, introduce

```math
G_\lambda=Q_A+\lambda(Q_B+Q_R).
```

This is an auxiliary encoding for comparing distinguishability. The protocol itself still leaves $A$ untouched. Because each effect commutes with $T$, an input rotation generated by $`\lambda T`$ disappears under the measurement and partial trace. The $A$ rotation passes through. Every $`\lambda`$ therefore produces the same output family,

```math
\sum_xp_x|x\rangle\langle x|\otimes
e^{-i\theta Q_A}\rho_xe^{i\theta Q_A}.
```

Its QFI is the average conditional QFI. On the input, sharp total charge gives

```math
(Q_A+\lambda Q_B)|\Omega\rangle
=(1-\lambda)Q_A|\Omega\rangle.
```

Product additivity now makes the input QFI exactly $`4(1-\lambda)^2V_A+\lambda^2F_R`$. The same output must satisfy data processing for every choice of the comparison generator, so

```math
\sum_xp_xF_Q(\rho_x,Q_A)
\leq\min_{\lambda\in\mathbb R}
\left[4(1-\lambda)^2V_A+\lambda^2F_R\right]
=\frac{4V_AF_R}{4V_A+F_R}.
```

The minimizing value is $`\lambda=4V_A/(4V_A+F_R)`$ when the denominator is positive. If both quantities vanish, the bound is zero. The reasoning includes mixed references and mixed conditional states.

For pure outputs, the fixed average gives a useful division of charge fluctuations:

```math
\sum_xp_x\mathrm{Var}_{\rho_x}(Q_A)=V_A-v.
```

The left side describes uncertainty within each conditional state; $v$ describes variation of its mean from outcome to outcome. Substituting the pure-state QFI formula yields

```math
v\geq\frac{V_A^2}{V_A+F_R/4}.
```

A design requires $`v=V_A/(D+1)`$, hence $`F_R\geq4DV_A`$. Exact moment equality already ensures purity even if it was not initially assumed: $`\mathrm{Tr}(SM_2)=\sum_xp_x\mathrm{Tr}\rho_x^2=1`$ forces every positive-weight output to be pure. The [canonical converse](../science/reference_bound.md) includes the charge-sector covariance interpretation. Its finite-reference metrological ingredients are inherited; [Related work](../references/RELATED_WORK.md#finite-reference-metrology) identifies them.

## Finite count and phase attainment

M17–M21 show why the lower bound is reachable. Choose an integer $`K\geq1`$ and take $`K-1`$ reference factors, each in $`|+_D\rangle=D^{-1/2}\sum_i|i\rangle`$ with charge $`-q_i`$ on label $i$. Independence gives

```math
F_R=4(K-1)V_A.
```

Count the labels across $B$ and those reference factors. The resulting vector $`N=(N_1,\ldots,N_D)`$ has $`\sum_iN_i=K`$ and total external charge $`t_N=-\sum_iq_iN_i`$. Resolving this count preserves charge, including when distinct counts have the same charge.

There are $`C_N=K!/\prod_iN_i!`$ strings with count $N$. Among them, the number with $B$ label $i$ is

```math
C_{i,N}=\frac{N_i}{K}C_N.
```

Let $`|u_{i,N}\rangle`$ be $`|i\rangle_B`$ tensored with the normalized equal superposition of the corresponding reference strings. These vectors are orthonormal and share charge $`t_N`$. The input restricted to this count sector has amplitudes proportional to $`\sqrt{C_{i,N}}`$. This counting identity is the origin of the output amplitudes $`\sqrt{N_i/K}`$.

Choose each $`\phi_i`$ independently from $`0,2\pi/3,4\pi/3`$. Within the occupied subspace use

```math
|v_{N,\phi}\rangle=\sum_{i:N_i>0}e^{-i\phi_i}|u_{i,N}\rangle,
\qquad M_{N,\phi}=3^{-D}|v_{N,\phi}\rangle\langle v_{N,\phi}|.
```

Phase averaging removes cross terms, so the effects sum to the projector onto the occupied subspace. An invariant complementary effect completes the POVM on the full space and has zero probability on the supplied input. It is included, not postselected away. Contracting a phase bra with the input gives

```math
|\psi_{N,\phi}\rangle
=\sum_i\sqrt{N_i/K}\,e^{i\phi_i}|i\rangle,
\qquad
p_{N,\phi}=\frac{C_N}{D^K3^D}.
```

Thus $N$ is multinomial and the phases are independent and uniform. The phases label effects within a fixed charge sector; they do not require an additional uncounted phase reference.

To check the design, use

```math
\mathbb E[(N_i/K)^2]=\frac{K+D-1}{KD^2},\qquad
\mathbb E[N_iN_j/K^2]=\frac{K-1}{KD^2}\quad(i\ne j).
```

In a second moment, every individual phase exponent lies between $-2$ and $2$. Averaging over three roots kills every nonzero exponent. With $`\Pi_{\mathrm{diag}}=\sum_i|ii\rangle\langle ii|`$, the surviving terms give

```math
M_K=\frac{K-1}{KD^2}(I+S)
+\frac{D+1-K}{KD^2}\Pi_{\mathrm{diag}}.
```

At $`K=D+1`$, the correction vanishes and the cost is $`4DV_A`$. This matches the converse with an explicit finite measurement.

The usual measurement dilation can also respect conservation. With a neutral pointer, define $`W|\eta\rangle=\sum_xM_x^{1/2}|\eta\rangle|x\rangle`$. Completeness makes $W$ an isometry, and commutation of each square root with $T$ means it preserves every charge sector. Extending it to a unitary separately in each sector produces a conserving realization. This is the extra step beyond unrestricted Naimark dilation. The [complete construction](../science/conserving_construction.md) proves completeness, the neutral-pointer implementation, and compression to one reference vector per distinct charge.

## A complete qubit example

Take $`Q_A=|1\rangle\langle1|`$, $`Q_B=-|1\rangle\langle1|`$, and the Bell state $`(|00\rangle+|11\rangle)/\sqrt2`$. Then $`D=2`$, $`\mu=1/2`$, and $`V_A=1/4`$. The exact design point is $`K=3`$.

Use a compressed three-level reference whose ket labels denote its charges:

```math
|r\rangle_R=\frac{|0\rangle+\sqrt2|-1\rangle+|-2\rangle}{2}.
```

Its charge probabilities are $`1/4,1/2,1/4`$, with mean $-1$ and variance $`1/2`$. It is a coherent pure superposition, so $`F_R=2=4DV_A`$. A scalar charge shift can make all reference charges nonnegative without changing the argument.

The six-dimensional space $BR$ splits into sectors of total charge $`-n`$, for $`n=0,1,2,3`$. Their available basis vectors are

```math
|u_{0,n}\rangle=|0\rangle_B|-n\rangle_R
\quad(0\leq n\leq2),\qquad
|u_{1,n}\rangle=|1\rangle_B|1-n\rangle_R
\quad(1\leq n\leq3).
```

For $`j=0,1,2`$, put $`\phi_j=2\pi j/3`$ and define the effects

```math
M_{n,j}=\frac13|v_{n,j}\rangle\langle v_{n,j}|,
\qquad
|v_{n,j}\rangle=|u_{0,n}\rangle+e^{-i\phi_j}|u_{1,n}\rangle,
```

omitting whichever basis vector is absent at an endpoint. Every effect lies in a single charge sector. Since $`\sum_je^{i\phi_j}=0`$, summing the three effects gives the identity on that sector. The sector dimensions are $`1,2,2,1`$, covering all of $BR$. This compressed example needs no complementary effect.

Contraction with the input produces

```math
p(n,j)=\frac{{3\choose n}}{24},\qquad
|\psi_{n,j}\rangle
=\sqrt{\frac{3-n}{3}}|0\rangle
+e^{i\phi_j}\sqrt{\frac n3}|1\rangle.
```

All twelve labels are retained:

| Count $n$ | Total probability of the count | Conditional state, up to global phase | Probability of each phase label |
| --- | --- | --- | --- |
| 0 | $`1/8`$ | $`\lvert0\rangle`$ | $`1/24`$ |
| 1 | $`3/8`$ | $`\sqrt{2/3}\lvert0\rangle+e^{i\phi_j}\sqrt{1/3}\lvert1\rangle`$ | $`1/8`$ |
| 2 | $`3/8`$ | $`\sqrt{1/3}\lvert0\rangle+e^{i\phi_j}\sqrt{2/3}\lvert1\rangle`$ | $`1/8`$ |
| 3 | $`1/8`$ | $`\lvert1\rangle`$ | $`1/24`$ |

The three labels at each pole describe the same ray. Merging only those duplicates gives eight distinct states, each of probability $`1/8`$. No event has been discarded.

The binomial count has $`\mathbb E[n/3]=1/2`$ and $`\mathbb E[(n/3)^2]=1/3`$, while $`\mathbb E[(n/3)(1-n/3)]=1/6`$. Combining these values with the phase average gives, in the basis $`00,01,10,11`$,

```math
M_2=\frac16
\begin{pmatrix}
2&0&0&0\\
0&1&1&0\\
0&1&1&0\\
0&0&0&2
\end{pmatrix}
=\frac{I+S}{6}.
```

This verifies the full design moment. The conditional charge-mean variance is $`v=1/12`$, and the average conditional QFI is $`4(1/4-1/12)=2/3`$. The apparatus cost is two. The example therefore displays the distinction between coherence in the output states and the reference needed to realize their complete ensemble.

## Accuracy and the role of purity

M22–M24 ask which parts of that cost survive a changed target. The additive error compares moment operators:

```math
\delta_K=\frac12\|M_K-M_{\mathrm H}\|_1
=\frac{D-1}{D}\left|\frac1K-\frac1{D+1}\right|.
```

This is not a channel-implementation error. Choosing $`K=\min\{D+1,\lceil1/\delta\rceil\}`$ reaches any fixed positive tolerance with $`F_R<4V_A/\delta`$ when $`V_A>0`$. The additional factor $D$ in the exact cost is absent from this achievable bound. For the qubit, $`K=2`$ costs one and has additive error $`1/12`$; $`K=3`$ costs two and is exact.

Even the multiplicative operator condition

```math
(1-\eta)M_{\mathrm H}\preceq M_2
\preceq(1+\eta)M_{\mathrm H}
```

does not generally retain the exact dimension factor. The [balanced-charge construction](../science/accuracy.md#3-a-multiplicative-error-counterexample-with-two-balanced-charges) reaches fixed positive $\eta$ at reference cost independent of $D$, using pure states and a finite conserving measurement. Contracting an operator inequality with $`H_A\otimes H_A`$ cannot establish the desired relative charge-variance inequality because that witness has both positive and negative eigenvalues.

Purity is another separate issue. The exact Haar moment forces pure conditional states. Additive error only implies average impurity $`p_{\mathrm{imp}}:=1-\sum_xp_x\mathrm{Tr}\rho_x^2\leq2\delta`$. The valid mixed-output bound is

```math
v+\frac{(q_{\max}-q_{\min})^2}{2}p_{\mathrm{imp}}
\geq\frac{V_A^2}{V_A+F_R/4}.
```

The [purity proof](../science/accuracy.md#4-mixed-conditional-states-and-a-sharp-purity-correction) quantifies the charge-mean variance lost when a refined record is forgotten. A fixed impurity cannot be ignored when the exact target fluctuation is as small as $`V_A/(D+1)`$. By contrast, the multiplicative moment upper bound has zero antisymmetric support and already forces purity; its inexpensive counterexample does not exploit mixed outputs.

## Fisher isotropy and useful information

M11 and M25–M27 connect the moment target to measurement performance. Take $`D\geq2`$, use $`E_x=Dp_xP_x`$, where $`P_x=\rho_x^{\mathsf T}`$, and perturb the maximally mixed input along a traceless Hermitian matrix $H$:

```math
\sigma_\theta=\frac{e^{\theta H}}{\mathrm{Tr}e^{\theta H}},\qquad
\sigma_0=I/D,\qquad \dot\sigma_0=H/D.
```

The probabilities have $`r_x(0)=p_x`$ and $`r_x'(0)=p_x\mathrm{Tr}(HP_x)`$, giving classical Fisher information

```math
J(H)=\sum_xp_x[\mathrm{Tr}(HP_x)]^2.
```

For an exact design this equals $`J_{\mathrm H}(H)=\mathrm{Tr}(H^2)/[D(D+1)]`$ in every traceless direction. The corresponding operator frame is isotropic and spans all state perturbations. This is the established tight rank-one informationally complete measurement interpretation, derived with its normalization in [Measurement geometry](../science/measurement_geometry.md). It is a local statement at $`I/D`$.

Now require two-sided relative isotropy,

```math
(1-\varepsilon)J_{\mathrm H}(H)\leq J(H)
\leq(1+\varepsilon)J_{\mathrm H}(H)
\quad\text{for every traceless }H,\qquad 0\leq\varepsilon<1,
```

and require every nonzero effect to be exactly rank one. The charge direction has $`J(H_A^{\mathsf T})=v`$, so the upper Fisher bound and the reference inequality imply

```math
F_R\geq4V_A\left[\frac{D+1}{1+\varepsilon}-1\right].
```

For the finite-$K$ measurement, relative Fisher eigenvalues are $`(D+1)/K`$ on traceless diagonal directions and $`(D+1)(K-1)/(KD)`$ on zero-diagonal directions. Setting $`K=\lceil(D+1)/(1+\varepsilon)\rceil`$ satisfies the criterion with cost less than $`4V_A`$ above the lower bound when $`V_A>0`$. The gap is zero when $`V_A=0`$. The [full proof](../science/measurement_geometry.md#4-two-sided-relative-fisher-isotropy) specifies the remaining continuous-budget gap.

Two-sided isotropy asks that information be distributed nearly evenly, including an upper bound on excess charge information. For $`0<\varepsilon<1`$, a one-sided guarantee, $`J(H)\geq(1-\varepsilon)J_{\mathrm H}(H)`$, is cheaper: the same family achieves it with cost below $`4V_A/\varepsilon`$ for positive $`V_A`$. For the qubit at $`K=2`$, the relative eigenvalues are $`3/2`$ and $`3/4`$. Information in the diagonal direction is enhanced while both off-diagonal directions retain three quarters of the symmetric benchmark.

Additional information is not intrinsically harmful to tomography. The large reference cost concerns the specified symmetry of the information, rather than a general requirement for useful measurements. Approximate Fisher isotropy also does not force exact rank one: replacing each normalized design effect $P_x$ by $`(1-s)P_x+sI/D`$ multiplies every $J(H)$ by $`(1-s)^2`$ while making the effects mixed. This observation alone specifies no apparatus cost; it explains why the rank-one premise cannot be inferred from a small statistical error.

## Connecting the full story

M01–M13 assemble the objects and the operational question. M14–M21 connect the comparison generator to a necessary cost and then realize that cost with counts and phases. M22–M27 distinguish the accuracy and measurement criteria. M28–M30 integrate the physical meaning, attribution, and verification.

For an exact design, average output QFI is $`4DV_A/(D+1)`$, while reference QFI is $`4DV_A`$. For $`V_A>0`$, the factor $D+1$ compares output sensitivity with implementation cost. Direct control is a different resource problem: the [explicit direct-preparation protocol](../science/interpretation.md#2-direct-control-changes-the-task) starts with coherent input on $A$ of QFI $`4V_A`$ and prepares the desired ensemble by diagonal Kraus operators. Its cost is an upper bound for that changed task, not an asserted direct optimum.

For $m$ excitation qubits, $`D=2^m`$ and $`V_A=m/4`$, so the exact remote cost is $`m2^m`$. This is QFI in fixed charge units. It is not a count of physical qubits or an energy requirement. The reference can be represented by $`mD+1`$ distinct charge levels, as explained in the [physical interpretation](../science/interpretation.md#3-excitation-conserving-qubits).

The [related-work account](../references/RELATED_WORK.md) separates inherited QFI, steering, design, and measurement results from the attained operational optimum. The [verification guide](../verification/README.md) checks finite effects, charge-sector feasibility, probabilities, moments, and accuracy formulas. Those checks complement the general proofs in [Reference bound](../science/reference_bound.md), [Conserving construction](../science/conserving_construction.md), [Accuracy](../science/accuracy.md), and [Measurement geometry](../science/measurement_geometry.md).
