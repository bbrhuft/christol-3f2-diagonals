# Version 1.5: change log and response to the review of version 1.4

*Christol's conjecture for non-resonant globally bounded ₃F₂(a₁,a₂,a₃;b,1) series* — David Jordan, 17 November 2026

**Provenance.** The comments addressed here, and those addressed in version 1.4, come from AI-assisted manuscript reviews. They are not independent journal peer review, and the paper has not been refereed. This revision was bounded as requested:

- the central geometric proof and the scope of Theorem A are unchanged;
- no construction search was started;
- the large B2/B3 searches were not rerun.

**Effect on Theorem A.** None of the changes below affects the proof of Theorem A:

- Items 1, 2 and 5 concern the computer search and the verification scripts, which are not part of the proof.
- Item 3 corrects notation in the proof of Lemma 2.1(ii); the lemma and its conclusion stand.
- Item 6 confirms two citations used in Lemma 5.3 and Proposition 5.4.

No new mathematical gap was found. These corrections do not certify Theorem A, and the audit is still not a substitute for verification by an independent specialist.

---

## 1. B2/B3 search coverage — confirmed and corrected (bounded remedy)

**Finding confirmed.** `family_ab.py` replaced each quadratic factor *separately* by the lexicographic minimum of its coefficient vector and that of its image under u ↔ v. The regression test checks the example exactly and with the search engine:

- 1/((1−u)(1−2v)) has diagonal 1/(1−2x);
- the individually canonicalized factors 1−u and 1−2u give diagonal 1;
- the pair {1−u, 1−2v} is not enumerated, even up to the simultaneous exchange u ↔ v.

**Remedy (as instructed).** The enumeration and all stored counts are unchanged. The paper now describes the pools actually enumerated:

| | Described set | Pool enumerated | Factor sets enumerated | Coverage of described family modulo simultaneous u ↔ v |
|---|---|---|---|---|
| B2 | 1,619 quadratics | P₂: 854, all in the set | 364,231 pairs | 364,231 of 657,226 classes of pairs |
| B3 | 95 quadratics | P₃: 77, of which 30 contain v² and are not in the set | 73,150 triples | 45,070 of 130,489 classes of triples; a further 28,080 triples lie outside the described family |

Candidate counts are unchanged: B2 has 472,043,376 and B3 has 426,610,800.

The paper now states:

- no representation of H was found **among the candidates actually enumerated**;
- families A are complete as described, because their reduction acts simultaneously on all factors;
- B2 and B3 are complete only within the explicit pools.

These changes appear in Appendix C (new description of the pools, Table 4 and its caption, a results paragraph naming (1−u)^α(1−2v)^β as untested) and in the other statements about scope: §1.2, Related work, Remark 8.4(5), concluding remarks (1) and (5), and Appendix B.

**Code.**

- `family_ab.py`:
  - the docstring and comments now distinguish `representative2` (choosing a representative for each factor, which restricts the pool) from `canon_collection2` and `canon3` (simultaneous canonicalization, a genuine symmetry reduction);
  - `b2_pool()` and `b3_pool()` reproduce the original pools;
  - the `__main__` block and `run_b2.py` call these functions in place of their original inline pool expressions, which `test_symmetry.py` confirms are identical.
- New `search/test_symmetry.py` (regression test, 25 checks).
- New `search/list_pools.py` and `search/pools_B2_B3.json` (explicit pools).
- Search README rewritten.
- Docstrings corrected.

## 2. Verification now enforces its stated checks — implemented

- **`search/test_engine.py`** fails with a nonzero exit status if the positive control does not match, or if the deliberate negative control does match.
- **`audit/audit_numerical.py`**:
  - the default run is labelled as inspecting **stored survivor records**; its 50-coefficient comparisons are not recomputed, and the console says so;
  - the counts and the bound (C.3) are recomputed;
  - a separately selectable routine, `--recompute-survivors` (about 8 minutes, not in the default), recomputes all 312 comparisons. I ran it: 312 of 312 agree. The manuscript (Appendix C and B) states which kind of check each command performs.
- **`run_checks.sh`** uses explicit failure handling: the first failed expectation stops the run with status 1.
- **New `audit/check_failure_propagation.sh`** (run inside the default command) copies the supplementary folder to a temporary directory, injects one failed expectation at a time **into the copy only**, and requires `run_checks.sh --quick` to fail. It also requires an unmodified copy to pass. All six cases behaved as expected:
  1. unmodified copy (passes);
  2. broken positive control;
  3. negative control made to match;
  4. altered stored reference output;
  5. altered expected pool size;
  6. altered expected candidate total.

  The stored reference outputs are byte-identical to v1.4.
- **New single default command `sh verify_all.sh`** at the package root. It checks SHA-256 checksums, then runs `run_checks.sh`.

## 3. Lemma 2.1(ii) — corrected (notation, not a failure of the lemma)

