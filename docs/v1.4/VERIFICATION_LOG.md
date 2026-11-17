# Verification log, version 1.4

17 November 2026. This log records what was rerun or checked for version 1.4 and what was not.

## 1. Environment

- Python 3.13.18 (standard library only for `scripts/`).
- NumPy 2.5.3 (only for `search/` and the two numerical audits).
- pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian), bibtex, latexmk 4.83.

## 2. Computational checks: completed

From `supplementary/`, run `sh run_checks.sh`. It exits with status 0 only if every check passes, and each script now compares its results with the numbers printed in the paper. The complete output below is from a run on a **copy of the package placed in a different directory** (a portability test). Exit status 0; wall time 3 min 27 s.

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
time 0.023913145065307617
[1, 1908874356, 371170058, 1776969083, 1330497452, 487403169, 1644618197, 502806404, 174670347]
[1, 1908874356, 371170058, 1776969083, 1330497452, 487403169, 1644618197, 502806404, 174670347]
match col0 True col1 False
== audit/audit_numerical.py
sets: {'A2': 391, 'A3': 500, 'A4': 10, 'B2': 364231, 'B3': 73150}
sizes: {'A2': 1140156, 'A3': 23328000, 'A4': 1049760, 'B2': 472043376, 'B3': 426610800} total 924172092
A2: |d_1| <= 9072, den | 4374, |numerator| <= 39680928 < p: True
A3: |d_1| <= 2688, den | 4374, |numerator| <= 11757312 < p: True
A4: |d_1| <= 120, den | 4374, |numerator| <= 524880 < p: True
B2: |d_1| <= 328, den | 162, |numerator| <= 53136 < p: True
B3: |d_1| <= 195, den | 162, |numerator| <= 31590 < p: True
survivors total 312 all verified to 50 mod P2: True
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
statements of Appendix C confirmed: True
== audit/audit_exclusions.py
family (i): {'not algebraic (BH)': 25266, 'not algebraic (Eis)': 46} subtypes of BH exclusions: {'P0': 25221, 'P1': 43, 'P2': 2}
family (ii) psi: {'algebraic (BH)': 34600, 'algebraic (rational)': 703, 'skip': 1457968, 'not algebraic (BH)': 4149117} subtypes of psi exclusions: {'P0': 3658432, 'P3': 472957, 'P2': 17728}
family (ii) phi: {'not algebraic (BH)': 31495, 'not algebraic (Eis)': 3808} subtypes of phi exclusions: {'P0': 28783, 'P3': 703, 'P1': 2009}
counts agree with Appendix C: True
== audit/rerun_numerical_A2_A4.py
A2: 1140156 candidates, 63 survivors
A4: 1049760 candidates, 0 survivors
survivors identical to stored output: True (63 new, 63 stored)
== ALL CHECKS COMPLETED

