# Response to the referee: version 1.3 → version 1.4

*Christol's conjecture for non-resonant globally bounded ₃F₂(a₁,a₂,a₃;b,1) series* — David Jordan, 17 November 2026

I thank the referee for a careful and constructive report. The revision implements the requested corrections in the manuscript itself. It keeps the mathematical scope of v1.3: no new construction search was run and no new generalization was added, and every existing proof and computation is retained unless noted below. Section, lemma and page numbers refer to v1.4 (38 pp.). The companion files are `VERIFICATION_LOG.md` (what was rerun or checked, and what was not) and `DEPENDENCY_TABLE.md` (imported results, proved deductions, unresolved steps).

**Overall finding of the audit.** I did not find a gap in the proof of Theorem A. I did find several imprecise or overstated statements, all corrected:

- a lemma stated more generally than its source (Lemma 2.3);
- a citation to Deligne–Mumford whose hypothesis (an algebraically closed residue field) was not met as the argument was written (Prop. 6.2);
- a pin-cite to Artin 1969 for a statement that Artin does not make in that form (now Lemma 2.1, with a proof);
- an incorrect remark about cohomological conventions in the literature (§2.5);
- miscounts and overstatements in Appendix C.

None of these corrections changes a conclusion of the paper. Each step the referee questioned is now justified in the text; the justifications are summarized under points 2–4.

---

## 1. Appendix C

**Agreed and implemented.**

- **Code and counts rechecked.** I wrote an independent script (`audit/audit_exclusions.py`) that recomputes every count of the exact families from scratch. All counts in v1.3 were confirmed except one: v1.3 said that all 35,303 algebraic ψ are "irreducible and interlace". In fact 34,600 are algebraic by interlacing, and 703 are the trivial case ψ = (1−x)⁻¹. This is corrected.
- **New Lemma C.1 (transcendence criterion).** It gives a complete argument for every exclusion counted as excluded. It covers cancellation of equal parameters, removal of polynomial factors (R2), shifting an integral lower parameter to 1 by contiguity, and the case of two integral lower parameters (Levelt). The proof handles the polynomial-factor step by a monodromy-equivariance argument, because algebraicity is not preserved by inverting P(θ). The exclusions are broken down by the case of the lemma they need.
- **Three categories, used consistently.** The appendix now defines *excluded*, *unresolved* and *survivor*, says explicitly that exact arithmetic is not the same as a complete decision, and keeps these apart throughout. In particular:
  - family (ii): 31,495 factorizations excluded by Lemma C.1; 3,808 unresolved (evidence only); 1,457,968 reducible ψ not examined, together with the reason they are not excluded;
  - family (i): 25,266 excluded, 46 unresolved.
  The phrase "two families were treated exactly" has been removed.
- **Eisenstein evidence is not an obstruction.** I verified the referee's identity ₂F₁(½, 116/11; 105/11; x) = (1−x)^(−½) + (11/210)·x·(1−x)^(−3/2) exactly to order 120 (`scripts/eisenstein_counterexample.py`). It is now equation (C.1), because it shows concretely why three outside primes do not imply transcendence. The paper also notes that our classifier happens to decide this particular series correctly through step (R2). All Eisenstein-type cases are now called *unresolved*.
- **No complexity lower bound.** Every suggestion that the search supports a complexity lower bound for representations of H has been removed: from Appendix C, the introduction, related work, Remark 8.4(5), concluding remark (1) and the plain-language summary. The appendix now says explicitly that the search gives no such bound.
- **Numerical families.** The handling of d₁ ≡ 0 (mod p) is now documented and justified. The bound |d₁|·den(d₁) ≤ 39,680,928 < p, eq. (C.3), holds in all five families, so d₁ ≡ 0 (mod p) only if d₁ = 0, which cannot occur for a true representation. Hence every discarded candidate is excluded, *provided the code computes the coefficients correctly*; this proviso is stated in the text. Survivors (312) are described as passing a 50-coefficient check and are not claimed as certified identities.

## 2. Section 4, the weight-one argument

**Agreed and implemented.** The proof of Theorem 4.3 is now organized in eight explicit steps, matching the referee's list:

1. the integral local system and the complex decomposition (4.1)–(4.2), derived from the isomorphism K⊗ℚℂ ≅ ℂ^φ(N);
2. conjugation compatibility: formula (4.3), (X̄)ₖ = conj(X₋ₖ), is derived, and the relations (4.4) between the Hodge pieces of 𝒮ₖ and 𝒮₋ₖ are stated as the only constraint between gradings;
3. holomorphicity of F¹;
4. V_ℂ = F¹ ⊕ F̄¹;
5. alternation, invariance and nondegeneracy of the trace form, including an explicit derivation of its complex bilinear extension (4.5);
6. isotropy of F¹;
7. positivity: signs εₖ, ε₋ₖ = −εₖ, and weak approximation over the real places of K⁺, with the bijection Φ ↔ real places made explicit;
8. integrality.

The new Remark 4.4 separates a shift of the grading of a single complex variation, which changes the sign of its polarization, from the Tate twist V(1) = V ⊗ 2πiℤ, which shifts all conjugates at once. §2.5 and §5 now use the Tate twist only to reach the type of Deligne's theorem.

**Conventions.** v1.3 claimed that the literature also states Deligne's equivalence cohomologically. Both sources I checked (Deligne, Hodge II 4.4.3; Milne, Thm 7.13) are homological, so the remark is replaced. Throughout, R₁f_* denotes homology, R¹f_* = (R₁f_*)^∨ cohomology, and periods pair R₁f_* with H¹_dR. The attribution of essential surjectivity to Borel (in Deligne) is restored.

**Fedorov.** The theorem allows repeated entries; it assumes only weakly increasing sequences with αᵢ ≠ βⱼ. The text now says so and introduces no distinctness assumption. I re-read Fedorov (arXiv:1505.01704). The v1.3 citation of Dettweiler–Sabbah Thm 2.4.1 for existence is correct as Fedorov gives it; his alternative inductive argument uses their Prop. 3.1.1, and both are now mentioned. I had planned to change this citation and withdrew the change after re-reading the source.

I also added a check that the two-level criterion does not depend on how L is matched to Fedorov's normal form (the swap α ↔ β, i.e. x ↦ 1/x); see the remark after Prop. 3.1.

## 3. Proposition 5.4 (formerly 5.3)

**Agreed and implemented.** New Lemma 5.3 proves the following for regular-singular connections on U over a number field:

- (a) Hom_𝒟(M, E) is finite-dimensional and compatible with extension of constants (affine base, flat base change, horizontal sections determined at a point);
- (b) full faithfulness of Riemann–Hilbert (Deligne LNM 163, II.5.9).

The proof of Prop. 5.4 now tracks the duals explicitly: M_L^∇ = 𝒮^∨, E^∇ = R¹f_*ℂ = (R₁f_*ℂ)^∨, so Hom ≅ Hom(R₁f_*ℂ, 𝒮). It also checks that this isomorphism is ω ↦ (γ ↦ ∫_γ ω). This gives existence of a nonzero ω over K₀ itself, with no further field extension, and surjectivity by irreducibility. The text states that ω is an **algebraic de Rham class, not necessarily a holomorphic relative differential**. After Prop. 5.1 it states that specialization preserves the local system but not necessarily the Hodge filtration, which is not used.

## 4. Sections 6–7, consolidation

**Agreed and implemented.**

- **New Proposition 7.3 (from vanishing-cycle periods to diagonals).** It collects, with explicit hypotheses, the whole mechanism the referee listed: number field, ramified base change, regular model with reduced nodal special fibre, horizontal and vertical poles, monodromy variation, node expansion, descent of the coefficient field, removal of the monomial shift, and extraction of a section. §7.1 (proof of Theorem A) now only checks its hypotheses. The paper says explicitly that it does **not** assert that algebraic periods are diagonals in general.
- **Chain quasi-unipotent → semistable Jacobian → stable curve → regular model (Prop. 6.2, Steps 1–4).** This chain is redone over R = ℚ̄[w]₍w₎, whose residue field is algebraically closed as Deligne–Mumford Thm 2.4 requires. It then descends to a number field by limit arguments, resolves the A_{e−1} points explicitly, spreads out, and removes the non-regular locus. Statement (iii) now records the completed local ring K₁[[û, v̂]] with w = ûv̂ at each node.
- **Meromorphic representative (Lemma 6.4).** The class is represented by a Čech–de Rham triple on two affine opens. The generic equality extends to W° because H¹_dR of the smooth projective family is locally free (argument included). Residues at horizontal poles vanish because ϖ = ϖ′ + dφ near D; hence small loops around D contribute nothing and periods depend only on homology classes.
- **Node coordinates (new Lemma 6.5).** Instead of the formal Morse lemma, which is no longer needed, the lemma uses the completed local ring from Prop. 6.2(iii) and Artin approximation (Thm 1.10, hypotheses stated) to obtain u, v ∈ 𝒪ʰ with uv = w. It identifies 𝒪ʰ with the algebraic power series ring (new Lemma 2.1, proved via Artin 1.10 and a Newton–Hensel uniqueness argument), and shows that u, v are holomorphic coordinates.
- **Dualizing sheaf at a node (Prop. 7.1).** du/u is justified as a local generator via an étale chart to the relative complete intersection uv = w.

