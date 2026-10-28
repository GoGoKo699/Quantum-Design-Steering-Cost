# Reference information and the exact design bound

An independent reference with quantum Fisher information $F_R$ can steer only a limited average charge sensitivity into an untouched system. In the [model](model.md) considered here, the precise bound is

$$
\boxed{
\sum_x p_x F_Q(\rho_x,Q_A)
\leq \frac{4V_A F_R}{4V_A+F_R}.
}
$$

It applies to mixed references and mixed conditional output states. For an exact state 2-design, it implies $F_R\geq 4D V_A$. The [finite conserving construction](conserving_construction.md) attains this value for every finite system charge spectrum, so the minimum is exactly $4D V_A$.

The proof uses established quantum Fisher information methods. Its connection to finite-reference metrology, conservation-limited measurements, and state designs is explained in [Related work](../references/RELATED_WORK.md). In particular, the charge-sector QFI loss analysis of [Šafránek, Ahmadi, and Fuentes](https://doi.org/10.1088/1367-2630/17/3/033012), in their section on commutative and noncommutative reference-frame noise, supplies a closely related route to the converse. The argument below uses an adjustable comparison generator to include mixed references directly.

## 1. Input, measurement, and QFI convention

Let $A$ and $B$ have dimension $D$, and choose an orthonormal eigenbasis of $Q_A$:

$$
Q_A=\sum_{i=1}^D q_i |i\rangle\langle i|,
\qquad
Q_B=-Q_A^{\mathsf T},
\qquad
|\Omega\rangle_{AB}
=\frac{1}{\sqrt D}\sum_{i=1}^D |i\rangle_A|i\rangle_B.
$$

Transposition refers to these paired bases. Thus $(Q_A+Q_B)|\Omega\rangle=0$. Adding a scalar multiple of the identity to either charge only changes this sharp total charge and has no effect on the results. Define

$$
\mu=\frac{\mathrm{Tr}Q_A}{D},
\qquad
H=Q_A-\mu I_A,
\qquad
V_A=\frac{\mathrm{Tr}H^2}{D}.
$$

The reference $R$ is any finite-dimensional system in a state $\rho_R$, initially independent of $AB$. It includes every additional source of initial asymmetry used by the apparatus. Its charge is $Q_R$, and its charged resource is

$$
F_R=F_Q(\rho_R,Q_R).
$$

Here $\rho_R$ is the full accessible apparatus state. A neutral classical flag that selects different reference preparations is included in $R$, with the charge acting trivially on that flag. Replacing this flagged state by the reduced reference state after forgetting the accessible flag would change the resource being charged.

The measurement acts on $BR$ alone. Its effects obey

$$
M_x\geq 0,
\qquad
\sum_x M_x=I_{BR},
\qquad
[M_x,T]=0,
\qquad
T=Q_B\otimes I_R+I_B\otimes Q_R.
$$

Each outcome label is neutral and fixed under the symmetry. All outcomes are retained. The reference may be consumed. The [construction](conserving_construction.md#6-a-conserving-unitary-and-neutral-pointer) realizes its invariant effects with an exactly conserving unitary and a finite neutral pointer.

The finite-outcome notation also covers classical randomization of a measurement by including its choice in the record. Because the primary model is finite-dimensional, there are no unbounded-generator or differentiability qualifications in the theorem. The $q_i$ may be arbitrary real numbers. A compact $U(1)$ description requires a common charge lattice for the system and apparatus after scalar shifts; general real spectra describe conservation under real-parameter time translations. The attaining reference shares the system lattice whenever one exists.

For the unitary family $\rho_\theta=e^{-i\theta Q}\rho e^{i\theta Q}$, we use symmetric logarithmic derivative QFI. If $\rho=\sum_a r_a |a\rangle\langle a|$, its value is

$$
F_Q(\rho,Q)
=2\sum_{a,b:\,r_a+r_b>0}
\frac{(r_a-r_b)^2}{r_a+r_b}
|\langle a|Q|b\rangle|^2.
$$

In particular, $F_Q(|\psi\rangle,Q)=4\mathrm{Var}_{\psi}(Q)$. The statistical interpretation of this QFI, and hence its monotonicity under a parameter-independent quantum channel, follows from the optimization over measurements in [Braunstein and Caves](https://doi.org/10.1103/PhysRevLett.72.3439).

The unnormalized conditional state of $A$ is

$$
\tau_x=
\mathrm{Tr}_{BR}\!\left[
(I_A\otimes M_x^{1/2})
(|\Omega\rangle\langle\Omega|\otimes\rho_R)
(I_A\otimes M_x^{1/2})
\right].
$$

Write $p_x=\mathrm{Tr}\tau_x$ and $\rho_x=\tau_x/p_x$ when $p_x>0$. These states depend only on the effects $M_x$, not on a choice of instrument on $BR$: operators acting solely on the traced subsystem can be cycled inside the partial trace. Completeness consequently gives the no-signalling identity

$$
\sum_x p_x\rho_x=\frac{I_A}{D}.
$$

## 2. A bound for arbitrary mixed outputs

**Theorem 1.** Every protocol in the model above satisfies

$$
\mathcal F_{\mathrm{out}}
:=\sum_x p_x F_Q(\rho_x,Q_A)
\leq \frac{4V_A F_R}{4V_A+F_R}.
$$

When $V_A=F_R=0$, the right-hand side is defined to be zero.

### Proof

Let $C$ be the neutral classical record. The map from an arbitrary input operator on $ABR$ to the retained record and system is the quantum channel

$$
\mathcal M(X)
=\sum_x |x\rangle\langle x|_C\otimes
\mathrm{Tr}_{BR}\!\left[
(I_A\otimes M_x^{1/2})X(I_A\otimes M_x^{1/2})
\right].
$$

For any real $\lambda$, introduce the comparison generator

$$
G_\lambda
=Q_A\otimes I_{BR}+\lambda I_A\otimes T.
$$

Invariance of each effect implies invariance of its positive square root. The $BR$ rotation generated by $T$ therefore disappears under the partial trace, while the $A$ rotation passes through the channel. For every $X$,

$$
\mathcal M\!\left(e^{-i\theta G_\lambda}Xe^{i\theta G_\lambda}\right)
=(I_C\otimes e^{-i\theta Q_A})\mathcal M(X)
(I_C\otimes e^{i\theta Q_A}).
$$

The parameter is a comparison used in the proof. The steering protocol itself still acts only on $BR$.

Apply the channel to the encoded input family with $X=|\Omega\rangle\langle\Omega|\otimes\rho_R$. For every $\lambda$, the output is the same family

$$
\Omega_\theta
=\sum_x p_x|x\rangle\langle x|_C\otimes
e^{-i\theta Q_A}\rho_xe^{i\theta Q_A}.
$$

The probabilities $p_x$ are independent of $\theta$. The SLD of this state can be chosen block diagonal in $x$, with the conditional SLD in each nonzero-probability block. Thus there is no classical Fisher term from the record, and

$$
F_Q(\Omega_\theta)=\sum_x p_x F_Q(\rho_x,Q_A)
=\mathcal F_{\mathrm{out}}.
$$

On the input, the generator separates between $AB$ and $R$:

$$
G_\lambda=(Q_A+\lambda Q_B)\otimes I_R
+I_{AB}\otimes\lambda Q_R.
$$

QFI is additive for product state families. One can see this directly by taking the sum of the two SLDs on the two tensor factors; the cross term vanishes because each SLD has zero expectation. The sharp total charge of $AB$ gives

$$
(Q_A+\lambda Q_B)|\Omega\rangle
=(1-\lambda)Q_A|\Omega\rangle,
$$

so the input QFI is exactly

$$
F_Q(|\Omega\rangle\langle\Omega|\otimes\rho_R,G_\lambda)
=4(1-\lambda)^2V_A+\lambda^2F_R.
$$

Data processing holds for every $\lambda$. If $4V_A+F_R>0$, minimizing the quadratic at

$$
\lambda_* =\frac{4V_A}{4V_A+F_R}
$$

gives

$$
\mathcal F_{\mathrm{out}}
\leq\min_{\lambda\in\mathbb R}
\left[4(1-\lambda)^2V_A+\lambda^2F_R\right]
=\frac{4V_A F_R}{4V_A+F_R}.
$$

If both quantities vanish, the same quadratic is zero for every $\lambda$. This proves the remaining case. $\square$

The bound is stronger than the separate inequalities $\mathcal F_{\mathrm{out}}\leq F_R$ and $\mathcal F_{\mathrm{out}}\leq 4V_A$. Both the independent reference and the correlations in $AB$ limit the output. At $F_R=0$, every retained conditional state has zero QFI and hence commutes with $Q_A$. As $F_R$ increases, the upper bound approaches $4V_A$, but a finite reference cannot attain that ceiling when $V_A>0$.

## 3. Pure ensembles and their conditional charge means

For a pure conditional ensemble, define

$$
m_x=\mathrm{Tr}(Q_A\rho_x),
\qquad
v=\sum_x p_x(m_x-\mu)^2.
$$

No signalling fixes $\sum_xp_xm_x=\mu$. It also fixes the average second charge moment. Therefore

$$
\sum_x p_x\mathrm{Var}_{\rho_x}(Q_A)
=\frac{\mathrm{Tr}Q_A^2}{D}-\sum_xp_xm_x^2
=V_A-v.
$$

Purity converts each conditional variance into one quarter of its QFI. Theorem 1 consequently yields the following equivalent form.

**Corollary 2.** If every nonzero-probability output is pure and $V_A>0$, then

$$
\boxed{
v\geq\frac{V_A^2}{V_A+F_R/4}.
}
$$

In particular, a finite reference cannot generate a pure ensemble whose charge expectation is identical in every outcome when $V_A>0$. This conclusion concerns the complete ensemble. Discarding outcomes would change both the no-signalling identity and the task.

There is also a charge-sector interpretation of this inequality. For a pure reference, refine the outcome by the value $t$ of $T$. If the original conditional state is pure, every nonzero refined conditional state must equal it, since a pure state has no nontrivial decomposition into distinct states. The resulting classical variables obey

$$
\mathrm{Cov}(m_x,T)=-V_A,
\qquad
\mathrm{Var}(T)=V_A+\mathrm{Var}_{\rho_R}(Q_R).
$$

The first identity follows from the sharp total charge of $AB$ and the independence of $R$; refining a commuting measurement preserves the joint expectation of $Q_A$ and $T$. Cauchy–Schwarz gives Corollary 2 because a pure reference has $F_R=4\mathrm{Var}(Q_R)$. This is the same conditional-charge information that appears in the finite-reference QFI loss formula of [Šafránek, Ahmadi, and Fuentes](https://arxiv.org/abs/1404.6421). Theorem 1 avoids a decomposition of a mixed reference and applies without assuming pure outputs.

## 4. Exact second moments force purity

Let $\mathsf S$ exchange the two copies of $A$, and let

$$
M_2=\sum_x p_x\rho_x\otimes\rho_x,
\qquad
M_{\mathrm H}=\frac{I_{A\otimes A}+\mathsf S}{D(D+1)}.
$$

The condition $M_2=M_{\mathrm H}$ is the second-moment condition for a weighted exact complex projective 2-design. Even if the $\rho_x$ were initially allowed to be mixed, this equality would force them to be pure:

$$
\sum_x p_x\mathrm{Tr}\rho_x^2
=\mathrm{Tr}(\mathsf S M_2)
=\mathrm{Tr}(\mathsf S M_{\mathrm H})
=1.
$$

Each purity is at most one. Consequently every term of nonzero weight has purity one. Thus the exact second-moment target already includes the purity needed in Corollary 2.

Since $\mathrm{Tr}H=0$ and $\mathrm{Tr}H^2=DV_A$, the same target fixes the conditional-mean variance:

$$
\begin{aligned}
v
&=\mathrm{Tr}\!\left[(H\otimes H)M_{\mathrm H}\right]\\
&=\frac{(\mathrm{Tr}H)^2+\mathrm{Tr}H^2}{D(D+1)}
=\frac{V_A}{D+1}.
\end{aligned}
$$

The identity $\mathrm{Tr}[(X\otimes Y)\mathsf S]=\mathrm{Tr}(XY)$ gives the second line. Inserting this value of $v$ into Corollary 2 proves the exact design converse when $V_A>0$. For $V_A=0$, the same conclusion follows from nonnegativity of QFI.

**Theorem 3.** Every allowed protocol with $M_2=M_{\mathrm H}$ satisfies

$$
F_R\geq4D V_A.
$$

Equivalently, an exact design has average output QFI $4D V_A/(D+1)$, and Theorem 1 gives the same bound after rearrangement.

## 5. The attained optimum and its scope

Let the minimum range over all finite reference Hilbert spaces, charges, mixed initial states, and invariant finite-outcome POVMs satisfying the model, with the target being some weighted exact complex projective 2-design. The [construction](conserving_construction.md#5-exact-design-and-equality-in-the-reference-bound) uses a pure finite reference with $F_R=4D V_A$. Together with Theorem 3, it establishes

$$
\boxed{
\min_{\text{allowed exact design protocols}}F_Q(\rho_R,Q_R)
=4D V_A.
}
$$

If $V_A=0$, then $Q_A=\mu I_A$ and $Q_B$ is scalar. A one-dimensional reference suffices: the design POVM on $B$ is itself invariant. The minimum is again the displayed value, zero. Degeneracies with $V_A>0$ require no change to the argument because the paired eigenbasis, maximally mixed marginal, and charge identities remain valid.

The result also has a measurement interpretation. The effective POVM on $B$ is

$$
E_x=\mathrm{Tr}_R\!\left[
(I_B\otimes\rho_R^{1/2})M_x(I_B\otimes\rho_R^{1/2})
\right],
\qquad
\tau_x=\frac{E_x^{\mathsf T}}{D}.
$$

For pure outputs, $E_x=Dp_x\rho_x^{\mathsf T}$ is rank one. The established equivalence between weighted state 2-designs and tight rank-one informationally complete POVMs, developed by [Scott](https://doi.org/10.1088/0305-4470/39/43/009), identifies the same minimum as the reference cost of implementing some POVM in that class. It does not assert that a particular prescribed SIC, MUB measurement, or Haar ensemble has a realization at this cost.

Exactness is material. Fixed additive second-moment accuracy, conventional multiplicative moment accuracy, and relative Fisher isotropy impose different conditions and have different cost consequences. The [accuracy analysis](accuracy.md) separates these targets and treats mixed-output impurity. The exact theorem charges initial reference QFI; gate count, reference dimension, mean energy, locality, and a reference-return condition are outside this optimization.
