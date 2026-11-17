# Dependency table for Theorem A (version 1.5)

**Theorem A.** If (a,b) is non-resonant and F = ₃F₂(a;b,1;x) is globally bounded, then F = Diag(g) for some g ∈ ℚ⟨u,v⟩ (algebraic). Hence F is the diagonal of a rational function in three variables, and of none in fewer.

Status codes:

- **I** = imported from the literature (source in the last column);
- **P** = proved in the paper;
- **C** = computation (only for examples, never for the general proof);
- **U** = unresolved.

"Checked (v1.4)" or "checked (v1.5)" means the cited statement was compared with the source by me during that revision. "Not rechecked" means it was cited but not compared again. The full list, with versions consulted, is in VERIFICATION_LOG.md. Checks reported in the external AI-assisted reviews are recorded there separately and are not counted here.

**Version 1.5 changes and the proof.** No change in v1.5 affects the proof of Theorem A. The proof of Lemma 2.1(ii) was corrected in notation only, by replacing a tensor-product identification with the coefficientwise map F[[u]] → ℂ[[u]]; the lemma and its use in Lemma 6.5 are unchanged. The Deligne citations for I6 and I7 were confirmed against the source. The search corrections (section D) concern material outside the proof.

## A. Imported results

| # | Result | Where used | Source | Checked? |
|---|---|---|---|---|
| I1 | Irreducibility of hypergeometric local systems; Levelt's companion-matrix form; finiteness iff interlacing | Lemma 2.5, Lemma C.1, Cor. C | Beukers–Heckman 1989, Prop. 3.3, Thm 3.5, Thm 4.8 | not rechecked (original); statements standard |
| I2 | Christol's criterion for global boundedness | Lemma 2.7, Prop. 3.1 | Christol 1987, Props 1, 1bis; Fürnsinn–Yurkevich 2024 | not rechecked |
| I3 | Existence and uniqueness (up to shift) of the complex VHS, and Hodge numbers ρ(k) = #{j: αⱼ < βₖ} − k; repeated entries allowed | Prop. 3.1 | Fedorov 2018, Prop. 2.6, Thm 1 (§1 hypotheses) | **checked (v1.4)** (arXiv:1505.01704) |
| I4 | Abelian schemes ⇔ polarizable ℤ-VHS of type {(−1,0),(0,−1)}, homological convention | Prop. 5.1 | Deligne 1971, 4.4.3; Milne 2013, Thm 7.13 | **checked (v1.4)** |
| I5 | Limit theorems (spreading out, descent) | Props 5.1, 6.2 | EGA IV₃ §8, IV₄ §17 | standard; not rechecked |
| I6a | Regularity of the Gauss–Manin connection on H¹_dR of the proper smooth abelian scheme | Prop. 5.4 | Deligne LNM 163, Thm II.7.9, with hypotheses supplied by Prop. II.6.14 (empty boundary divisor) and V = (𝒪, d) | **checked (v1.5)** (IAS scan, book pp. 106–107, 118) |
| I6b | Quasi-unipotence of local monodromy | Prop. 6.2 | Katz 1970 | not rechecked |
| I7 | Riemann–Hilbert for regular-singular connections (full faithfulness) | Lemma 5.3(b) | Deligne LNM 163, Thm II.5.9 (analytification), Thm I.2.17 (horizontal sections), Def. II.4.5 (regularity) | **checked (v1.5)** (book pp. 12–13, 89–90, 97) |
| I8 | Bertini over an infinite field; Lefschetz hyperplane theorem | Prop. 6.1 | Jouanolou 1983 §6; Lazarsfeld 2004 §3.1 | not rechecked |
| I9 | Grothendieck's semistable-reduction criterion; ℓ-adic/topological comparison of monodromy | Prop. 6.2, Step 1 | SGA 7 I, Exp. IX §3; SGA 7 II, Exp. XIV | not rechecked |
| I10 | Stable reduction of the curve from semi-abelian reduction of its Jacobian (residue field algebraically closed) | Prop. 6.2, Step 1 | Deligne–Mumford 1969, Thm 2.4 | **checked (v1.4)** (hypothesis on residue field respected) |
| I11 | Local structure of split nodes on a model; minimal resolution of A_{e−1} | Prop. 6.2, Steps 2–3 | Deligne–Mumford 1969 §1; Liu 2002 §10.3 | not rechecked (section-level citation) |
| I12 | Relative dualizing sheaf of an l.c.i. morphism; generator du/u for uv = w | Lemma 6.4, Prop. 7.1 | Liu 2002 §6.4; DM §1 | not rechecked (section-level citation) |
| I13 | Algebraic de Rham cohomology of affine smooth varieties is computed by global forms | Lemma 6.4 | Grothendieck 1966 | standard; not rechecked |
| I14 | Artin approximation for henselizations of local rings of finite type over a field | Lemmas 2.1, 6.5 | Artin 1969, Thm 1.10 | **checked (v1.4)** |
| I15 | Diagonals of algebraic series in n+1 variables = diagonals of rational functions in n+2 variables (number field, D-finite) | §7.1 (upper bound 3) | Harder–Kramer-Miller 2026, Lemma 3.2 (via Denef–Lipshitz 1987, Thm 6.2, Rem. 6.4) | **checked (v1.4)** (HKM journal version); DL only as quoted by HKM |
| I16 | Two-variable rational diagonals are algebraic, and conversely | §7.1 (lower bound 3) | Pólya 1922; Furstenberg 1967 | standard |

