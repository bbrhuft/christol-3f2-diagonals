# Verification log, version 1.5

17 November 2026. This log records what was rerun or checked for version 1.5, and what was not.

**Provenance.** The comments that led to versions 1.4 and 1.5 came from AI-assisted manuscript reviews, not from independent journal peer review. Checks reported by those reviews are listed separately in section 6 and are not counted as checks made for this revision.

## 1. Environment

- Python 3.13.18 (standard library only for `scripts/`).
- NumPy 2.5.3 (for `search/` and the search audits).
- pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), bibtex, latexmk 4.83.

## 2. Default verification command: completed

From the package root, `sh verify_all.sh` checks `SHA256SUMS` and then runs `supplementary/run_checks.sh`. The full output of `run_checks.sh` on the final v1.5 files is reproduced below (exit status 0, wall time 4 min 37 s). The run of `verify_all.sh` on the packaged copy is recorded in section 4.

```
== python version
Python 3.13.18
== scripts/verify.py --full
PASS: Section 8.1 (i)-(vi): monodromy, hermitian form, signatures, Gram determinant 3^36
PASS: Appendix A: Hodge numbers for H, three controls and 9,086 parameter sets
PASS: Remark 7.2, Proposition D (order 60), closed form of rho in Proposition 3.1
PASS: Appendix A, full scan: 38,164 parameter sets, 221,946 conjugate cases
ALL CHECKS PASSED
== scripts/hadamard_identities.py
all identities hold to n = 200 : True
3F2(1/9,4/9,7/9;1/3,1) = T_1/3 * (1-x)^(-2/3)
3F2(1/9,4/9,7/9;2/3,1) = T_1/3 * (1-x)^(-1/3)
3F2(2/9,5/9,8/9;2/3,1) = T_2/3 * (1-x)^(-1/3)
3F2(2/9,5/9,8/9;1/3,1) = T_2/3 * (1-x)^(-2/3)
== scripts/eisenstein_counterexample.py
identity holds to order 120 : True
first coefficient: 58/105
classifier verdict: algebraic (BH, poly)
outside primes in denominators up to n = 80: [3, 5, 7] ...
== search/test_engine.py
PASS: positive control: coefficients equal 3F2(1/9,4/9,7/9;1/3,1;27x) to order 8
PASS: positive control: invariants match the target
PASS: negative control: invariants do not match the target
ENGINE TEST PASSED
== search/test_symmetry.py
PASS: exact: Diag 1/((1-u)(1-2v)) = 1/(1-2x)
PASS: exact: Diag 1/((1-u)(1-2u)) = 1
PASS: engine: Diag (1-u)^-1 (1-2v)^-1 = 2^n mod p
PASS: engine: Diag (1-u)^-1 (1-2u)^-1 = 1
PASS: individual representatives change the product: representative2(1-2v) = 1-2u
PASS: simultaneous canonicalization preserves the diagonal
PASS: b2_pool() equals the pool of the original run
PASS: b3_pool() equals the pool of the original run
PASS: the pair {1-u, 1-2v} is not enumerated in B2, even up to simultaneous u<->v
PASS: stored pools_B2_B3.json agrees with the pools
PASS: both factors 1-u and 1-2v belong to the originally described B2 polynomials
PASS: B2 described polynomials: 1619 (expected 1619)
PASS: B2 pool: 854 (expected 854)
PASS: B2 pairs enumerated: 364231 (expected 364231)
PASS: B2 classes of described pairs: 657226 (expected 657226)
PASS: B2 classes hit: 364231 (expected 364231)
PASS: B3 described polynomials: 95 (expected 95)
PASS: B3 pool: 77 (expected 77)
PASS: B3 pool outside described set: 30 (expected 30)
PASS: B3 triples enumerated: 73150 (expected 73150)
PASS: B3 classes of described triples: 130489 (expected 130489)
PASS: B3 classes hit: 45070 (expected 45070)
PASS: B3 enumerated outside described family: 28080 (expected 28080)
PASS: candidate counts: B2 = 364,231 x 36^2, B3 = 73,150 x 18^3
ALL SYMMETRY CHECKS PASSED
== audit/audit_numerical.py (stored survivor records; bound and counts recomputed)
factor sets enumerated: {'A2': 391, 'A3': 500, 'A4': 10, 'B2': 364231, 'B3': 73150} (B2, B3: from the restricted pools)
candidates enumerated: {'A2': 1140156, 'A3': 23328000, 'A4': 1049760, 'B2': 472043376, 'B3': 426610800} total 924172092
A2: |d_1| <= 9072, den | 4374, |numerator| <= 39680928 < p: True
A3: |d_1| <= 2688, den | 4374, |numerator| <= 11757312 < p: True
A4: |d_1| <= 120, den | 4374, |numerator| <= 524880 < p: True
B2: |d_1| <= 328, den | 162, |numerator| <= 53136 < p: True
B3: |d_1| <= 195, den | 162, |numerator| <= 31590 < p: True
stored survivor records: 312 ; stored flags verified_to_50_mod_P2 all true: True (stored records from the original run; comparisons not recomputed unless --recompute-survivors)
   ('A2', '3F2(1/9,4/9,7/9;1/3,1)') 18
   ('A2', '3F2(1/9,4/9,7/9;2/3,1)') 9
   ('A2', '3F2(2/9,5/9,8/9;2/3,1)') 18
   ('A2', 'control 2F1(1/6,2/3;1)') 18
   ('A3', '3F2(1/9,4/9,7/9;1/3,1)') 8
   ('A3', '3F2(2/9,5/9,8/9;1/3,1)') 4
   ('A3', '3F2(2/9,5/9,8/9;2/3,1)') 8
   ('A3', 'control 2F1(1/6,2/3;1)') 16
   ('B2', 'control 2F1(1/6,2/3;1)') 109
   ('B3', 'control 2F1(1/6,2/3;1)') 104
statements of Appendix C confirmed: True (survivor comparisons: stored records only)
== audit/audit_exclusions.py
family (i): {'not algebraic (BH)': 25266, 'not algebraic (Eis)': 46} subtypes of BH exclusions: {'P0': 25221, 'P1': 43, 'P2': 2}
family (ii) psi: {'algebraic (BH)': 34600, 'algebraic (rational)': 703, 'skip': 1457968, 'not algebraic (BH)': 4149117} subtypes of psi exclusions: {'P0': 3658432, 'P3': 472957, 'P2': 17728}
family (ii) phi: {'not algebraic (BH)': 31495, 'not algebraic (Eis)': 3808} subtypes of phi exclusions: {'P0': 28783, 'P3': 703, 'P1': 2009}
counts agree with Appendix C: True
== audit/rerun_numerical_A2_A4.py
A2: 1140156 candidates, 63 survivors
A4: 1049760 candidates, 0 survivors
survivors identical to stored output: True (63 new, 63 stored)
== audit/check_failure_propagation.sh
PASS: unmodified copy -> run_checks.sh --quick passed as expected
PASS: positive control of search/test_engine.py broken -> run_checks.sh --quick failed as expected
        == FAILED: search/test_engine.py (exit status 1)
PASS: negative control of search/test_engine.py made to match -> run_checks.sh --quick failed as expected
        == FAILED: search/test_engine.py (exit status 1)
PASS: stored reference output results/mechanism_controls.json altered (copy only) -> run_checks.sh --quick failed as expected
        == FAILED: scripts/verify.py --full (exit status 1)
PASS: expected pool size in search/test_symmetry.py altered -> run_checks.sh --quick failed as expected
        == FAILED: search/test_symmetry.py (exit status 1)
PASS: expected candidate total in audit/audit_numerical.py altered -> run_checks.sh --quick failed as expected
        == FAILED: audit/audit_numerical.py (stored survivor records; bound and counts recomputed) (exit status 1)
FAILURE PROPAGATION VERIFIED
== ALL CHECKS PASSED

real	4m36.828s
user	4m33.716s
sys	0m1.208s
```

