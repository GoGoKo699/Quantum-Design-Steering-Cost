# Measurement geometry and Fisher isotropy

The optimized cost of an exact state 2-design is also the optimized cost of a tight rank-one informationally complete measurement in the same conserving apparatus model. The equivalence between these measurement and design conditions is established work: Scott [1] developed tight informationally complete measurements, and Zhu and Hayashi [2, Proposition 1] identify their Fisher symmetry at the maximally mixed state. The resource statement here comes from combining that geometry with the conserving reference bound and its finite construction.

For exactly rank-one effects, two-sided relative Fisher isotropy retains a reference cost of order $DV_A$, with a construction at most $4V_A$ above the lower bound. The gap is strictly smaller when $V_A>0$. A one-sided guarantee that every Fisher direction is at least as informative as a fixed fraction of the symmetric benchmark is already possible at cost of order $V_A/\varepsilon$. These criteria therefore have different operational consequences.

Throughout this page $D\geq2$. The one-dimensional case has a unique state and zero charge variance, and is covered by the trivial case in the [model](model.md).

## 1. From remote preparation to a POVM

Use the maximally entangled state $|\Omega\rangle=D^{-1/2}\sum_i|i\rangle_A|i\rangle_B$, with $Q_B=-Q_A^{\mathsf T}$. An independent reference $R$ supplies a state $\rho_R$, and every measurement effect on $BR$ commutes with $Q_B+Q_R$. The conditional ensemble on untouched $A$ has mean $I/D$.

Let $E_x$ be the effective POVM on $B$. It can be written without any commutation assumption on $\rho_R$ as

$$
E_x=\operatorname{Tr}_R\!\left[
(I_B\otimes\rho_R^{1/2})M_x(I_B\otimes\rho_R^{1/2})\right].
$$

It is positive and sums to $I_B$. The maximally entangled identity gives

$$
p_x=\frac{\operatorname{Tr}E_x}{D},\qquad
\rho_x=\frac{E_x^{\mathsf T}}{\operatorname{Tr}E_x},\qquad
E_x=Dp_x\rho_x^{\mathsf T}.
\tag{1}
$$

All transposes refer to the chosen charge basis. Zero effects are omitted. Define $P_x=\rho_x^{\mathsf T}$; in the pure-output case these are rank-one projectors. Thus pure conditional states correspond exactly to rank-one effective POVM elements. The physical apparatus realizes $E_x$, while the steering representation encodes its normalized effects as states.

Write

$$
\mu=\frac{\operatorname{Tr}Q_A}{D},\qquad
V_A=\frac1D\operatorname{Tr}(Q_A-\mu I)^2,\qquad
F_R=F_Q(\rho_R,Q_R).
$$

