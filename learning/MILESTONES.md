# Project understanding map: 30 milestones

This map connects the physical task of remote state preparation to its exact reference cost and its accuracy limits. It contains exactly **30 milestones**, with understanding targets and dependencies defined by the scientific argument.

The allocation is **13 background/preliminaries milestones** and **17 narrative/innovation milestones**. The background joins several kinds of information: density operators and measurements, additive charge conservation, quantum Fisher information, state moments, and local statistical geometry. Its final milestone assembles these into one operational question. The narrative then follows the converse and finite construction to an attained optimum before examining the different consequences of additive error, multiplicative error, mixed outputs, and Fisher isotropy. Its final milestones integrate the physical meaning and evidence for that complete account.

The single educational anchor is John Watrous's *The Theory of Quantum Information*, using the **2018 author-posted prepublication manuscript**, whose preface is dated January 2018. The [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies the manuscript. The [Watrous bridge](WATROUS_BRIDGE.md#targeted-reading) identifies the relevant sections, translates notation, and supplies the steps that the anchor does not cover. Watrous provides the finite-dimensional quantum-information foundations. The charge-resource model, SLD-QFI argument, conserving design construction, and Fisher-cost consequences are developed in the linked scientific pages, with their research antecedents attributed there.

Each milestone states a central question, an understanding target, earlier dependencies and its role in the story, a conceptual connection, and source pointers. The phase headings assign the phase of each milestone. The map supports a connected understanding of the result; complete proofs and specialist calculations remain in their canonical topic files.

## Route through the project

