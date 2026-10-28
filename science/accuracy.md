# Accuracy, moment distance, and imperfect purity

The exact reference cost does not extend uniformly to approximate state designs. The conserving multinomial construction reaches any fixed positive additive second-moment error with reference quantum Fisher information of order $V_A/\delta$, independent of the Hilbert-space dimension. For a balanced two-charge spectrum, a charge-preserving block randomization also reaches the usual multiplicative second-moment criterion at a cost independent of dimension. A different criterion, two-sided Fisher isotropy with exactly rank-one effects, retains the dimension factor; its statement and proof are in [Measurement geometry](measurement_geometry.md).

This page derives the moment formulas, gives the conserving multiplicative counterexample, and proves a correction for mixed conditional states. The resource throughout is reference quantum Fisher information. Apparatus dimension, number of outcomes, gate complexity, and classical randomness are not included in this cost.

## 1. Setting and conventions

Let $A$ and $B$ have dimension $D\geq 2$, with

$$
Q_A=\sum_{i=1}^D q_i|i\rangle\langle i|,
\qquad Q_B=-Q_A^{\mathsf T},
\qquad
|\Omega\rangle_{AB}=\frac{1}{\sqrt D}\sum_{i=1}^D|i\rangle_A|i\rangle_B.
$$

The apparatus $R$ is initially independent of $AB$. Each measurement effect $M_x$ on $BR$ satisfies

$$
[M_x,T]=0,\qquad T=Q_B+Q_R.
$$

The record is neutral, $A$ is not acted on, and all outcomes are retained. Any asymmetric helper belongs in $R$. Its initial state may be mixed, and the reference may be consumed. Finite real charge spectra are allowed. A compact $U(1)$ interpretation requires a common system-apparatus charge lattice after scalar shifts; the commutation formulation itself does not require one.

Write

$$
\mu=\frac{\mathrm{Tr}Q_A}{D},\qquad
V_A=\frac{1}{D}\mathrm{Tr}(Q_A-\mu I)^2,
\qquad
F_R=F_Q(\rho_R,Q_R).
$$