## B. Deductions proved in the paper (chain of Theorem A)

| Step | Statement | Status | Inputs |
|---|---|---|---|
| 1 | GB ⇔ every conjugate has two adjacent Hodge levels | P | I2, I3, Lemma 2.5 (I1) |
| 2 | Invariant hermitian form h over K, unique up to K⁺ˣ | P (Lemma 4.2) | Step 1, I1 |
| 3 | Polarized ℤ-VHS of type {(1,0),(0,1)} on Res Λ: eight explicit steps (decomposition, conjugation, holomorphicity, V = F¹ ⊕ F̄¹, trace form, isotropy, positivity via weak approximation, integrality) | P (Thm 4.3) | Steps 1–2 |
| 4 | Abelian scheme over a number field K₀ with R₁f_*ℚ ≅ V_ℚ (local system only) | P (Prop. 5.1) | Step 3, I4, I5 |
| 5 | Finite-dimensionality and descent of Hom_𝒟(M,E) for regular-singular connections | P (Lemma 5.3) | I7 |
| 6 | Nonzero algebraic de Rham class ω over K₀ with L·ω = 0, and surjective period map R₁f_*ℂ → 𝒮 | P (Prop. 5.4) | Steps 4–5, I6, Lemma 2.5 |
| 7 | F = (2πi m)⁻¹ ∫ over (T₀ᵐ − 1)γ_Y of ω | P (Cor. 5.5) | Step 6, Lemma 2.6 |
| 8 | Family of curves C → U₁ with ι_* surjective on H₁ | P (Prop. 6.1) | I8 |
| 9 | Regular model 𝒳 → W over a number field, reduced nodal special fibre, Ô = K₁[[û,v̂]], w = ûv̂ at the nodes | P (Prop. 6.2) | I5, I6, I9, I10, I11 |
| 10 | Meromorphic representative ϖ with horizontal and vertical poles, zero residues, periods compatible with ι | P (Lemma 6.4) | Step 9, I12, I13 |
| 11 | 𝒪ʰ = algebraic power series ring; holomorphic coordinates u, v with uv = w (notation in Lemma 2.1(ii) corrected in v1.5) | P (Lemmas 2.1, 6.5) | I14, Step 9 |
| 12 | (T − 1)H₁ ⊂ span of vanishing cycles | P (Lemma 6.6) | Step 11 (topology) |
| 13 | Node expansion: ∫ over δⱼ of ϖ = 2πi·w^(−νⱼ)·Diag(gⱼ), with gⱼ ∈ K₁⟨u,v⟩ | P (Prop. 7.1) | Steps 10–11, I12 |
| 14 | Mechanism: descent of the coefficient field, removal of the monomial shift, extraction of the section ⇒ F = Diag(g), g ∈ ℚ⟨u,v⟩ | P (Prop. 7.3, Lemma 2.2) | Steps 12–13 |
| 15 | Assembly: lifting γ_Y to 𝒳, compatibility ι_*T_𝒳 = T₀ᵐι_* | P (§7.1) | Steps 7–14 |
| 16 | Three rational variables suffice | P (§7.1) | Step 15, I15 (K = ℚ, n = 1; F is D-finite) |
| 17 | Fewer than three do not | P (§7.1) | Lemma 2.6(iv), I16 |

## C. Unresolved steps

None found in the proof of Theorem A. The 2026 audit found and corrected the following imprecisions, none of which changes a conclusion:

- a lemma stated more generally than its source (now Lemma 2.3);
- the DM residue-field hypothesis, now respected by working over ℚ̄ and descending;
- a pin-cite to Artin 1969 for the henselization statement, replaced by a proof (Lemma 2.1);
- an incorrect remark about conventions (§2.5).

**Residual risks** (not gaps, but limits of this check):

1. The references marked *not rechecked* above were not compared with the originals by me.
2. The proof has not been checked by an independent specialist in Hodge theory or arithmetic geometry.
3. The scripts check examples (Christol's H, controls, Appendix A); they do not verify the general proof.

**Dependent statements.**

- Corollary B is Theorem A plus the checks in §8.1 and Example 8.2.
- Corollary C is Theorem A plus I1, I2 and I15 (n = 2).
- Corollary E is Theorem A plus Rivoal–Roques, Prop. 1, and is **conditional on the Rohrlich–Lang conjecture**.
- Proposition D is proved independently of Theorem A by elementary identities.

## D. Computational material (not part of the proof of Theorem A)

| Item | Status after v1.5 |
|---|---|
| Christol's H, §8.1 (i)–(vi); Appendix A Hodge-number check; Prop. D identities (illustrations) | rerun, pass (`verify.py --full`, `hadamard_identities.py`) |
| Appendix C exact families (Lemma C.1 exclusions, unresolved and not-examined cases) | recomputed, pass (`audit_exclusions.py`) |
| Numerical families A2, A3, A4 | complete as described, up to simultaneous permutation of variables; A2 and A4 recomputed (v1.4); A3 stored only |
| Numerical families B2, B3 | **corrected in v1.5**: only the restricted pools P₂ (854) and P₃ (77) were enumerated; complete within the pools, not in the families first described; not recomputed |
| 312 survivors, 50-coefficient comparisons | stored records inspected by default; recomputed once for v1.5 with the optional routine (312/312 agree) |
| Verification scripts | enforce their expectations; failure propagation tested by injection on temporary copies |

These computations concern examples and the search for explicit representations. They do not verify the general proof, and the v1.5 corrections do not certify Theorem A.