| Phase | Milestones | Connection established |
| --- | --- | --- |
| Background/preliminaries | [M01](#m01-states-mixtures-and-charge-observables) to [M04](#m04-steering-and-the-effective-measurement) | States, measurements, and remote conditional ensembles |
| Background/preliminaries | [M05](#m05-conservation-and-charge-sectors) to [M08](#m08-qfi-under-channels-and-classical-conditioning) | Charge conservation, complete resource accounting, and reference QFI |
| Background/preliminaries | [M09](#m09-symmetric-tensors-and-haar-second-moments) to [M13](#m13-the-complete-operational-question) | Design moments, statistical geometry, and the complete optimization |
| Narrative/innovation | [M14](#m14-an-auxiliary-generator-that-preserves-the-output) to [M16](#m16-exact-moments-impose-the-converse) | A mixed-reference information bound gives the exact converse |
| Narrative/innovation | [M17](#m17-a-reference-built-from-independent-charge-samples) to [M21](#m21-the-attained-all-spectrum-optimum) | Charge samples, count sectors, and finite phase effects attain the bound |
| Narrative/innovation | [M22](#m22-additive-accuracy-changes-the-cost) to [M24](#m24-mixed-outputs-and-the-purity-correction) | Moment accuracy and imperfect purity change the resource question |
| Narrative/innovation | [M25](#m25-the-exact-measurement-interpretation) to [M27](#m27-one-sided-statistical-usefulness) | Tight measurements, two-sided isotropy, and one-sided information have distinct costs |
| Narrative/innovation | [M28](#m28-remote-access-and-the-meaning-of-the-cost) to [M30](#m30-the-complete-scientific-story) | Physical interpretation, attribution, and the complete scientific account |

## Phase I: background/preliminaries

### M01 States, mixtures, and charge observables

**Central question.** Which mathematical objects describe the system and the charge whose coherence is being counted?

**Understanding target.** Interpret a density operator as positive and trace one, a pure state as rank one, and a mixed state as admitting ensemble decompositions. Read the spectral expression $Q_A=\sum_iq_i|i\rangle\langle i|$ and the variance $V_A=\mathrm{Tr}(Q_A-\mu I)^2/D$, with $\mu=\mathrm{Tr}Q_A/D$. Distinguish a basis label from its charge value when charges are degenerate.

**Dependencies and story role.** No earlier milestones. This introduces the states and observables used throughout the map.

**Conceptual connection.** A maximally mixed density operator and a distribution of pure states with that average contain different conditional information. That distinction will make an ensemble-preparation task meaningful even when the unconditional system has no charge coherence.

**Source pointers.** Watrous §2.1.2; [notation and conventions](WATROUS_BRIDGE.md#notation-and-conventions); [system and charge](../science/model.md#1-entangled-source-and-conserved-charge).

### M02 Composite systems and an untouched marginal

**Central question.** How can a globally sharp charge coexist with nontrivial charge fluctuations on each subsystem?

**Understanding target.** Interpret tensor products, partial trace, and the maximally entangled vector $|\Omega\rangle=D^{-1/2}\sum_i|i\rangle_A|i\rangle_B$. With $Q_B=-Q_A^{\mathsf T}$, explain its sharp total charge and its two maximally mixed marginals. Distinguish correlations already present in $AB$ from an independent apparatus state.

**Dependencies and story role.** [M01](#m01-states-mixtures-and-charge-observables). The local objects become the correlated source on which the remote task is defined.

**Conceptual connection.** Global charge symmetry does not remove the correlations that a measurement on $B$ can reveal in $A$. Leaving $A$ untouched constrains how those correlations can be converted into a retained ensemble.

**Source pointers.** Watrous §§2.1.2–2.1.3; [entangled source](../science/model.md#1-entangled-source-and-conserved-charge); [steering from a fixed average](WATROUS_BRIDGE.md#steering-from-a-fixed-average).

### M03 POVMs, instruments, and neutral records

**Central question.** What does the apparatus measure, and what information remains after the measurement?

**Understanding target.** Distinguish a POVM effect, an instrument's state transformation, and a classical outcome label. Use positivity and completeness of the effects to obtain normalized outcome probabilities. Interpret a neutral record as one whose labels neither rotate nor get relabeled under the charge symmetry, and retain all outcomes.

**Dependencies and story role.** [M01](#m01-states-mixtures-and-charge-observables), [M02](#m02-composite-systems-and-an-untouched-marginal). This specifies the operation and record before imposing its conservation law.

**Conceptual connection.** Internal apparatus disturbance can be discarded, but a retained setting or preparation label remains part of the operational description. Selecting only successful outcomes changes the complete-ensemble task.

**Source pointers.** Watrous §§2.2.1–2.2.2 and §§2.3.1–2.3.3; [allowed measurement and retained ensemble](../science/model.md#2-allowed-measurement-and-retained-ensemble).

### M04 Steering and the effective measurement

**Central question.** How does a measurement on the partner specify the states prepared remotely?

**Understanding target.** Explain why the unnormalized conditional state on untouched $A$ depends only on the effect on the discarded systems. Completeness gives $\sum_xp_x\rho_x=I/D$. Relate the effective POVM on $B$ to the ensemble through $E_x=Dp_x\rho_x^{\mathsf T}$, and recognize the transpose as a consequence of the chosen paired basis.

**Dependencies and story role.** [M02](#m02-composite-systems-and-an-untouched-marginal), [M03](#m03-povms-instruments-and-neutral-records). This connects a physical measurement to the ensemble that the later theorem constrains.

**Conceptual connection.** The same object can be described as remote state preparation or as a measurement with normalized effects. Pure conditional states correspond to rank-one effective effects, while the reference itself may be mixed.

**Source pointers.** Watrous §2.3.3 and Exercise 2.2; [steering bridge](WATROUS_BRIDGE.md#steering-from-a-fixed-average); [effective POVM identity](../science/measurement_geometry.md#1-from-remote-preparation-to-a-povm).

### M05 Conservation and charge sectors

**Central question.** Which measurements respect the charge restriction without using an external phase reference?

**Understanding target.** Interpret $[M_x,Q_B+Q_R]=0$ for each fixed label as block structure in total-charge eigenspaces. Distinguish individual invariance from a measurement whose outcomes transform with the symmetry. Arbitrary finite real spectra generate real-parameter time translations; a compact $U(1)$ description requires a common charge lattice for the system and apparatus, up to scalar shifts.

**Dependencies and story role.** [M01](#m01-states-mixtures-and-charge-observables), [M03](#m03-povms-instruments-and-neutral-records). This adds the physical restriction to the measurement model.

**Conceptual connection.** Degeneracy permits operations within a charge sector and does not require distinct basis labels to be identified. The construction will use this freedom while never coupling different total charges.

**Source pointers.** [Conservation bridge](WATROUS_BRIDGE.md#conservation-and-an-independent-reference); [charge and group scope](../science/model.md#1-entangled-source-and-conserved-charge); [invariant effects](../science/model.md#2-allowed-measurement-and-retained-ensemble).

### M06 Independent references and resource accounting

**Central question.** Which initial coherence must be charged to the apparatus?

**Understanding target.** Assemble the independent input $|\Omega\rangle\langle\Omega|\otimes\rho_R$ and include every accessible asymmetric helper in $R$. A neutral flag selecting coherent preparations remains part of the charged state when it is accessible. Distinguish reference consumption from a return requirement, and reference QFI from dimension, mean energy, locality, outcome count, and computation.

**Dependencies and story role.** [M02](#m02-composite-systems-and-an-untouched-marginal), [M03](#m03-povms-instruments-and-neutral-records), [M05](#m05-conservation-and-charge-sectors). This defines the optimization domain before choosing its numerical resource measure.

**Conceptual connection.** Forgetting an accessible flag only in the accounting can conceal useful coherence. Allowing arbitrary finite conserving interactions does not promise that their physical implementation is small or local.

**Source pointers.** [Independent-reference bridge](WATROUS_BRIDGE.md#conservation-and-an-independent-reference); [flags and retained records](../science/model.md#2-allowed-measurement-and-retained-ensemble); [charged and uncharged resources](../science/model.md#3-charged-resource).

### M07 Charge variance and quantum Fisher information

**Central question.** Why is phase sensitivity measured by QFI rather than by charge variance for every state?

**Understanding target.** Interpret SLD quantum Fisher information for $e^{-i\theta Q}\rho e^{i\theta Q}$ as local sensitivity to the phase parameter. Fix the normalization $F_Q(|r\rangle,Q)=4\mathrm{Var}_r(Q)$. For mixed states, separate charge fluctuations from coherence: a charge-diagonal state can have positive variance and zero QFI.

**Dependencies and story role.** [M01](#m01-states-mixtures-and-charge-observables), [M05](#m05-conservation-and-charge-sectors), [M06](#m06-independent-references-and-resource-accounting). This supplies the cost variable used in the theorem.

**Conceptual connection.** A variance bound for a pure reference is not automatically the desired bound for an arbitrary mixed reference. The distinction determines what the converse must prove and why charge units must be held fixed.

**Source pointers.** [Locally supplied QFI bridge](WATROUS_BRIDGE.md#quantum-fisher-information-as-the-reference-cost); [QFI convention](../science/reference_bound.md#1-input-measurement-and-qfi-convention); [metrological antecedents](../references/RELATED_WORK.md#finite-reference-metrology).

### M08 QFI under channels and classical conditioning

**Central question.** How can a measurement channel turn a phase-sensitivity statement into a resource bound?

**Understanding target.** Connect a parameter-independent quantum channel to QFI data processing, product families to additive QFI, and a neutral classical record to a block-diagonal output state. When outcome probabilities are parameter independent, its QFI is the probability-weighted sum of conditional QFIs, with no classical Fisher term from the record.

**Dependencies and story role.** [M03](#m03-povms-instruments-and-neutral-records), [M07](#m07-charge-variance-and-quantum-fisher-information). This combines the channel description with the sensitivity measure needed for the converse.

**Conceptual connection.** The bound concerns the full record and system together. Its application requires checking which parameter family reaches that output, rather than assuming that conditioning preserves a sensitivity inequality branch by branch.

**Source pointers.** Watrous §§2.2.1–2.2.2 for channels; [QFI bridge](WATROUS_BRIDGE.md#quantum-fisher-information-as-the-reference-cost); [block-state and product-QFI arguments](../science/reference_bound.md#2-a-bound-for-arbitrary-mixed-outputs).

### M09 Symmetric tensors and Haar second moments

**Central question.** What does a state 2-design reproduce about Haar-random pure states?

**Understanding target.** Read $M_2=\sum_xp_x\rho_x^{\otimes2}$ as an ensemble moment on two copies. Connect the swap operator $\mathsf S$, the symmetric subspace, and the Haar value $M_{\mathrm H}=(I+\mathsf S)/[D(D+1)]$. The partial trace fixes the first moment, and the swap expectation tests average purity.

**Dependencies and story role.** [M01](#m01-states-mixtures-and-charge-observables), [M02](#m02-composite-systems-and-an-untouched-marginal), [M04](#m04-steering-and-the-effective-measurement). This specifies the tensor target rather than only selected output statistics.

**Conceptual connection.** A finite weighted ensemble can have the required moment without being a continuous Haar distribution. The moment condition is stronger than the statement that its average state is maximally mixed.

**Source pointers.** Watrous §7.1.1 and §§7.2.1–7.2.2, especially Lemma 7.24 for the Haar moment; [exact design target](../science/model.md#4-exact-design-target); [swap and purity](../science/reference_bound.md#4-exact-second-moments-force-purity).

### M10 Finite designs from amplitudes and phases

**Central question.** How can classical amplitude statistics and finite phase averaging control a quantum state moment?

**Understanding target.** Write a normalized state as $\sum_i\sqrt{p_i}e^{i\phi_i}|i\rangle$. Identify the amplitude moments and phase cancellations entering its second tensor moment. Independent third-root phases remove every nonzero coordinate exponent between $-2$ and $2$, so a finite phase set suffices at this moment order.

**Dependencies and story role.** [M01](#m01-states-mixtures-and-charge-observables), [M09](#m09-symmetric-tensors-and-haar-second-moments). This introduces the design-building ingredients before assigning them a conserving apparatus.

**Conceptual connection.** Matching a moment algebraically is only one requirement. The physical task also needs a single independent reference and complete invariant effects that realize the chosen amplitude distribution.

**Source pointers.** Watrous §7.2.2 for Haar averages; [amplitude-phase attribution](../references/RELATED_WORK.md#amplitude-and-phase-constructions); [phase and occupation averages](../science/accuracy.md#22-phase-and-occupation-averages).

### M11 Informational completeness and Fisher geometry

**Central question.** How do ensemble moments describe information obtained by a measurement near the maximally mixed state?

**Understanding target.** Use the effective POVM from M04 and the local model $\sigma_\theta=e^{\theta H}/\mathrm{Tr}(e^{\theta H})$ for traceless Hermitian $H$. Interpret its classical Fisher information as a quadratic form on perturbation directions. Distinguish positivity of this form, which gives local informational completeness, from equal sensitivity in every direction.

**Dependencies and story role.** [M04](#m04-steering-and-the-effective-measurement), [M09](#m09-symmetric-tensors-and-haar-second-moments). This connects the ensemble target to the statistical geometry used in the later accuracy statements.

**Conceptual connection.** The physical reference cost concerns a measurement capability. Understanding the geometry makes it possible to distinguish isotropy from the weaker condition that every direction is measured usefully.

**Source pointers.** Watrous §§2.3.1–2.3.3 for measurement foundations; [local statistical model](../science/measurement_geometry.md#21-the-local-statistical-model); [Fisher bridge](WATROUS_BRIDGE.md#fisher-isotropy-and-useful-information).

### M12 Distance, purity, and distinct approximation criteria

**Central question.** What is being approximated when an ensemble is called close to a design?

**Understanding target.** Distinguish half trace-norm moment error, a positive-semidefinite multiplicative sandwich for $M_2$, and a two-sided relative bound on the Fisher quadratic form. Separate these from average conditional purity. Recognize that contracting an operator inequality with an indefinite charge witness does not preserve its order.

**Dependencies and story role.** [M07](#m07-charge-variance-and-quantum-fisher-information), [M09](#m09-symmetric-tensors-and-haar-second-moments), [M11](#m11-informational-completeness-and-fisher-geometry). This gives the distinctions needed to state an approximate result without changing its meaning.

**Conceptual connection.** Additive moment error need not preserve exact purity or Fisher isotropy. The upper inequality $M_2\preceq(1+\eta)M_{\mathrm H}$ still forces exact purity through its zero antisymmetric support, but it does not force the Fisher isotropy needed for a dimension-dependent cost at fixed positive $\eta$.

**Source pointers.** Watrous §§1.1.3 and 3.1.1 for norms and distinguishability; [moment-error definitions](../science/accuracy.md#1-setting-and-conventions); [accuracy bridge](WATROUS_BRIDGE.md#accuracy-and-the-role-of-purity).

### M13 The complete operational question

**Central question.** Which complete experiment and which minimum does the theorem describe?

**Understanding target.** Assemble finite-dimensional $A,B,R$, the sharp-charge maximally entangled source, an independent possibly mixed reference, individually invariant effects, a neutral complete record, and untouched $A$. The target is some weighted exact complex projective 2-design. The minimized quantity is initial reference QFI, with arbitrary finite collective conserving apparatuses and no reference-return requirement.

**Dependencies and story role.** [M06](#m06-independent-references-and-resource-accounting), [M08](#m08-qfi-under-channels-and-classical-conditioning), [M10](#m10-finite-designs-from-amplitudes-and-phases), [M12](#m12-distance-purity-and-distinct-approximation-criteria). This integrates the background into the precise question that the narrative answers.

**Conceptual connection.** A prescribed SIC, a continuous Haar ensemble, an initially correlated reference, a retained asymmetric pointer, or conditional control on $A$ changes the task. Finite attainment of the stated minimum makes no claim about those changed optimizations.

**Source pointers.** [Complete model](../science/model.md); [exact optimization and scope](../science/reference_bound.md#5-the-attained-optimum-and-its-scope); [bridge to the full story](WATROUS_BRIDGE.md#connecting-the-full-story).

## Phase II: narrative/innovation

### M14 An auxiliary generator that preserves the output

**Central question.** Why can different input phase encodings be compared to the same conditional output family?

**Understanding target.** Introduce $G_\lambda=Q_A+\lambda(Q_B+Q_R)$ as a proof generator. Commutation of every effect with $T=Q_B+Q_R$ removes the $BR$ rotation after tracing out the apparatus, while the $A$ rotation passes through. For every real $\lambda$, the output family is the same record of states rotated by $Q_A$, with unchanged probabilities.

**Dependencies and story role.** [M05](#m05-conservation-and-charge-sectors), [M08](#m08-qfi-under-channels-and-classical-conditioning), [M13](#m13-the-complete-operational-question). This identifies the common output against which input information can be minimized.

**Conceptual connection.** The auxiliary encoding is a mathematical comparison. It does not give the steering apparatus permission to act on $A$ or to access the parameter.

**Source pointers.** [Comparison-generator bridge](WATROUS_BRIDGE.md#the-comparison-generator-and-the-bound); [channel intertwining proof](../science/reference_bound.md#2-a-bound-for-arbitrary-mixed-outputs).

### M15 The mixed-reference information bound

**Central question.** How does the common output impose a stronger cost than ordinary output-QFI monotonicity alone?

**Understanding target.** Combine the sharp total charge of $AB$ with reference independence to obtain input QFI $4(1-\lambda)^2V_A+\lambda^2F_R$. QFI data processing and minimization over $\lambda$ give

$$
\sum_xp_xF_Q(\rho_x,Q_A)\leq\frac{4V_AF_R}{4V_A+F_R}.
$$

The statement allows mixed references and mixed conditional states; the right-hand side is zero when both $V_A$ and $F_R$ vanish.

**Dependencies and story role.** [M07](#m07-charge-variance-and-quantum-fisher-information), [M08](#m08-qfi-under-channels-and-classical-conditioning), [M14](#m14-an-auxiliary-generator-that-preserves-the-output). This proves the information obstruction before imposing a design target.

**Conceptual connection.** The harmonic form records both the supplied entangled correlations and the independent reference. Its method belongs to established finite-reference metrology; the remaining task is to match it with a feasible complete design.

**Source pointers.** [Mixed-output theorem and proof](../science/reference_bound.md#2-a-bound-for-arbitrary-mixed-outputs); [finite-reference attribution](../references/RELATED_WORK.md#finite-reference-metrology).

### M16 Exact moments impose the converse

**Central question.** How does the design tensor turn the information obstruction into the factor $D$?

**Understanding target.** Use the swap expectation of an exact Haar second moment to force purity of every positive-weight output. For a pure ensemble, the average QFI is $4(V_A-v)$, where $v$ is the variance of its conditional charge means. The design fixes $v=V_A/(D+1)$, so M15 implies $F_R\geq4DV_A$; the $V_A=0$ case is trivial.

**Dependencies and story role.** [M09](#m09-symmetric-tensors-and-haar-second-moments), [M13](#m13-the-complete-operational-question), [M15](#m15-the-mixed-reference-information-bound). This completes necessity for the exact target.

**Conceptual connection.** Exactness supplies the purity and the small charge-mean variance needed here. This derivation does not justify replacing either condition by an arbitrary fixed error tolerance.

**Source pointers.** [Pure-ensemble variance relation](../science/reference_bound.md#3-pure-ensembles-and-their-conditional-charge-means); [exact-moment converse](../science/reference_bound.md#4-exact-second-moments-force-purity).

### M17 A reference built from independent charge samples

**Central question.** Which finite reference has charge statistics suited to saturating the bound?

**Understanding target.** For an integer $K\geq1$, take $K-1$ uniform $D$-level superpositions with charge $-q_i$ on label $i$. Their total reference charge is the negative sum of independent uniform label charges, giving $F_R=4(K-1)V_A$. At $K=1$ the reference is trivial. Scalar shifts can make its finite spectrum nonnegative without changing QFI.

**Dependencies and story role.** [M05](#m05-conservation-and-charge-sectors), [M07](#m07-charge-variance-and-quantum-fisher-information), [M10](#m10-finite-designs-from-amplitudes-and-phases), [M16](#m16-exact-moments-impose-the-converse). This supplies the independent apparatus state for the constructive side.

**Conceptual connection.** The reference distribution is chosen together with the ensemble, rather than after prescribing a particular design. Its variance is additive because its factors are independent and pure.

**Source pointers.** [Reference and charge accounting](../science/conserving_construction.md#1-reference-and-charge-accounting); [finite construction bridge](WATROUS_BRIDGE.md#finite-count-and-phase-attainment).

### M18 Count sectors turn multiplicities into amplitudes

**Central question.** How do uniform reference amplitudes produce the nonuniform amplitudes needed by the design?

**Understanding target.** Count labels across $B$ and the $K-1$ reference factors. A count vector $N$ has total charge $-\sum_iq_iN_i$ and multinomial probability. For a fixed $B$ label $i$, the relative number of reference strings is $N_i/K$, so normalized coherent sums carry amplitudes $\sqrt{N_i/K}$.

**Dependencies and story role.** [M02](#m02-composite-systems-and-an-untouched-marginal), [M05](#m05-conservation-and-charge-sectors), [M17](#m17-a-reference-built-from-independent-charge-samples). This identifies the physical origin of the chosen amplitude statistics.

**Conceptual connection.** Counting refines charge sectors without violating conservation. Distinct label counts can share the same charge, and repeated system eigenvalues leave the orthogonal basis labels and multiplicity argument intact.

**Source pointers.** [Count sectors and occupied vectors](../science/conserving_construction.md#2-count-sectors-and-the-occupied-subspace); [conditional contraction](../science/conserving_construction.md#4-conditional-states-and-probabilities).

### M19 A finite phase measurement with full completeness

**Central question.** Which invariant effects turn the occupied count sector into the desired pure ensemble?

**Understanding target.** On the occupied vectors $|u_{i,N}\rangle$, use phase vectors $\sum_i e^{-i\phi_i}|u_{i,N}\rangle$ with independent third-root phases. Their weighted effects sum to the occupied projector. Include the complementary effect on the remaining Hilbert space, even though it has zero probability on the supplied input. The output is $\sum_i\sqrt{N_i/K}e^{i\phi_i}|i\rangle$ with the full stated count and phase probabilities.

**Dependencies and story role.** [M03](#m03-povms-instruments-and-neutral-records), [M10](#m10-finite-designs-from-amplitudes-and-phases), [M18](#m18-count-sectors-turn-multiplicities-into-amplitudes). This turns the amplitude mechanism into a complete finite measurement.

**Conceptual connection.** Phase labels describe effects acting inside fixed total-charge sectors. They do not supply another external phase reference, and the zero-probability completion is not postselection.

**Source pointers.** [Finite phase effects](../science/conserving_construction.md#3-a-finite-phase-povm-in-each-count-sector); [probabilities and pure outputs](../science/conserving_construction.md#4-conditional-states-and-probabilities).

### M20 A conserving pointer and compressed reference

**Central question.** Does the effect construction admit a fully conserving finite apparatus, including its readout?

**Understanding target.** Use the measurement isometry built from $M_x^{1/2}$ and extend it to a unitary separately inside each total-charge eigenspace. A pointer with zero charge can be prepared and read without additional asymmetry. Compress this pure reference to one occupied vector per distinct charge through a charge-intertwining isometry; pulling back the effects preserves completeness, invariance, conditional states, and QFI.

**Dependencies and story role.** [M03](#m03-povms-instruments-and-neutral-records), [M05](#m05-conservation-and-charge-sectors), [M06](#m06-independent-references-and-resource-accounting), [M19](#m19-a-finite-phase-measurement-with-full-completeness). This closes the implementation and accounting requirements of the construction.

**Conceptual connection.** Finite realization is an existence statement about allowed conserving interactions. Compression preserves the operational result but does not prove an optimum for apparatus dimension, circuit size, or interaction time.

**Source pointers.** Watrous Theorem 2.42 and its following corollary for dilation foundations; [neutral-pointer realization](../science/conserving_construction.md#6-a-conserving-unitary-and-neutral-pointer); [charge compression](../science/conserving_construction.md#7-compression-to-one-reference-vector-per-charge).

### M21 The attained all-spectrum optimum

**Central question.** Where do complete design moments and physical feasibility meet at the same resource value?

**Understanding target.** Combine the multinomial amplitude moments with finite phase cancellation to obtain

$$
M_K=\frac{K-1}{KD^2}(I+\mathsf S)
+\frac{D+1-K}{KD^2}\Pi_{\mathrm{diag}},
\qquad
\Pi_{\mathrm{diag}}=\sum_i|ii\rangle\langle ii|.
$$

At $K=D+1$, this is the exact Haar moment and the reference costs $4DV_A$. Together with M16 it proves an attained minimum for every finite real spectrum, including degeneracies. Scalar charge and $D=1$ give zero cost.

**Dependencies and story role.** [M16](#m16-exact-moments-impose-the-converse), [M19](#m19-a-finite-phase-measurement-with-full-completeness), [M20](#m20-a-conserving-pointer-and-compressed-reference). This integrates the converse and construction into the main result.

**Conceptual connection.** The family also attains $v=V_A/K$ at each integer $K$. Those discrete saturation points do not assert an exact optimum for every prescribed design or every continuous approximate budget.

**Source pointers.** [Moment identity and saturation](../science/conserving_construction.md#5-exact-design-and-equality-in-the-reference-bound); [attained minimum and scope](../science/reference_bound.md#5-the-attained-optimum-and-its-scope); [complete qubit example](WATROUS_BRIDGE.md#a-complete-qubit-example).

### M22 Additive accuracy changes the cost

**Central question.** How much of the exact resource cost remains at fixed positive moment trace-distance error?

**Understanding target.** Read the symmetric-subspace spectrum of $M_K-M_{\mathrm H}$ to obtain $\delta_K=(D-1)|1/K-1/(D+1)|/D$. For $0<\delta<1$, choosing $K=\min\{D+1,\lceil1/\delta\rceil\}$ gives an achievable cost below $4V_A/\delta$ when $V_A>0$, and zero when $V_A=0$. This is an upper bound, not an optimal additive-error frontier.

**Dependencies and story role.** [M12](#m12-distance-purity-and-distinct-approximation-criteria), [M21](#m21-the-attained-all-spectrum-optimum). This shows precisely why exact attainment does not imply the same dimension factor at fixed additive accuracy.

**Conceptual connection.** The finite construction can approach the Haar second moment cheaply while retaining larger fluctuations in selected directions. Increasing $K$ past the exact point does not monotonically improve this family's moment error.

**Source pointers.** [Half trace-norm error](../science/accuracy.md#23-half-trace-norm-error); [physical accuracy interpretation](../science/interpretation.md#4-exactness-and-the-accuracy-criterion).

### M23 A conserving multiplicative counterexample

**Central question.** Does a multiplicative operator bound on the second moment restore the exact dimension factor?

**Understanding target.** For $D=2d$ with balanced charges $+1,-1$, randomize the multinomial outputs within the two charge sectors by an allowed operation on $B$. A finite weighted randomization reproduces the required block average. Its multiplicative error is $\eta_K=|D+1-K|/(DK)$. For fixed $0<\eta<1$, a finite choice of $K$ gives cost below $4/\eta$, independent of $D$; zero tolerance returns the exact endpoint.

**Dependencies and story role.** [M05](#m05-conservation-and-charge-sectors), [M12](#m12-distance-purity-and-distinct-approximation-criteria), [M21](#m21-the-attained-all-spectrum-optimum), [M22](#m22-additive-accuracy-changes-the-cost). This tests a stronger-looking error criterion by a physical counterexample.

**Conceptual connection.** The example uses pure outputs, a finite reference, and a neutral finite record. It refutes a universal dimension-cost claim for this criterion, without asserting a cheap construction for every charge spectrum.

**Source pointers.** [Balanced-charge construction and spectrum](../science/accuracy.md#3-a-multiplicative-error-counterexample-with-two-balanced-charges); [accuracy bridge](WATROUS_BRIDGE.md#accuracy-and-the-role-of-purity).

### M24 Mixed outputs and the purity correction

**Central question.** Which part of the pure-ensemble obstruction survives when retained outputs are mixed?

**Understanding target.** With $p_{\mathrm{imp}}=1-\sum_xp_x\mathrm{Tr}\rho_x^2$ and $\Delta q=q_{\max}-q_{\min}$, understand the bound

$$
v+\frac{(\Delta q)^2}{2}p_{\mathrm{imp}}
\geq\frac{V_A^2}{V_A+F_R/4}.
$$

Reference decomposition and total-charge refinement give the fine-record variance bound; trace distance controls the variance lost on forgetting the refinement. The QFI convex roof handles mixed references. The scalar-charge case has zero lower bound.

**Dependencies and story role.** [M07](#m07-charge-variance-and-quantum-fisher-information), [M12](#m12-distance-purity-and-distinct-approximation-criteria), [M15](#m15-the-mixed-reference-information-bound), [M16](#m16-exact-moments-impose-the-converse). This quantifies the purity qualification rather than dropping it.

**Conceptual connection.** The decomposition label is mathematical, not an accessible free preparation flag. The coefficient is sharp, and a fixed nonzero impurity cannot simply be ignored on the small design-fluctuation scale $V_A/(D+1)$.

**Source pointers.** Watrous §3.1.1 for trace-distance foundations; [mixed-output correction and proof](../science/accuracy.md#4-mixed-conditional-states-and-a-sharp-purity-correction); [convex-roof attribution](../references/RELATED_WORK.md#finite-reference-metrology).

### M25 The exact measurement interpretation

**Central question.** Which established measurement class has the same attained reference cost?

**Understanding target.** Connect the weighted projective 2-design condition to tight rank-one informational completeness and to the local Fisher benchmark $J_{\mathrm H}(H)=\mathrm{Tr}(H^2)/[D(D+1)]$ at $I/D$. Explain how the frame trace fixes this normalization. Exact equality with the benchmark in every direction also forces rank-one normalized effects, even if rank one was not initially imposed.

**Dependencies and story role.** [M04](#m04-steering-and-the-effective-measurement), [M11](#m11-informational-completeness-and-fisher-geometry), [M21](#m21-the-attained-all-spectrum-optimum), [M24](#m24-mixed-outputs-and-the-purity-correction). This translates the ensemble optimum into an exact measurement capability.

**Conceptual connection.** The design/frame/Fisher equivalence is established geometry. The additional resource statement concerns implementing some measurement in that class with a conserving independent reference.

**Source pointers.** [Tight measurements and Fisher symmetry](../science/measurement_geometry.md#2-tight-rank-one-measurements-designs-and-fisher-symmetry); [rank-one implication](../science/measurement_geometry.md#6-why-exact-rank-one-matters); [Scott and Zhu-Hayashi attribution](../references/RELATED_WORK.md#state-designs-and-tomography).

### M26 Two-sided Fisher isotropy

**Central question.** Which approximate criterion retains a nearly matched dimension-dependent reference cost?

**Understanding target.** Within the class of exactly rank-one effective effects, require $(1-\varepsilon)J_{\mathrm H}\leq J\leq(1+\varepsilon)J_{\mathrm H}$ in every traceless direction, with $0\leq\varepsilon<1$. The charge direction gives $F_R\geq4V_A[(D+1)/(1+\varepsilon)-1]$. The construction with $K=\lceil(D+1)/(1+\varepsilon)\rceil$ satisfies the criterion with a gap below $4V_A$ for $V_A>0$; both costs vanish for scalar charge.

**Dependencies and story role.** [M15](#m15-the-mixed-reference-information-bound), [M21](#m21-the-attained-all-spectrum-optimum), [M25](#m25-the-exact-measurement-interpretation). This states the robust dimension-cost result with its exact output-rank premise.

**Conceptual connection.** The converse uses the upper Fisher inequality, which suppresses excess information in the charge direction. Integer construction points do not determine the entire continuous-budget optimum.

**Source pointers.** [Two-sided criterion, converse, and construction](../science/measurement_geometry.md#4-two-sided-relative-fisher-isotropy); [Fisher bridge](WATROUS_BRIDGE.md#fisher-isotropy-and-useful-information).

### M27 One-sided statistical usefulness

**Central question.** Must a measurement pay the isotropy cost to be informative in every local direction?

**Understanding target.** Use the finite-$K$ Fisher spectrum to satisfy only $J\geq(1-\varepsilon)J_{\mathrm H}$, for $0<\varepsilon<1$, at achievable cost below $4V_A/\varepsilon$ when $V_A>0$. Diagonal information can exceed the benchmark while off-diagonal information remains competitive. Approximate isotropy alone also fails to impose exact rank one, so the premise of M26 cannot be inferred from small statistical error.

**Dependencies and story role.** [M12](#m12-distance-purity-and-distinct-approximation-criteria), [M24](#m24-mixed-outputs-and-the-purity-correction), [M25](#m25-the-exact-measurement-interpretation), [M26](#m26-two-sided-fisher-isotropy). This establishes the practical boundary of the dimension-dependent interpretation.

**Conceptual connection.** Excess charge information is not intrinsically a statistical defect. The local Fisher comparison establishes neither a finite-sample estimator guarantee nor an optimal apparatus cost for arbitrary mixed-effect measurements.

**Source pointers.** [One-sided information guarantee](../science/measurement_geometry.md#5-a-one-sided-information-guarantee-is-much-cheaper); [approximate rank-one limitation](../science/measurement_geometry.md#6-why-exact-rank-one-matters).

### M28 Remote access and the meaning of the cost

**Central question.** Which physical restriction explains the large reference cost, and what does its scaling measure?

**Understanding target.** Compare the exact reference cost with the average output QFI, smaller by a factor $D+1$ for $V_A>0$. Direct control changes the supplied input: diagonal conserving Kraus operators can prepare the same ensemble from $|+_D\rangle$ at initial QFI $4V_A$. This is an explicit direct upper bound, not a proved direct optimum. For $m$ excitation qubits, the remote optimum is $m2^m$, with an attainable compressed reference on $m2^m+1$ charge levels.

**Dependencies and story role.** [M06](#m06-independent-references-and-resource-accounting), [M20](#m20-a-conserving-pointer-and-compressed-reference), [M21](#m21-the-attained-all-spectrum-optimum), [M27](#m27-one-sided-statistical-usefulness). This integrates operational access, resource normalization, and a physical scaling example.

**Conceptual connection.** Reference QFI is phase sensitivity, not a count of physical qubits, energy, or gates. The remote/direct comparison changes where initial coherence is supplied, while the fixed-error examples change the requested measurement capability.

**Source pointers.** [Output and implementation coherence](../science/interpretation.md#1-output-coherence-and-implementation-coherence); [direct-control construction](../science/interpretation.md#2-direct-control-changes-the-task); [excitation qubits](../science/interpretation.md#3-excitation-conserving-qubits).

### M29 Attribution and the strength of evidence

**Central question.** Which ingredients are established, and which combination produces the attained apparatus optimum?

**Understanding target.** Locate the quantum-information foundations, finite-reference QFI methods, HJW steering, conserving-effect feasibility, amplitude-phase designs, and tight-measurement geometry in their sources. Identify the constructive match of the complete design tensor to an independent charge-convolution reference as the step that attains the bound. Distinguish exact finite identities and numerical matrix checks from the general analytical proof.

**Dependencies and story role.** [M21](#m21-the-attained-all-spectrum-optimum), [M23](#m23-a-conserving-multiplicative-counterexample), [M24](#m24-mixed-outputs-and-the-purity-correction), [M27](#m27-one-sided-statistical-usefulness), [M28](#m28-remote-access-and-the-meaning-of-the-cost). This connects the complete result to the kind of evidence supporting each part.

**Conceptual connection.** A single educational anchor can support the learning route while multiple primary research sources remain necessary for attribution. Finite checks do not prove a universal theorem or establish that no other related result exists.

**Source pointers.** [Related work and attribution](../references/RELATED_WORK.md); [source versions and comparison limits](../references/RELATED_WORK.md#source-versions-and-limits-of-the-comparison); [verification guide](../verification/README.md); [targeted Watrous route](WATROUS_BRIDGE.md#targeted-reading).

### M30 The complete scientific story

**Central question.** What does the attained optimum teach about realizing a random pure-state ensemble under conservation?

**Understanding target.** Connect the independent-reference model, mixed-state QFI converse, exact-moment purity constraint, count-and-phase implementation, and neutral-pointer realization into the attained law $F_{Q,\min}=4DV_A$. Place additive moment error, the balanced multiplicative counterexample, impurity, two-sided rank-one Fisher isotropy, and one-sided information beside that law with their own conditions.

**Dependencies and story role.** [M13](#m13-the-complete-operational-question), [M21](#m21-the-attained-all-spectrum-optimum), [M27](#m27-one-sided-statistical-usefulness), [M28](#m28-remote-access-and-the-meaning-of-the-cost), [M29](#m29-attribution-and-the-strength-of-evidence). This integrates both phases into one explanation of what is necessary, what is attainable, and why the qualifications matter.

**Conceptual connection.** Interpret a change in physical access or target accuracy and identify the statement that still applies. Keep finite arbitrary real charges, the compact-group lattice condition, consumed references, optimized weighted designs, exact rank-one premises, and unoptimized implementation resources explicit.

**Source pointers.** [Model and exact optimum](../science/model.md); [scientific reading route](../science/README.md); [physical interpretation](../science/interpretation.md); [connecting the full story](WATROUS_BRIDGE.md#connecting-the-full-story).