We use SLD quantum Fisher information, normalized so that $F_Q(|r\rangle,Q_R)=4\mathrm{Var}_r(Q_R)$. The conditional ensemble obeys $\sum_xp_x\rho_x=I/D$. For pure conditional states, the [reference bound](reference_bound.md#3-pure-ensembles-and-their-conditional-charge-means) is

$$
v:=\mathrm{Var}_x\!\left[\mathrm{Tr}(Q_A\rho_x)\right]
\geq \frac{V_A^2}{V_A+F_R/4}.
\tag{1}
$$

The mixed-output extension proved in Section 4 includes (1). When $V_A=0$, the charge on $A$ is constant and every resource lower bound here is zero; fractions with a zero numerator and denominator are understood through this trivial case.

Let $S$ swap the two copies of $A$. For any ensemble, define

$$
M_2=\sum_xp_x\rho_x\otimes\rho_x,
\qquad
M_{\mathrm H}=\frac{I+S}{D(D+1)}.
$$

For pure states, $M_2=M_{\mathrm H}$ is the weighted complex projective 2-design condition. We distinguish two approximate conditions:

$$
\delta(M_2)=\frac12\|M_2-M_{\mathrm H}\|_1
\tag{2}
$$

and

$$
(1-\eta)M_{\mathrm H}\preceq M_2\preceq(1+\eta)M_{\mathrm H}.
\tag{3}
$$

The second is an operator inequality on two copies. It is not the same condition as a relative bound on the classical Fisher-information quadratic form.

## 2. Exact moments of the conserving multinomial family

### 2.1 Ensemble and reference cost

For an integer $K\geq1$, let

$$
N=(N_1,\ldots,N_D)\sim\mathrm{Multinomial}
\left(K;\frac1D,\ldots,\frac1D\right).
$$

Independently choose each $e^{i\phi_i}$ uniformly from the third roots of unity, and prepare

$$
|\psi_{N,\phi}\rangle
=\sum_{i=1}^D\sqrt{\frac{N_i}{K}}e^{i\phi_i}|i\rangle.
\tag{4}
$$

One overall phase can be fixed. This is a finite weighted ensemble.

Its [conserving implementation](conserving_construction.md) uses $K-1$ reference factors, each in $D^{-1/2}\sum_i|i\rangle$ with charge $-q_i$ on $|i\rangle$. Therefore

$$
F_R=4(K-1)V_A.
\tag{5}
$$

The occupation count of $B$ together with the $K-1$ factors can be measured without violating charge conservation. For a fixed count vector $N$, let $|u_{i,N}\rangle$ be $|i\rangle_B$ tensored with the normalized equal superposition of reference strings with counts $N-e_i$, for each $i$ with $N_i>0$. These orthonormal vectors all have total external charge $-\sum_jq_jN_j$. On their span, the finite phase POVM with vectors

$$
|v_{N,\phi}\rangle
=\sum_{i:N_i>0}e^{-i\phi_i}|u_{i,N}\rangle
$$

and effects $|v_{N,\phi}\rangle\langle v_{N,\phi}|$ weighted by the uniform phase probabilities is complete. Phase averaging removes all off-diagonal terms. Complete the POVM on the unused orthogonal subspace with effects that have zero probability on the supplied input.

There are

$$
\frac{(K-1)!}{(N_i-1)!\prod_{j\ne i}N_j!}
=\frac{N_i}{K}\frac{K!}{\prod_jN_j!}
$$

reference strings in the component labeled by $i$. Contracting the phase bra with the initial state consequently produces (4), with count probability $K!/(D^K\prod_jN_j!)$. Every effect acts within a total-charge sector. This argument also covers repeated or incommensurate charges: labels remain orthogonal, and count sectors with the same charge can be measured separately.

### 2.2 Phase and occupation averages

The phase average of a first moment removes $|i\rangle\langle j|$ for $i\ne j$. Since $\mathbb E N_i/K=1/D$,

$$
\mathbb E\,|\psi_{N,\phi}\rangle\langle\psi_{N,\phi}|=I/D.
$$

For a second moment, each phase exponent is one of $-2,-1,0,1,2$. Independent third-root phases retain precisely the terms for which the two ket indices and the two bra indices have the same multiset. The relevant multinomial averages are

$$
\alpha_K:=\mathbb E\left(\frac{N_i}{K}\right)^2
=\frac{K+D-1}{KD^2},
\qquad
\beta_K:=\mathbb E\frac{N_iN_j}{K^2}
=\frac{K-1}{KD^2}\quad(i\ne j).
\tag{6}
$$

Define $\Pi_{\mathrm{diag}}=\sum_i|ii\rangle\langle ii|$. The diagonal terms in $I+S$ occur twice, so

$$
\begin{aligned}
M_K
&=\beta_K(I+S)+(\alpha_K-2\beta_K)\Pi_{\mathrm{diag}}\\
&=\frac{K-1}{KD^2}(I+S)
 +\frac{D+1-K}{KD^2}\Pi_{\mathrm{diag}}.
\end{aligned}
\tag{7}
$$

At $K=D+1$, the second term vanishes and $M_K=M_{\mathrm H}$. Together with (5), this gives the exact design cost $4DV_A$.

### 2.3 Half trace-norm error

Both moments vanish on the antisymmetric subspace. On the symmetric subspace, use the orthogonal decomposition into $\mathrm{span}\{|ii\rangle\}$ and $\mathrm{span}\{(|ij\rangle+|ji\rangle)/\sqrt2:i<j\}$. Put $c_K=1/K-1/(D+1)$. The spectrum of the difference is

| Subspace | Dimension | Eigenvalue of $M_K-M_{\mathrm H}$ |
| --- | ---: | --- |
| Diagonal | $D$ | $(D-1)c_K/D^2$ |
| Off-diagonal symmetric | $D(D-1)/2$ | $-2c_K/D^2$ |
| Antisymmetric | $D(D-1)/2$ | $0$ |

The positive and negative trace contributions have equal magnitude. Hence, for every integer $K\geq1$,

$$
\boxed{
\delta_K=\frac12\|M_K-M_{\mathrm H}\|_1
=\frac{D-1}{D}\left|\frac1K-\frac1{D+1}\right|.
}
\tag{8}
$$

The branch $1\leq K\leq D+1$ improves monotonically to zero error. Increasing $K$ beyond $D+1$ does not continue improving the moment. In the limit $K\to\infty$, the amplitudes become uniform and $\delta_K\to(D-1)/[D(D+1)]$.

The charge mean in (4) is $K^{-1}\sum_iq_iN_i$, a mean of $K$ independent uniform charge samples. Thus

$$
v_K=\frac{V_A}{K}.
\tag{9}
$$

Equations (5) and (9) saturate (1) at every integer $K$, not only at the design point.

For a fixed additive tolerance $0<\delta<1$, choose

$$
K=\min\!\left\{D+1,\left\lceil\frac1\delta\right\rceil\right\}.
$$

Then $\delta_K\leq\delta$ and, for $V_A>0$,

$$
F_R=4(K-1)V_A<\frac{4V_A}{\delta}.
\tag{10}
$$

For $V_A=0$, the same construction has zero reference cost. This is an achievable bound, not an optimal additive-error tradeoff. Low-resource approximate designs are already known in other preparation models, including the shallow-circuit construction of Lee, Hhan, Cho, and Kwon [1]. Here the relevant statement is the explicit conserving remote realization and its reference-QFI accounting.

## 3. A multiplicative-error counterexample with two balanced charges

The usual multiplicative moment condition (3) also permits a cost independent of $D$ for a fixed positive tolerance. The following construction is a counterexample to a universal dimension-dependent lower bound under that criterion. It uses a particular charge spectrum, not an arbitrary-spectrum assertion.

### 3.1 Charge-preserving block randomization

Take $D=2d$ and orthogonal rank-$d$ projectors $P_+$ and $P_-$. Fix the charge normalization

$$
Q_A=P_+-P_-,\qquad \mu=0,\qquad V_A=1.
\tag{11}
$$

Begin with the multinomial ensemble (4), at cost $F_R=4(K-1)$. For a sampled pure state, write

$$
m=\langle Q_A\rangle,\qquad
w_+=\frac{1+m}{2},\qquad w_-=\frac{1-m}{2}.
$$

Its charge statistics satisfy

$$
\mathbb E m=0,\qquad v:=\mathbb E m^2=\frac1K.
\tag{12}
$$

Independently randomize the state by $U=U_+\oplus U_-$, where the two blocks have independent Haar distributions on $U(d)$. This randomization is realized without an operation on $A$. Apply $U^{\mathsf T}$ on $B$ before the original measurement, using

$$
(I\otimes U^{\mathsf T})|\Omega\rangle=(U\otimes I)|\Omega\rangle.
$$

Since $[U,Q_A]=0$, also $[U^{\mathsf T},Q_B]=0$. Record the random choice and then the original outcome. Conjugating each original effect by this charge-commuting unitary preserves its commutation with $T$. A neutral classical control supplies no additional charge asymmetry, so the reference cost remains exactly $4(K-1)$.

The Haar notation does not require an infinite record or pointer. Consider the map $X\mapsto U^{\otimes2}X(U^\dagger)^{\otimes2}$ as an element of a finite-dimensional real vector space of linear maps. Its Haar average lies in the convex hull of the compact set of these maps. Carathéodory's theorem therefore supplies a finite weighted collection of block unitaries with exactly the same two-copy average. Replacing the Haar sampling by that collection preserves every second-moment formula below. Each unitary still commutes with charge, and the original ensemble is finite. Its first moment remains $I/D$ under every such unitary.

### 3.2 Second-moment spectrum

Let $\Pi_{++}$ and $\Pi_{--}$ project onto the symmetric squares of the two charge sectors. Each has rank

$$
r_s=\frac{d(d+1)}{2}.
$$

Let $\Pi_{+-}$ project onto the symmetric cross-sector subspace spanned by $(|a_+b_-\rangle+|b_-a_+\rangle)/\sqrt2$, of rank $r_c=d^2$. These three orthogonal projectors sum to the projector onto the full symmetric subspace.

Independent block Haar averaging gives a scalar on each of these subspaces. Its weights follow from

$$
\mathbb E w_+^2=\mathbb E w_-^2=\frac{1+v}{4},
\qquad
2\mathbb E w_+w_-=\frac{1-v}{2}.
$$

Consequently,

$$
M_K^{\mathrm{block}}
=\frac{1+v}{4r_s}(\Pi_{++}+\Pi_{--})
 +\frac{1-v}{2r_c}\Pi_{+-}.
\tag{13}
$$

There are no coherences between these subspaces after the block average. For example, independent scalar phases in $U_+$ and $U_-$ already remove those coherences.

The Haar moment has eigenvalue $h=2/[D(D+1)]$ throughout the symmetric subspace. Put

$$
\Delta v=v-\frac1{D+1}.
$$

The two eigenvalue ratios of (13) to the Haar moment are

$$
\frac{\lambda_s}{h}
=\frac{D+1}{D+2}(1+v)
=1+\frac{D+1}{D+2}\Delta v,
\tag{14}
$$

$$
\frac{\lambda_c}{h}
=\frac{D+1}{D}(1-v)
=1-\frac{D+1}{D}\Delta v.
\tag{15}
$$

Both moments vanish on the antisymmetric subspace. Since $(D+1)/D>(D+1)/(D+2)$, the smallest multiplicative tolerance in (3) is exactly

$$
\boxed{
\eta_K=\frac{D+1}{D}\left|\frac1K-\frac1{D+1}\right|
=\frac{|D+1-K|}{DK}.
}
\tag{16}
$$

The total same-sector weight differs from Haar by $\Delta v/2$, while the cross-sector weight differs by $-\Delta v/2$. Thus its additive error is also explicit:

$$
\frac12\|M_K^{\mathrm{block}}-M_{\mathrm H}\|_1
=\frac{|\Delta v|}{2}.
\tag{17}
$$

### 3.3 Cost at fixed multiplicative tolerance

For $0\leq\eta<1$, choose

$$
K_\eta=\left\lceil\frac{D+1}{1+D\eta}\right\rceil.
\tag{18}
$$

Then $2\leq K_\eta\leq D+1$ and (16) gives $\eta_{K_\eta}\leq\eta$. For every $0<\eta<1$,

$$
F_R=4(K_\eta-1)
<4\frac{D+1}{1+D\eta}
<\frac4\eta.
\tag{19}
$$

At $\eta=0$, the same choice gives $K=D+1$ and the exact cost $4D$. For fixed positive $\eta$, the bound in (19) is independent of $D$.

The example uses pure conditional states, exact conservation, a finite reference, and a finite record. Its low cost is therefore not caused by mixed outputs or an omitted phase reference. It shows that multiplicative approximation of the two-copy moment alone does not retain the exact dimension factor. In particular, one cannot obtain a relative bound on the charge-mean variance by contracting (3) with $(Q_A-\mu I)\otimes(Q_A-\mu I)$: that operator is indefinite. The two-sided Fisher criterion in [Measurement geometry](measurement_geometry.md#4-two-sided-relative-fisher-isotropy) controls the relevant quadratic form directly.

## 4. Mixed conditional states and a sharp purity correction

### 4.1 Statement

For arbitrary conditional states $\rho_x$, define the mean impurity and the charge range by

$$
p_{\mathrm{imp}}=1-\sum_xp_x\mathrm{Tr}(\rho_x^2),
\qquad
\Delta q=q_{\max}-q_{\min}.
$$

Under the model in Section 1, with arbitrary finite-dimensional mixed reference state,

$$
\boxed{
v+\frac{(\Delta q)^2}{2}p_{\mathrm{imp}}
\geq\frac{V_A^2}{V_A+F_R/4}.
}
\tag{20}
$$

The coefficient $1/2$ is sharp. This bound concerns the actual retained ensemble, including any coarse graining of the measurement record. No purity promise is needed.

### 4.2 Refine the record by reference decomposition and total charge

Choose any pure-state decomposition

$$
\rho_R=\sum_jw_j|r_j\rangle\langle r_j|,
\qquad
V_j=\mathrm{Var}_{r_j}(Q_R).
$$

This is a mathematical decomposition, not access to a free physical label. For each pure component, refine the effect by the spectral projectors $\Pi_t$ of $T$:

$$
M_{x,t}=\Pi_tM_x\Pi_t.
$$

Commutation with $T$ ensures $\sum_tM_{x,t}=M_x$. Conditional on $j$, let $\rho_{jxt}$ be the normalized state of $A$ after the refined outcome, and put $a_{jxt}=\mathrm{Tr}(Q_A\rho_{jxt})$. Zero-probability branches can be omitted.

Completeness of the refined POVM gives, for every $j$,

$$
\mathbb E[a\mid j]=\mu,
\qquad
\mathrm{Var}(t\mid j)=V_A+V_j,
\qquad
\mathrm{Cov}(a,t\mid j)=-V_A.
\tag{21}
$$

For clarity, the last identity follows from $\sum_{x,t}tM_{x,t}=T$. Hence $\mathbb E[at\mid j]$ is the initial expectation of $Q_A T$. The $Q_AQ_B$ covariance on $|\Omega\rangle$ is $-V_A$, while the independent reference contributes no covariance. The variance of $T$ is the sum of the marginal variances on $B$ and $R$. These statements do not require the refined states of $A$ to be pure.

Cauchy–Schwarz applied to (21) gives

$$
\mathrm{Var}(a\mid j)\geq\frac{V_A^2}{V_A+V_j}.
$$

All conditional means over $j$ equal $\mu$, so the fully refined variance satisfies

$$
\begin{aligned}
v_{\mathrm{fine}}
&=\sum_jw_j\mathrm{Var}(a\mid j)\\
&\geq\sum_jw_j\frac{V_A^2}{V_A+V_j}
\geq\frac{V_A^2}{V_A+\sum_jw_jV_j},
\end{aligned}
\tag{22}
$$

where the final step uses convexity of $u\mapsto1/(V_A+u)$.

### 4.3 Bound the variance lost by forgetting the refinement

For a fixed retained outcome $x$, write its refined decomposition as $\rho_x=\sum_y\lambda_{y|x}\rho_y$, where $y$ collects $j$ and $t$. The law of total variance gives

$$
v_{\mathrm{fine}}-v
=\sum_x\frac{p_x}{2}\sum_{y,z}\lambda_{y|x}\lambda_{z|x}
\left[\mathrm{Tr}Q_A(\rho_y-\rho_z)\right]^2.
\tag{23}
$$

For any two density operators $\rho,\sigma$, trace-norm duality after subtracting the midpoint of the charge spectrum yields

$$
|\mathrm{Tr}Q_A(\rho-\sigma)|
\leq \Delta q\,D_{\mathrm{tr}}(\rho,\sigma),
\qquad
D_{\mathrm{tr}}(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\tag{24}
$$

We also need

$$
D_{\mathrm{tr}}(\rho,\sigma)^2\leq1-\mathrm{Tr}(\rho\sigma).
\tag{25}
$$

One direct proof is to decompose both states into pure states. Joint convexity of trace distance, its pure-state formula, and concavity of the square root give

$$
\begin{aligned}
D_{\mathrm{tr}}(\rho,\sigma)
&\leq\sum_{a,b}r_as_b\sqrt{1-|\langle\psi_a|\varphi_b\rangle|^2}\\
&\leq\sqrt{1-\sum_{a,b}r_as_b|\langle\psi_a|\varphi_b\rangle|^2}
=\sqrt{1-\mathrm{Tr}(\rho\sigma)}.
\end{aligned}
$$

Substitution into (23) gives

$$
\begin{aligned}
v_{\mathrm{fine}}-v
&\leq\frac{(\Delta q)^2}{2}
\sum_xp_x\sum_{y,z}\lambda_{y|x}\lambda_{z|x}
\left[1-\mathrm{Tr}(\rho_y\rho_z)\right]\\
&=\frac{(\Delta q)^2}{2}
\sum_xp_x\left[1-\mathrm{Tr}(\rho_x^2)\right]
=\frac{(\Delta q)^2}{2}p_{\mathrm{imp}}.
\end{aligned}
\tag{26}
$$

### 4.4 Optimize the reference decomposition

The established convex-roof identity for SLD quantum Fisher information is

$$
\frac14F_Q(\rho_R,Q_R)
=\inf_{\rho_R=\sum_jw_j|r_j\rangle\langle r_j|}
\sum_jw_j\mathrm{Var}_{r_j}(Q_R).
\tag{27}
$$

See Mohammady, Miyadera, and Loveridge [2, Eq. (13)], which also identifies the original convex-roof references. Combining (22) and (26), then choosing decompositions approaching the infimum in (27), proves (20). The decomposition label has not been supplied to the protocol and carries no uncharged operational resource.

### 4.5 Sharpness and the limit of the correction

For a qubit with charges $+1$ and $-1$, use a trivial reference and retain only a single outcome. Then $\rho_x=I/2$, $F_R=0$, $V_A=1$, $v=0$, $\Delta q=2$, and $p_{\mathrm{imp}}=1/2$. Both sides of (20) equal one. Thus a smaller universal coefficient multiplying $(\Delta q)^2p_{\mathrm{imp}}$ is impossible.

An exact second-moment target forces pure outputs even if purity was not separately imposed. Indeed,

$$
\mathrm{Tr}(SM_2)=\sum_xp_x\mathrm{Tr}(\rho_x^2),
\qquad
\mathrm{Tr}(SM_{\mathrm H})=1.
$$

Every density operator has purity at most one, so $M_2=M_{\mathrm H}$ implies that every positive-weight $\rho_x$ is pure. For an additive-error target, (2) instead gives the quantitative bound $p_{\mathrm{imp}}\leq2\delta$ by trace-norm duality. The multiplicative criterion (3) is different: its upper inequality forces $M_2$ to have zero weight on the antisymmetric subspace, whose weight is $p_{\mathrm{imp}}/2$. Thus (3) already forces exact purity. The counterexample in Section 3 satisfies this stronger requirement.

Equation (20) does not imply that fixed impurity preserves the exact dimension factor. The design charge-mean variance is $V_A/(D+1)$, so the impurity term must be controlled on that scale to retain the same order of lower bound. In particular, small fixed detector noise or small fixed average impurity does not by itself establish a reference cost of order $DV_A$.

## References

1. W. Lee, M. Hhan, G. Y. Cho, and H. Kwon, *Shallow Quantum Circuit for Generating Extremely Low-Entangled Approximate State Designs*, Physical Review Letters **136**, 150603 (2026). [Published article](https://doi.org/10.1103/p966-lcgs); [arXiv text](https://arxiv.org/html/2507.17871v3). This work concerns low-resource approximate design preparation in a different operational model.
2. M. H. Mohammady, T. Miyadera, and L. Loveridge, *Measurement disturbance and conservation laws in quantum mechanics*, Quantum **7**, 1033 (2023). [Published article](https://doi.org/10.22331/q-2023-06-05-1033); [arXiv text](https://arxiv.org/html/2110.11705v3). Equation (13) states the variance convex-roof identity used in (27).