What each item establishes:

| Command | Establishes | Kind of check |
|---|---|---|
| `scripts/verify.py --full` | §8.1 (i)–(vi); Appendix A; Remark 7.2; Prop. D(b) to order 60; closed form of ρ | recomputed, then compared with stored reference outputs |
| `scripts/hadamard_identities.py` | Prop. D(a) identity to n = 200 (illustration; the proof is algebraic) | recomputed |
| `scripts/eisenstein_counterexample.py` | identity (C.1) to order 120; denominator primes 3, 5, 7 | recomputed |
| `search/test_engine.py` | engine positive control matches; negative control does **not** match | recomputed; enforced by exit status (new in v1.5) |
| `search/test_symmetry.py` | B2/B3 regression: the counterexample (exact and engine); simultaneous canonicalization preserves Diag; pools equal those of the original run; {1−u, 1−2v} not enumerated; all pool and coverage counts of Appendix C | recomputed (new in v1.5) |
| `audit/audit_numerical.py` | numbers of candidates enumerated (924,172,092; B2 and B3 from the restricted pools); bound (C.3) | recomputed |
| `audit/audit_numerical.py` | 312 survivors and their 50-coefficient outcomes | **stored records inspected, not recomputed** (default) |
| `audit/audit_exclusions.py` | every count of the exact families and the breakdown by cases of Lemma C.1 | recomputed |
| `audit/rerun_numerical_A2_A4.py` | families A2 and A4 recomputed; survivors identical to stored output (63) | recomputed |
| `audit/check_failure_propagation.sh` | failed expectations make `run_checks.sh` exit nonzero; an unmodified copy passes | failure injection on temporary copies (new in v1.5) |