real	3m27.053s
user	3m25.480s
sys	0m0.162s
```

What each item establishes:

| Command | Paper statement | Result |
|---|---|---|
| `scripts/verify.py --full` | §8.1 (i)–(vi); Appendix A (38,164 parameter sets, 221,946 conjugate cases); Remark 7.2; Prop. D(b) to order 60; closed form of ρ in Prop. 3.1 | PASS |
| `scripts/hadamard_identities.py` | Prop. D(a) coefficient identity to n = 200, twelve pairs (s,c) (illustration; the proof is algebraic) | PASS |
| `scripts/eisenstein_counterexample.py` | identity (C.1) to order 120; first coefficient 58/105; outside primes 3, 5, 7 | PASS |
| `search/test_engine.py` | engine reproduces the Abdelaziz–Koutschan–Maillard representation (column 0); column 1 is a deliberate non-match | PASS |
| `audit/audit_numerical.py` | family sizes (total 924,172,092); bound (C.3), at most 39,680,928 < p; 312 survivors, all checked to 50 terms; none for H | PASS |
| `audit/audit_exclusions.py` | every count of the exact families in Appendix C, and the breakdown by the cases of Lemma C.1 | PASS |
| `audit/rerun_numerical_A2_A4.py` | families A2 and A4 recomputed from scratch; survivors identical to the stored output (63) | PASS |

LaTeX: a clean build in a fresh directory (pdflatex, bibtex, then pdflatex three times) gives 38 pages, no warnings, and text identical to the shipped PDF; the `.bbl` is identical.

## 3. Computational checks: not performed

- Numerical families **A3, B2, B3** (about 922 million candidates, several hours on two cores) were not recomputed. Their stored output (`search/results_numerical_all.json`) was re-examined by `audit_numerical.py`.
- The exact families for **S₇** were not recomputed; the counts quoted in Appendix C are from the stored file `search/results_family_ce.json`.
- The 312 survivors were not certified individually as identities. One of them, the Abdelaziz–Koutschan–Maillard function, is proved in Remark 8.4(3), and Prop. D(a) proves that the four target series are diagonals.
- No computer check of the general proof of Theorem A exists or is claimed.

## 4. Handling of d₁ ≡ 0 (mod p) in the numerical search

`engine.invariants` marks candidates with d₁ ≡ 0 (mod p) as failing. By the bound (C.3), d₁ ≡ 0 (mod p) implies d₁ = 0, and then the candidate cannot equal a target at λx with λ ≠ 0. Every quantity entering the invariant test is p-integral, and the scale λ = d₁/t₁ is a p-adic unit. So the screen discards no true representation, assuming the code computes d₀, …, d₆ correctly.

## 5. Primary sources: checked during this revision

| Source | Version consulted | What was checked |
|---|---|---|
| Fedorov, IMRN 2018 | arXiv:1505.01704 (current arXiv version, retrieved 17 Nov 2026; the retrieved PDF shows no version number) | §1 hypotheses: weakly increasing α, β in [0,1), repeated entries allowed, only αᵢ ≠ βⱼ. Theorem 1 formula ρ(k) = #{j: αⱼ < βₖ} − k. Proposition 2.6: existence via Simpson Cor. 8.1, "see also" Dettweiler–Sabbah Thm 2.4.1; alternative induction via Dettweiler–Sabbah Prop. 3.1.1; uniqueness via Deligne 1987 Prop. 1.13(i). **The v1.3 citation of DS Thm 2.4.1 was correct; a change planned during the audit was withdrawn.** |
| Deligne, Théorie de Hodge II, Publ. IHÉS 40 (1971) | published version | 4.4.3: equivalence between abelian schemes and polarizable ℤ-VHS of type {(−1,0),(0,−1)} (homology); essential surjectivity attributed to Borel |
| Milne, Shimura varieties and moduli (Handbook of Moduli II, 2013) | arXiv:1105.0887v1 (numbering used in the bibliography note) | Theorem 7.13, homological convention |
| Deligne–Mumford, Publ. IHÉS 36 (1969) | published version | Theorem 2.4 is stated for a DVR with **algebraically closed residue field**. Prop. 6.2 now works over ℚ̄[w]₍w₎ and descends. |
| Artin, Publ. IHÉS 36 (1969) | published version | Theorem 1.10: approximation for henselizations of local rings of finite type over a field. The v1.3 pin-cite (§§1, 5) for "henselization = algebraic power series" was replaced by Lemma 2.1 with a proof. |
| Harder–Kramer-Miller, IMRN 2026, rnag040 | journal PDF supplied by the author | Lemma 3.2: K a number field (fixed in §2), f D-finite; proof via the Denef–Lipshitz map D, Thm 6.2 and Rem. 6.4. Lemma 2.3 narrowed accordingly. |
| Rivoal–Roques, JNT 145 (2014) | journal PDF supplied by the author | Proposition 1 (S₇, conditional on Rohrlich–Lang; grade over ℚ̄); §10 on Christol's question for H |

## 6. Primary sources: cited but not rechecked in this revision

These references are cited at section level where the theorem number could not be confirmed:

- Deligne, LNM 163 (1970): II.5.9 (Riemann–Hilbert) and II.7.9 (regularity of Gauss–Manin).
- Katz, Publ. IHÉS 39 (1970): regularity of Gauss–Manin; monodromy theorem.
- SGA 7 I, Exp. IX §3 (Grothendieck's semistable-reduction criterion).
- SGA 7 II, Exp. XIV (ℓ-adic/topological comparison) and Exp. XV.
- Liu (2002), §6.4 (dualizing sheaf) and §10.3 (stable curves, nodes, resolution).
- Beukers–Heckman (1989), Prop. 3.3, Thm 3.5, Thm 4.8: standard statements, original not reopened.
- Christol (1987), Props 1 and 1bis; Fürnsinn–Yurkevich (2024).
- Denef–Lipshitz (1987), Thm 6.2 and Rem. 6.4: checked only as quoted by Harder–Kramer-Miller.
- EGA IV₃ §8, IV₄ §17; Jouanolou (1983) §6; Lazarsfeld (2004) §3.1; Grothendieck (1966); Ehresmann (1950).

## 7. Files

- No files referred to in the paper were missing.
- **New in v1.4:** `run_checks.sh`, `audit/*.py`, `scripts/eisenstein_counterexample.py`.
- **Changed in v1.4:**
  - `scripts/hadamard_identities.py`: now returns a nonzero exit status on failure;
  - `search/family_ab.py`: docstring only;
  - `search/README.md`: rewritten with the excluded / unresolved / not examined terminology.
- Checksums of all files are in `SHA256SUMS`; check them with `sha256sum -c SHA256SUMS` from the package root.
