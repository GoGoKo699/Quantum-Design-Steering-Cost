# What the reference cost measures

The exact law $F_{Q,\min}=4DV_A$ concerns the physical realization of a pure-state decomposition of $I/D$. The maximally mixed average contains no charge coherence. Individual conditional states can have substantial coherence, and their charge expectations must also have the fluctuations required by the design. The apparatus is responsible for realizing that complete ensemble while conserving charge.

## 1. Output coherence and implementation coherence

For a pure ensemble with average $I/D$, define

$$
v=\operatorname{Var}_x[\langle Q_A\rangle_x].
$$

The law of total variance gives

$$
\sum_xp_xF_Q(\rho_x,Q_A)=4(V_A-v).
$$

An exact 2-design has $v=V_A/(D+1)$, so its average conditional QFI is

$$
\mathcal F_{\mathrm{out}}=\frac{4D}{D+1}V_A.
$$

The required reference QFI is instead $4DV_A$, a factor $D+1$ larger than this output average when $V_A>0$. Output resource monotonicity by itself therefore misses the implementation cost. The sharper relation,

$$
\mathcal F_{\mathrm{out}}
\leq\frac{4V_AF_R}{4V_A+F_R},
$$

retains the restriction that the apparatus acts only on the entangled partner. Its [proof](reference_bound.md) is an application of established finite-reference QFI methods.

The covariance form explains the factor. If the reference is pure, the refined measurement record contains total external charge $T=Q_B+Q_R$. The conditional system charge mean and $T$ have covariance $-V_A$. A design demands conditional-mean variance only $V_A/(D+1)$. Cauchy–Schwarz can permit that concentration only when the external charge variance is at least $(D+1)V_A$, of which $V_A$ comes from $B$ and $DV_A$ from the reference. The finite construction attains this relation.

## 2. Direct control changes the task

The remote-access restriction has a concrete consequence. Suppose that $A$ can instead be prepared directly in

$$
|+_D\rangle=\frac{1}{\sqrt D}\sum_i|i\rangle,
$$

which has QFI $4V_A$. Let any desired pure ensemble have normalized vectors
$|\psi_x\rangle=\sum_i\psi_{x,i}|i\rangle$, probabilities $p_x$, and average $I/D$. Define diagonal Kraus operators on $A$ by

$$
K_x=\sqrt{Dp_x}\sum_i\psi_{x,i}|i\rangle\langle i|.
$$

They commute with $Q_A$. The diagonal part of the ensemble average gives

$$
\sum_xK_x^\dagger K_x
=D\sum_i\left(\sum_xp_x|\psi_{x,i}|^2\right)|i\rangle\langle i|
=I.
$$

Moreover,

$$
K_x|+_D\rangle=\sqrt{p_x}\,|\psi_x\rangle.
$$

This conserving instrument prepares the requested ensemble, including an exact design, from initial QFI $4V_A$. Its diagonal Kraus operators admit a neutral-pointer dilation by the same charge-block isometry argument used for the remote measurement.

This is a sufficient direct protocol. Together with the remote optimum, it gives a factor-$D$ comparison between the exact remote cost and this explicit direct cost. No exact optimum for the directly controlled task is asserted. A protocol that supplies coherent input directly on $A$ has changed both the accessible subsystem and the supplied resource.

## 3. Excitation-conserving qubits

For $m$ qubits, take

$$
D=2^m,\qquad
Q_A=\sum_{j=1}^{m}|1\rangle\langle1|_j.
$$

In the maximally mixed state, the $m$ occupations are independent fair bits, so

$$
\mu=m/2,\qquad V_A=m/4.
$$

The exact remote design cost is therefore

$$
F_{Q,\min}=m2^m.
$$

The product reference used in the construction contains $D$ copies of the uniform $D$-level state at the exact endpoint. Its total charge distribution can be compressed to a single ladder with a binomial distribution:

$$
|r\rangle
=\sum_{n=0}^{mD}\sqrt{\binom{mD}{n}2^{-mD}}\,|n\rangle,
$$

up to a sign and scalar shift of the reference charge. This state has variance $mD/4$ and QFI $mD$, on $mD+1$ distinct charge levels. The conserving POVM can be pulled back to this compressed reference without changing the conditional ensemble.

The QFI scaling does not itself specify a number of physical qubits. Encoding a charge ladder requires a physical choice of charge operator and a measurement implementation. The theorem charges phase sensitivity, and the compression establishes a finite realization within that accounting.

## 4. Exactness and the accuracy criterion

The same construction with $K-1$ reference factors costs $4(K-1)V_A$ and has additive moment error

$$
\delta_K=\frac{D-1}{D}
\left|\frac1K-\frac1{D+1}\right|.
$$

At fixed positive additive tolerance, $K$ can be bounded independently of $D$. For excitation qubits, the resulting QFI is of order $m/\delta$, rather than $m2^m$. The [accuracy proof](accuracy.md) also gives a balanced two-charge example with fixed multiplicative moment error and dimension-independent reference cost.

Relative Fisher isotropy asks a different question. It constrains the information about every traceless perturbation of $I/D$ to be close on both sides to the symmetric benchmark, while retaining exactly rank-one effects. This criterion controls the small charge-mean variance directly and preserves a cost of order $DV_A$. The [finite-$K$ spectrum](measurement_geometry.md) gives a construction within an additive $4V_A$ of its converse.

Two-sided isotropy is stronger than having useful information in every direction. A cheap measurement in the same family can provide nearly the symmetric information in all off-diagonal directions and much more in the diagonal directions. It is consequently competitive under a one-sided information criterion. This distinction prevents an inference from the exact design theorem to a general obstruction for tomography.

Output purity also has a quantitative role. For arbitrary mixed conditional states,

$$
v+\frac{(q_{\max}-q_{\min})^2}{2}
\left(1-\sum_xp_x\operatorname{Tr}\rho_x^2\right)
\geq\frac{V_A^2}{V_A+F_R/4}.
$$

The correction is proved and shown sharp in [the purity analysis](accuracy.md#4-mixed-conditional-states-and-a-sharp-purity-correction). It makes the precision requirements visible: a small fixed impurity is not sufficient to retain a lower bound on the much smaller design fluctuation scale $V_A/(D+1)$.

## 5. Relation to projected ensembles

Projected-ensemble studies ask which state distributions emerge when part of a larger quantum system is measured. In charge-conserving dynamics, the initial charge distribution and the chosen measurement basis can influence the limiting ensemble. Recent work also relates projected ensembles to quantum resource generation. Those results provide direct motivation for asking how the selected measurement is physically supplied. The [related-work account](../references/RELATED_WORK.md#projected-ensembles-and-deep-thermalization) distinguishes their models and claims.

The present source is a fixed maximally entangled pair, and the apparatus is optimized explicitly. No chaotic dynamics, thermalization rate, or locality assumption enters the theorem. Its conclusion is an exact physical cost for a measurement capability in this setting. The finite realization and the accuracy formulas identify both what conservation requires and which changes to the target make that requirement cheaper.