## 3. Optional routine: survivor comparisons recomputed

`python3 -I audit/audit_numerical.py --recompute-survivors` is not part of the default command (about 8 minutes). It was run once for v1.5:

```
RECOMPUTED 50-coefficient comparisons modulo 2147483629 for 312 survivors: 312 agree, 0 disagree (489 s)
statements of Appendix C confirmed: True (survivor comparisons: recomputed)
real	8m8.732s
```

## 4. Failure propagation and packaging checks

- **Failure injection.** `audit/check_failure_propagation.sh` copies `supplementary/` to a temporary directory and alters only the copy. Each of five injected failures made `run_checks.sh --quick` exit with status 1 at the intended step, and the unmodified copy passed (output in section 2). The five injections were:
  - broken positive control;
  - negative control made to match;
  - altered stored reference output;
  - altered expected pool size;
  - altered expected candidate total.
- **Reference outputs.** The stored reference outputs (`results/*.json`, `search/results_*.json`) are byte-identical to v1.4.
- **Packaged copy.** `verify_all.sh` was run on a copy of the final package placed in a different directory: exit status 0.
- **Checksum failure.** In a separate temporary copy with one file altered, `verify_all.sh` exited with status 1 at the checksum step.
- **LaTeX.** A clean build in a fresh directory gives 39 pages, no warnings, no overfull boxes, and text identical to the shipped PDF.

## 5. Computational checks not performed

- Numerical families **A3, B2, B3** were not recomputed in v1.4 or v1.5; their stored output was re-examined.
- The **B2/B3 families as first described** (all pairs and triples of the described quadratics, modulo simultaneous u ↔ v) were **not** searched. Only the restricted pools P₂ (854) and P₃ (77) were enumerated; see Appendix C and `search/test_symmetry.py`.
- The exact families for S₇ were not recomputed; the counts come from `search/results_family_ce.json`.
- The survivors were not certified as identities. Prop. D(a) proves that the four target series concerned are diagonals.
- No computer check of the general proof of Theorem A exists or is claimed.

## 6. Primary sources

### 6a. Checked by me for version 1.5

**Deligne, *Équations différentielles à points singuliers réguliers*, LNM 163 (1970).** Scan supplied by the author (`Number9.pdf`, 136 PDF pages; source: publications.ias.edu). I read the passages myself: the page images of PDF pages 100, 110 and 121, and the OCR text for the others.