## 5. Primary sources

**Implemented, with one partial exception.** The following were compared with the cited sources: Fedorov (arXiv:1505.01704), Deligne Hodge II 4.4.3, Milne Thm 7.13 (arXiv:1105.0887v1), Deligne–Mumford Thm 2.4, Artin Thm 1.10, Harder–Kramer-Miller (IMRN 2026, rnag040) and Rivoal–Roques (JNT 2014). As a result:

- **Lemma 2.3 is narrowed** to D-finite series over a number field, as Harder–Kramer-Miller state it. The paper explains the Denef–Lipshitz map behind it, where it is used (K = ℚ; n = 1 and n = 2), and why it gives three rational variables. It keeps the separate lower-bound argument (Pólya–Furstenberg plus transcendence).
- **Corollary E** still states its dependence on Rohrlich–Lang explicitly.
- **Priority of Prop. D** is worded cautiously: "elementary identities, which may well be known to specialists, although we have not found them in print". The introduction says Theorem A is the principal contribution and Prop. D is elementary.
- **No announcements** are used as evidence.
- **New Table 3** (Appendix B) lists every imported result and where it is used.

**Partial:** I could not recheck the following against the originals in this revision: Deligne LNM 163 (II.5.9), Katz 1970, SGA 7 I Exp. IX §3, SGA 7 II Exp. XIV, Liu §§6.4 and 10.3, and the original Beukers–Heckman and Christol 1987 papers. To avoid citing numbers I have not verified, the paper cites sections rather than theorem numbers where I could not confirm them. These references are listed as *not rechecked* in the verification log.

## 6. Title, summary, citations, distinctions

**Agreed:**

- **Title** is now exactly the referee's preferred title.
- **Citations** are numbered (`natbib` with `numbers,sort&compress`, plainnat). Citations inside theorem headers were converted so that they print correctly in numeric style.
- **"Right dimension"** is replaced by an explicit matching condition: the number of logarithms must match the dimension of the family.
- **The four kinds of result are kept distinct** throughout: non-constructive existence; explicit algebraic diagonal; explicit rational diagonal; proved minimal number of variables. A new paragraph in §1.4 says this, and Remark 8.4(4) separates explicit algebraic from explicit rational representations for Prop. D.

**Partly implemented:** the plain-language summary is shortened by about half, but it stays after the abstract. The author asked for this summary specifically, and placing it after the abstract is common in interdisciplinary venues. It can be moved to the end at the editor's request.

## 7. Verification

**Implemented.** All scripts were rerun with Python 3.13.18 and NumPy 2.5.3; commands, runtimes and outputs are in Appendix B and `VERIFICATION_LOG.md`. `run_checks.sh` runs everything and exits non-zero on any discrepancy; the audit scripts now compare their results with the numbers printed in the paper. The numerical families A2 and A4 were recomputed from scratch, and their survivors are identical to the stored output (63 survivors). A3, B2 and B3 (about 922 million candidates, several hours) were not recomputed; their stored output was re-examined. The Prop. D all-order proofs were re-read; they are algebraic identities, and the scripts only illustrate them. No files were missing. One stale docstring in `search/family_ab.py`, which disagreed with the code and with Table 4, was corrected; the code itself was not changed.

## Deliverables

- `christol_w1.tex`, `christol_w1.bib`, `christol_w1.bbl`, `christol_w1.pdf` (v1.4)
- this response
- `VERIFICATION_LOG.md`
- `DEPENDENCY_TABLE.md`
- `supplementary/` with `run_checks.sh` and `SHA256SUMS`
- portable archive `Christol_3F2_Diagonals_Paper_v1_4.zip`

*Acknowledgment.* If the referee agrees, the author would like to acknowledge the referee for the example (C.1).