The [reference bound for pure outputs](reference_bound.md#3-pure-ensembles-and-their-conditional-charge-means) is

$$
v:=\operatorname{Var}_x\operatorname{Tr}(Q_A\rho_x)
\geq\frac{V_A^2}{V_A+F_R/4}.
\tag{2}
$$

Mixed reference states are allowed. Exact rank one concerns the effective measurement, not the reference. The [purity correction](accuracy.md#4-mixed-conditional-states-and-a-sharp-purity-correction) gives the corresponding bound without a pure-output promise.

## 2. Tight rank-one measurements, designs, and Fisher symmetry

### 2.1 The local statistical model

For any traceless Hermitian matrix $H$, consider the state family on $B$

$$
\sigma_\theta=\frac{e^{\theta H}}{\operatorname{Tr}e^{\theta H}}.
$$

At $\theta=0$, the state is $I/D$ and its derivative is $H/D$. The outcome probability $r_x(\theta)=\operatorname{Tr}(E_x\sigma_\theta)$ obeys

$$
r_x(0)=p_x,\qquad
r_x'(0)=p_x\operatorname{Tr}(HP_x).
$$

Its classical Fisher information is therefore

$$
J(H)=\sum_x\frac{r_x'(0)^2}{r_x(0)}
=\sum_xp_x[\operatorname{Tr}(HP_x)]^2.
\tag{3}
$$

The quantum Fisher information of this model at zero is $\operatorname{Tr}(H^2)/D$, because the SLD is $H$. The symmetric single-copy benchmark is

$$
J_{\mathrm H}(H)=\frac{\operatorname{Tr}(H^2)}{D(D+1)}.
\tag{4}
$$

It is a fraction $1/(D+1)$ of the quantum Fisher information in every direction. The statements below concern this local full-state model at $I/D$, rather than uniform Fisher symmetry at all mixed states.

### 2.2 Frame operator and the known equivalence

On the real vector space of traceless Hermitian matrices, with Hilbert–Schmidt inner product, define

$$
\mathcal C(H)=\sum_xp_x\operatorname{Tr}(HP_x)(P_x-I/D).
\tag{5}
$$

Then $J(H)=\operatorname{Tr}[H\mathcal C(H)]$. A tight rank-one informationally complete POVM has $\mathcal C=c\,\operatorname{id}$ on this space, for a positive constant $c$.

For completeness, the equivalence with an exact weighted state 2-design follows directly. If

$$
\sum_xp_xP_x\otimes P_x=\frac{I+S}{D(D+1)},
\tag{6}
$$

then contracting with $H\otimes H$ gives $J(H)=J_{\mathrm H}(H)$. Conversely, suppose equality holds in every traceless Hermitian direction. Polarization determines the bilinear form on pairs of traceless Hermitian matrices. The first moment $\sum_xp_xP_x=I/D$ fixes the identity direction and the cross terms. Hence, for all Hermitian $X,Y$,

$$
\sum_xp_x\operatorname{Tr}(XP_x)\operatorname{Tr}(YP_x)
=\frac{\operatorname{Tr}(XY)+\operatorname{Tr}X\operatorname{Tr}Y}{D(D+1)}.
\tag{7}
$$

Products of Hermitian operator bases span the Hermitian operators on two copies, so (7) implies (6). Simultaneous transpose leaves $I+S$ invariant, which makes the condition equivalent for $P_x$ and $\rho_x$.

It remains to check the value of the tight-frame constant. Let $\{H_a\}_{a=1}^{D^2-1}$ be an orthonormal traceless Hermitian basis, with $\operatorname{Tr}(H_aH_b)=\delta_{ab}$. Rank one gives

$$
\begin{aligned}
\sum_{a=1}^{D^2-1}J(H_a)
&=\sum_xp_x\left[\operatorname{Tr}(P_x^2)-\frac1D\right]\\
&=1-\frac1D.
\end{aligned}
\tag{8}
$$

If $\mathcal C=c\,\operatorname{id}$, its trace is $(D^2-1)c$, so $c=1/[D(D+1)]$. This constant is positive, which also implies informational completeness on the traceless space; the normalization supplies the identity direction. Thus the following are equivalent for a rank-one POVM:

1. Its normalized effects form a weighted complex projective 2-design.
2. It is tight and informationally complete.
3. Its Fisher information at the maximally mixed state equals (4) in every traceless direction.

This equivalence and its statistical interpretation belong to the established tight-measurement and Fisher-symmetry literature [1, 2]. Equations (3)–(8) fix the normalization used here.

### 2.3 Exact reference cost

Choose the charge direction

$$
H_Q=(Q_A-\mu I)^{\mathsf T}.
$$

It is traceless, and (1) gives

$$
J(H_Q)=v,\qquad
J_{\mathrm H}(H_Q)=\frac{V_A}{D+1}.
\tag{9}
$$

An exact tight rank-one measurement therefore obeys $v=V_A/(D+1)$. Substituting in (2) yields

$$
F_R\geq4DV_A.
\tag{10}
$$

The [conserving multinomial construction](conserving_construction.md) at $K=D+1$ reaches equality. Thus $4DV_A$ is the exact optimized cost over the allowed apparatuses and over the choice of a weighted tight rank-one informationally complete POVM. This does not assert that every prescribed SIC, mutually unbiased basis measurement, or other prescribed design has an implementation at that cost. Apparatus size and measurement complexity are also outside the optimized resource.

## 3. Fisher spectrum of the finite-$K$ construction

Use the multinomial phase ensemble from [Accuracy, Section 2](accuracy.md#2-exact-moments-of-the-conserving-multinomial-family), with reference cost $4(K-1)V_A$. Decompose a traceless Hermitian matrix in the charge eigenbasis as

$$
H=H_{\mathrm{diag}}+H_{\mathrm{off}},
$$

where $H_{\mathrm{diag}}$ is diagonal and traceless, while $H_{\mathrm{off}}$ has zero diagonal. This is an orthogonal decomposition of real Hilbert spaces, of dimensions $D-1$ and $D(D-1)$.

For the diagonal part, let $h_i=H_{ii}$, with $\sum_i h_i=0$. Using the multinomial second moments,

$$
\mathbb E\left(\sum_i h_i\frac{N_i}{K}\right)^2
=(\alpha_K-\beta_K)\sum_i h_i^2
=\frac{\operatorname{Tr}(H_{\mathrm{diag}}^2)}{KD}.
$$

For the off-diagonal part, phase averaging pairs $H_{ij}$ with $H_{ji}$. It removes its cross terms with the diagonal part, giving

$$
\mathbb E\left[\operatorname{Tr}(H_{\mathrm{off}}P_x)\right]^2
=\beta_K\sum_{i\ne j}|H_{ij}|^2
=\frac{K-1}{KD^2}\operatorname{Tr}(H_{\mathrm{off}}^2).
$$

Therefore the full Fisher quadratic form is

$$
\boxed{
J_K(H)=\frac{\operatorname{Tr}(H_{\mathrm{diag}}^2)}{KD}
 +\frac{K-1}{KD^2}\operatorname{Tr}(H_{\mathrm{off}}^2).
}
\tag{11}
$$

Relative to the benchmark in (4), its eigenvalues are

| Directions | Multiplicity | Relative Fisher eigenvalue |
| --- | ---: | --- |
| Traceless diagonal | $D-1$ | $a_K=(D+1)/K$ |
| Zero-diagonal Hermitian | $D(D-1)$ | $b_K=(D+1)(K-1)/(KD)$ |

They obey

$$
b_K=1-\frac{a_K-1}{D}.
\tag{12}
$$

The measurement is informationally complete for every $K\geq2$, because both frame eigenvalues are positive. At $K=1$, only the diagonal directions are measured. At $K=D+1$, both eigenvalues equal one. These properties hold even if $Q_A$ has degeneracies; the diagonal/off-diagonal splitting refers to the selected basis, not just to distinct charge sectors.

Equation (12) shows how this family redistributes a fixed total amount of Fisher information. When $2\leq K<D+1$, diagonal directions are enhanced, while the many off-diagonal directions are each reduced. The total frame trace remains the rank-one value (8).

## 4. Two-sided relative Fisher isotropy

### 4.1 Criterion and converse

Fix $0\leq\varepsilon<1$ and require

$$
(1-\varepsilon)J_{\mathrm H}(H)
\leq J(H)\leq
(1+\varepsilon)J_{\mathrm H}(H)
\quad\text{for every traceless Hermitian }H.
\tag{13}
$$

Assume that every nonzero effective effect is exactly rank one. The upper bound in the charge direction (9) implies

$$
v\leq\frac{(1+\varepsilon)V_A}{D+1}.
$$

Combining with the pure-output reference bound (2) and rearranging gives

$$
\boxed{
F_R\geq L_\varepsilon
:=4V_A\left[\frac{D+1}{1+\varepsilon}-1\right].
}
\tag{14}
$$

For $D\geq2$ and $\varepsilon<1$, the bracket is positive. If $V_A=0$, the result is the trivial zero lower bound. The reference can be mixed; the rank-one restriction applies only to the effective POVM.

The converse uses the upper Fisher inequality in (13). It requires suppression of excess information in the charge direction as part of isotropy. A lower bound on useful information alone does not impose this condition.

### 4.2 Construction within less than one reference factor

Choose

$$
K=\left\lceil\frac{D+1}{1+\varepsilon}\right\rceil.
\tag{15}
$$

This integer lies between $2$ and $D+1$. Equations (11) and (12) then give

$$
1\leq a_K\leq1+\varepsilon,
\qquad
1-\frac{\varepsilon}{D}\leq b_K\leq1.
$$

Thus the construction satisfies the full two-sided criterion (13). Its cost is

$$
F_R^{\mathrm{constr}}=4(K-1)V_A,
\qquad
0\leq F_R^{\mathrm{constr}}-L_\varepsilon<4V_A
\quad(V_A>0).
\tag{16}
$$

The gap is zero whenever $(D+1)/(1+\varepsilon)$ is an integer. Otherwise it is the cost of less than one of the $D$-level reference factors. For $V_A=0$, both quantities in (16) vanish.

Equations (14)–(16) determine the leading dimension dependence with an explicit finite construction. They do not determine the exact continuous-budget optimum between the integer construction points. At $\varepsilon=0$, they coincide with the exact cost (10).

## 5. A one-sided information guarantee is much cheaper

Suppose the requirement is only

$$
J(H)\geq(1-\varepsilon)J_{\mathrm H}(H)
\quad\text{for every traceless Hermitian }H,
\qquad 0<\varepsilon<1.
\tag{17}
$$

The same finite-$K$ family satisfies this criterion with

$$
K=\left\lceil\frac{D+1}{1+D\varepsilon}\right\rceil.
\tag{18}
$$

Here $2\leq K\leq D+1$, so $a_K\geq1$. The choice of $K$ gives

$$
b_K=\frac{D+1}{D}\left(1-\frac1K\right)\geq1-\varepsilon.
$$

Every direction therefore meets (17), at cost

$$
F_R=4(K-1)V_A
<4V_A\frac{D+1}{1+D\varepsilon}
<\frac{4V_A}{\varepsilon}
\quad(V_A>0).
\tag{19}
$$

The diagonal Fisher information can be much larger than the symmetric benchmark. That excess is not intrinsically a statistical defect. For example, the matrix inequality corresponding to (17) bounds the inverse Fisher matrix by $1/(1-\varepsilon)$ times the inverse symmetric benchmark whenever both are positive. This is a local information statement; it does not by itself establish a finite-sample estimator guarantee.

The large cost in Section 4 consequently concerns two-sided isotropy. It is not a lower bound for a measurement that performs competitively in every local direction, and it is not a general lower bound for useful tomography.

## 6. Why exact rank one matters

For arbitrary positive effects, the normalized operators $P_x=E_x/\operatorname{Tr}E_x$ may be mixed. The statistical formula (3) remains valid, but the frame trace becomes

$$
\sum_{a=1}^{D^2-1}J(H_a)
=\sum_xp_x\operatorname{Tr}(P_x^2)-\frac1D
\leq1-\frac1D.
\tag{20}
$$

Equality holds if and only if every positive-weight normalized effect is pure. This calculation explains the maximality in the exact Fisher-symmetry benchmark. An arbitrary POVM with $J(H)=J_{\mathrm H}(H)$ for every traceless $H$ necessarily saturates (20), so exact Fisher symmetry itself forces rank one. For this exact condition, a separate rank-one assumption is unnecessary.

Approximate Fisher isotropy does not force exact rank one. To see this at the level of measurement geometry, start with a design POVM $E_x=Dp_xP_x$ and replace its normalized effects by

$$
P_x^{(s)}=(1-s)P_x+sI/D,\qquad 0<s<1.
$$

The resulting operators $E_x^{(s)}=Dp_xP_x^{(s)}$ still form a POVM. Every normalized effect is mixed, while

$$
J^{(s)}(H)=(1-s)^2J_{\mathrm H}(H).
\tag{21}
$$

For arbitrarily small $s>0$, this is arbitrarily close to the benchmark under the two-sided criterion. This example makes no assertion about the optimal conserving apparatus cost of the depolarized measurement. It shows only that the approximate statistical condition does not supply the exact rank-one premise needed in (14).

When purity is imperfect, the valid reference constraint is the [mixed-output correction](accuracy.md#4-mixed-conditional-states-and-a-sharp-purity-correction), involving both the charge-mean variance and average conditional impurity. Fixed nonzero impurity cannot simply be discarded from a dimension-dependent claim. Likewise, the usual multiplicative state-moment criterion has the [finite conserving counterexample](accuracy.md#3-a-multiplicative-error-counterexample-with-two-balanced-charges); its operator ordering is distinct from (13).

## References

1. A. J. Scott, *Tight informationally complete quantum measurements*, Journal of Physics A: Mathematical and General **39**, 13507–13530 (2006). [Published article](https://doi.org/10.1088/0305-4470/39/43/009); [arXiv record](https://arxiv.org/abs/quant-ph/0604049). The rank-one tight-IC/weighted-2-design equivalence is established here.
2. H. Zhu and M. Hayashi, *Universally Fisher-Symmetric Informationally Complete Measurements*, Physical Review Letters **120**, 030404 (2018). [Published article](https://doi.org/10.1103/PhysRevLett.120.030404); [arXiv text](https://arxiv.org/html/1709.06112v2). Proposition 1 and Supplementary Section V identify Fisher symmetry at the completely mixed state with the 2-design condition and explain the relation to tight measurements.