| Item | Book page (PDF page) | Content | Use in the paper |
|---|---|---|---|
| Théorème II.5.9 | p. 97 (p. 100) | X a smooth complex algebraic variety: V ↦ V^an is an equivalence between algebraic vector bundles with **regular** integrable connection and holomorphic vector bundles with integrable connection on X^an. Full faithfulness ("pleine fidélité") is proved on the next page. | Lemma 5.3(b), on U_ℂ |
| Théorème I.2.17 | pp. 12–13 (pp. 15–16) | On a complex manifold, local systems are equivalent to holomorphic vector bundles with integrable connection, via horizontal sections. | Lemma 5.3(b), composed with II.5.9 |
| Prop. II.4.4, Déf. II.4.5 | pp. 89–90 | Definition of regularity (via curves, or via codimension-one points of a compactification) | Lemma 5.3, regularity over K₀ defined after base change to ℂ |
| Théorème II.6.13, Prop. II.6.14 | pp. 106–107 (pp. 109–110) | 6.14: if f has a proper smooth compactification with a relative normal-crossings boundary, the conclusions (i)–(iii) of 6.13 hold. A proper smooth f (empty boundary) qualifies. | hypotheses of II.7.9 |
| Théorème II.7.9 | p. 118 (p. 121) | f: X → S smooth, between smooth schemes of finite type over ℂ, satisfying (i)–(iii) of 6.13; V regular integrable on X ⇒ the Gauss–Manin connection on Rⁱf_*(Ω•_{X/S}(V)) is regular. | Prop. 5.4, with f the abelian scheme (after base change to ℂ) and V = (𝒪_𝒜, d) |

**Applicability.** U_ℂ is a smooth complex algebraic variety. M_L is regular, because L_{a,b} is Fuchsian. E = H¹_dR(𝒜/U) is regular by II.7.9 with II.6.14. Lemma 5.3(b) uses only full faithfulness. The manuscript now cites these numbers exactly, and Table 3 was split accordingly.

### 6b. Checked by me for version 1.4 (unchanged)

| Source | Version | Checked |
|---|---|---|
| Fedorov, IMRN 2018 | arXiv:1505.01704 | §1 hypotheses (repeated entries allowed); Thm 1; Prop. 2.6 and its citations |
| Deligne, Théorie de Hodge II (1971) | published | 4.4.3 (homological; essential surjectivity attributed to Borel) |
| Milne (2013) | arXiv:1105.0887v1 | Thm 7.13 |
| Deligne–Mumford (1969) | published | Thm 2.4 (algebraically closed residue field) |
| Artin (1969) | published | Thm 1.10 |
| Harder–Kramer-Miller (2026) | IMRN journal PDF | Lemma 3.2 (number field, D-finite) |
| Rivoal–Roques (2014) | JNT journal PDF | Prop. 1; §10 |

### 6c. Reported by the external AI-assisted review (not independently counted)

The review of v1.4 reported locating and checking Deligne II.5.9 and II.7.9. I repeated those checks myself (section 6a), and only my own checks are recorded as checks.

### 6d. Cited but not rechecked by me

Most of these are cited by section rather than theorem number where I could not confirm the number:

- Katz, Publ. IHÉS 39 (1970): monodromy theorem;
- SGA 7 I, Exp. IX §3; SGA 7 II, Exp. XIV, XV;
- Liu (2002), §§6.4 and 10.3;
- Beukers–Heckman (1989), Prop. 3.3, Thm 3.5, Thm 4.8;
- Christol (1987), Props 1 and 1bis; Fürnsinn–Yurkevich (2024);
- Denef–Lipshitz (1987), Thm 6.2 and Rem. 6.4 (only as quoted by Harder–Kramer-Miller);
- EGA IV₃ §8, IV₄ §17; Jouanolou (1983) §6; Lazarsfeld (2004) §3.1; Grothendieck (1966); Ehresmann (1950).

## 7. Files changed in v1.5

- **Manuscript:** `christol_w1.tex`; `christol_w1.bbl` and `christol_w1.pdf` rebuilt; `christol_w1.bib` unchanged.
- **Supplementary, changed:**
  - `run_checks.sh`;
  - `audit/audit_numerical.py`;
  - `search/family_ab.py`, `search/run_b2.py` (pool functions and comments; enumeration unchanged, as `test_symmetry.py` confirms);
  - `search/test_engine.py`;
  - `search/hyp.py` (docstring only);
  - `search/README.md`.
- **Supplementary, new:** `audit/check_failure_propagation.sh`, `search/test_symmetry.py`, `search/list_pools.py`, `search/pools_B2_B3.json`.
- **Package root:** `verify_all.sh`, `CHANGES_AND_RESPONSE_v1_5.md`, `README.md`, `DEPENDENCY_TABLE.md`, `NOTES_FOR_AUTHOR.md`, this log, `SHA256SUMS`.
- **Unchanged:** all stored reference outputs.
- **Preserved:** the v1.3 and v1.4 archives, unchanged.