The identification of 𝒪̂ ⊗_F ℂ with ℂ[[u₁,…,uₙ]] has been removed. The proof now uses the natural coefficientwise map ι: F[[u]] → ℂ[[u]]. Two local homomorphisms from the local ring of an étale neighbourhood into ℂ[[u]] are shown to agree: the Taylor expansion of holomorphic germs, and ι composed with completion. Both extend continuously to 𝒪̂ and agree on the dense subring F[u]. The conclusions are unchanged: elements of 𝒪ʰ are holomorphic germs whose Taylor series is their image under ι, and algebraic power series converge. The statement of (ii), and Lemma 6.5(ii), now say "regarded in ℂ[[u]] via the coefficientwise inclusion".

## 4. Plain-language definition of a diagonal — corrected

The summary now says: keep the coefficient of u₁ⁿ⋯u_dⁿ and use it as the coefficient of xⁿ. This agrees with the formal definition in §1.1.

## 5. Precision corrections — implemented

- **Eisenstein.** The paper now states that an algebraic power series over ℚ has only finitely many *distinct* denominator primes, and that a fixed prime may divide infinitely many denominators. The `hyp.py` docstring was corrected to match; the code itself is unchanged.
- **Sixteen targets.** They are now specified as the grid {1/9, …, 8/9}, with a₁ ≤ a₂ ≤ a₃, repetitions allowed, non-resonant and globally bounded (`gb_targets()`). This wording is used in Appendix C, concluding remark (5) and the search README.
- **Cross-reference.** §8.1(vi) now refers to "the sign conditions (4.8) of Step 7"; the numbering was checked in the compiled PDF.
- **Provenance.** The AI statement now describes the earlier exchanges as AI-assisted manuscript reviews, not independent peer review. It credits those reviews with the example (C.1) and with identifying the B2/B3 pool restriction; this is the only acknowledgment of the example. The v1.4 response document, titled "Response to the referee", is not carried into the v1.5 package; the README explains where it is and what it was.

## 6. Source check of Deligne, LNM 163 — done by me, recorded separately

I read the uploaded scan (`Number9.pdf`, 136 pp., IAS publications) myself, using the page images for the three key pages and the OCR text for the rest:

- **Théorème II.5.9** (book p. 97, PDF p. 100). On a smooth complex algebraic variety, analytification is an equivalence between algebraic vector bundles with regular integrable connection and holomorphic vector bundles with integrable connection. Full faithfulness is proved explicitly there.
- **Théorème I.2.17** (pp. 12–13). Holomorphic integrable connections are equivalent to local systems, via horizontal sections.
- **Définition II.4.5 and Proposition II.4.4** (pp. 89–90): regularity.
- **Théorème II.7.9** (p. 118, PDF p. 121). For f smooth, between smooth schemes of finite type over ℂ and satisfying (i)–(iii) of Théorème II.6.13, and for V a regular integrable connection on the source, the Gauss–Manin connection on Rⁱf_*(Ω•_{X/S}(V)) is regular.
- **Proposition II.6.14** (pp. 106–107). Properness plus smoothness, with empty boundary divisor, gives the conclusions of II.6.13.

**Applicability confirmed.**

- Lemma 5.3(b) uses II.5.9 together with I.2.17 on U_ℂ, and regularity is now defined via II.4.5 after base change to ℂ.
- Proposition 5.4 uses II.7.9 with V = (𝒪_𝒜, d) for the proper smooth abelian scheme; its hypotheses hold by II.6.14.

The manuscript now cites these exact numbers, and Table 3 was split accordingly. The verification log records these as **my own checks for v1.5**, kept separate from checks reported by the external AI-assisted review. Katz 1970, SGA 7, Liu, the original Beukers–Heckman and Christol papers, and Denef–Lipshitz (checked only as quoted by HKM) remain marked as not rechecked.

## 7. Verification and packaging

`sh verify_all.sh` passes. `run_checks.sh` took 4 min 37 s on the final files. Failure injection confirms that failed expectations produce a nonzero exit status. The symmetry counterexample is handled by `test_symmetry.py`. Stored-result inspections are labelled as such, and the manuscript's counts describe the enumeration actually performed.

The manuscript is now 39 pages. It compiles with no LaTeX warnings and no overfull boxes; citations and cross-references were checked in the PDF. Versions 1.3 and 1.4 are preserved unchanged.

## Files changed

**Manuscript:**

- `christol_w1.tex`, and the rebuilt `christol_w1.bbl` and `christol_w1.pdf`;
- `christol_w1.bib` is unchanged (Deligne1970 already present).

**Supplementary:**

- **changed:** `run_checks.sh`, `audit/audit_numerical.py`, `search/family_ab.py`, `search/run_b2.py`, `search/test_engine.py`, `search/hyp.py` (docstring only), `search/README.md`;
- **new:** `audit/check_failure_propagation.sh`, `search/test_symmetry.py`, `search/list_pools.py`, `search/pools_B2_B3.json`.

**Package root:**

- **new:** `verify_all.sh`, this file;
- **updated:** `VERIFICATION_LOG.md`, `DEPENDENCY_TABLE.md`, `NOTES_FOR_AUTHOR.md`, `README.md`, `SHA256SUMS`.
