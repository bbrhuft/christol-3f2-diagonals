# Christol's conjecture for non-resonant globally bounded hypergeometric series of height two

David Jordan, Maynooth University Social Sciences Institute (MUSSI), Maynooth University.

**Paper:** [`paper/christol_w1_v1_9_standalone.pdf`](paper/christol_w1_v1_9_standalone.pdf) (version 1.9, 21 November 2026, 45 pages). Source: [`paper/christol_w1_v1_9_standalone.tex`](paper/christol_w1_v1_9_standalone.tex) (bibliography embedded; compiles with `pdflatex` alone).

What changed since v1.6: [`docs/v1.9/CHANGES_v1_7_to_v1_9.md`](docs/v1.9/CHANGES_v1_7_to_v1_9.md).

## Summary

Christol conjectured that every globally bounded, D-finite power series with rational coefficients is the diagonal of a rational function. The paper proves this for the hypergeometric series

$${}_nF_{n-1}(a_1,\dots,a_n;\ b_1,\dots,b_{n-2},\ m;\ x),\qquad n\ge 3,\ m\in\mathbb{Z}_{\ge 1},$$

with rational parameters satisfying the non-resonance condition (NR): every $`a_i`$, every $`b_j`$ and every $`a_i-b_j`$ is non-integral. Counting the factorial as a lower parameter $1$, these are the series of **height two**. Global boundedness does not depend on $m$. If the series is globally bounded, it is the diagonal of an algebraic power series in two variables over $`\mathbb{Q}`$, and hence of a rational function in three variables; three is the least possible number of variables (Theorem A). Repetitions within the upper list, or within the non-integral lower list, are allowed.

The result includes Christol's 1987 example $`H(x)={}_3F_2(1/9, 4/9, 5/9; 1/3, 1; x)`$ and the series $`S_7(x)={}_3F_2(1/7, 2/7, 4/7; 1/2, 1; x)`$, which Christol suggested as a possible counterexample to his conjecture (Corollary B). By a result of Rivoal and Roques (2014), assuming the Rohrlich–Lang conjecture, $`S_7`$ is not a Hadamard product of finitely many algebraic series. Conditionally on that conjecture alone, the paper therefore gives a diagonal of a rational function with infinite Hadamard grade (Corollary E).

Combined with the two extreme heights, the paper settles the conjecture for every non-resonant $`{}_3F_2(a_1,a_2,a_3;b_1,b_2;x)`$ whose lower parameters are non-integral or positive integers (Corollary C). At maximal height (all displayed lower parameters positive integers, any order $n$), the series is a Hadamard product of $n$ algebraic series, and $`\mathrm{hg}=\mathrm{dg}=n`$ (Remark 9.6).

The proof is Hodge-theoretic and **not constructive**: it shows that the diagonal representations exist but does not produce them. Global boundedness is equivalent to every Galois conjugate of the hypergeometric local system having exactly two adjacent Hodge levels (Fedorov's formula). That condition gives a polarized integral variation of Hodge structure of weight one, hence (by Deligne) an abelian scheme and a family of curves of which the series is a period. Expanding the period over vanishing cycles at the nodes of a regular semistable model gives the diagonal. For $m\ge 2$ an explicit rational differential inverse of the contiguity relation reduces to $m=1$.

For $`S_7`$ the curve step is made explicit near $x=\infty$: with $`x=64/s^{14}`$, a companion note gives a marked genus-three family whose central fibre is $`v^2=u^7-1`$, and a holomorphic differential whose period over a transported cycle is $`S_7`$. Turning this into an explicit diagonal remains open.

Proposition D observes that some neighbouring series, including the two treated by Abdelaziz, Koutschan and Maillard (2020), are Hadamard products of two algebraic series, for an elementary reason. Christol's series is not of this kind. A computer search (Appendix C) found no explicit representation of it **among the candidates it enumerated**. That search gives no lower bound for the complexity of a representation. Its numerical families B2 and B3 cover only explicit restricted factor pools, which are smaller than first described; see Appendix C and `supplementary/search/README.md`.

| **Aspect** | **Known Before** | **Known Now (Assuming the Paper Is Correct)** |
| --- | --- | --- |
| **General Christol's conjecture** | Open in general; every diagonal of a rational function is D-finite and globally bounded, while the converse was unsolved even for hypergeometric series. | Still open in general, and for hypergeometric series of intermediate height $`2<h<n`$ and for resonant parameters. |
| **Non-resonant $`{}_nF_{n-1}(a;b_1,\dots,b_{n-2},m;x)`$, $`n\ge3`$, $`m\ge1`$ (height two)** | Widely open; for $`n=3`$ only isolated examples and a one-parameter family were known to be diagonals. The classical Euler integral gives a family of dimension $`n-1`$ (minimum monodromy weight $`-(n-1)`$), mismatching the series' weight $`-1`$, so Christol's theorem did not apply. | Proved (Theorem A): every globally bounded series in this class is the diagonal of a 2-variable algebraic power series over $`\mathbb{Q}`$ and of a 3-variable rational function over $`\mathbb{Q}`$ regular at the origin (non-constructively). Global boundedness is independent of $m$. |
| **Non-resonant $`{}_3F_2(a_1,a_2,a_3;b_1,b_2;x)`$ with $`b_1,b_2 \in \mathbb{Q}\setminus\mathbb{Z}_{\le0}`$** | Settled only when $`b_1,b_2 \notin \mathbb{Z}`$ (globally bounded $`\iff`$ algebraic) and when both $`b_j`$ are positive integers (Hadamard product of algebraic series). | Completely settled (Corollary C): the series is globally bounded if and only if it is the diagonal of a rational function over $`\mathbb{Q}`$ regular at the origin. |
| **Maximal height: $`{}_nF_{n-1}(a;m_1,\dots,m_{n-1};x)`$, all $`m_j`$ positive integers** | Known to be a Hadamard product of algebraic series when all $`m_j=1`$. | For all positive integers $`m_j`$: a Hadamard product of $n$ algebraic series, with $`\mathrm{hg}=\mathrm{dg}=n`$, so $`n+1`$ rational variables are optimal (Remark 9.6). |
| **Christol's 1987 test case $`H(x) = {}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{5}{9};\tfrac{1}{3},1;x)`$** | Not known to be a diagonal; only heuristic arguments existed. Known unconditionally that $`\mathrm{dg}(H) \ge 2`$ and $`\mathrm{hg}(H) \ge 2`$. | Proved to be the diagonal of a 2-variable algebraic series and a 3-variable rational function over $`\mathbb{Q}`$, with $`\mathrm{dg}(H) = 2`$ (Corollary B). No explicit representation is known, and whether $`H`$ is a Hadamard product of two algebraic hypergeometric series remains open. |
| **Potential counterexample $`S_7(x) = {}_3F_2(\tfrac{1}{7},\tfrac{2}{7},\tfrac{4}{7};\tfrac{1}{2},1;x)`$** | Suggested by Christol as a possible counterexample; not known whether it is a diagonal. Under the Rohrlich–Lang conjecture, known not to be a Hadamard product of finitely many algebraic power series over $`\overline{\mathbb{Q}}`$ ($`\mathrm{hg}(S_7) = \infty`$). | Ruled out as a counterexample (Corollary B): proved non-constructively to be the diagonal of a 2-variable algebraic series and a 3-variable rational function over $`\mathbb{Q}`$, with $`\mathrm{dg}(S_7) = 2`$. An explicit local genus-three curve and differential realizing its period near $x=\infty$ are described (companion note); an explicit diagonal is still open. |
| **Diagonals vs. Hadamard products of algebraic series** | Every Hadamard product of $`k`$ algebraic series is a diagonal in $`k+1`$ rational variables. The failure of the converse was known only conditionally on *both* Christol's conjecture and the Rohrlich–Lang conjecture. | Christol's conjecture is removed as a hypothesis (Corollary E): assuming *only* the Rohrlich–Lang conjecture, $`S_7`$ is a 3-variable rational diagonal with $`\mathrm{hg}(S_7) = \infty`$, so series of finite Hadamard grade form a proper subset of diagonals. |
| **Minimal number of rational variables (diagonal grade $`\mathrm{dg}`$)** | For height two, the lower bound $`\mathrm{dg} \ge 2`$ (at least 3 rational variables) was known unconditionally (Harder–Kramer-Miller), but no general upper bound was known. | Exact diagonal grade established (Theorem A): every globally bounded non-resonant height-two series has $`\mathrm{dg} = 2`$ (3 rational variables are both sufficient and necessary). |
| **Known explicit $`{}_3F_2`$ examples (Abdelaziz–Koutschan–Maillard 2020)** | $`{}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{7}{9};\tfrac{1}{3},1;x)`$, $`{}_3F_2(\tfrac{2}{9},\tfrac{5}{9},\tfrac{8}{9};\tfrac{2}{3},1;x)`$, and a one-parameter family were given as explicit 3-variable algebraic and 6-variable rational diagonals. A footnote claimed $`{}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{7}{9};\tfrac{2}{3},1;x)`$ is not a Hadamard product. | Shown elementarily (Proposition D) that those series—including $`{}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{7}{9};\tfrac{2}{3},1;x)`$ and infinitely many neighbours—are Hadamard products of two algebraic series ($`\mathrm{hg} = 2`$), and the one-parameter family is an explicit 2-variable algebraic diagonal (hence 3-variable rational). |
| **Hodge-theoretic meaning of global boundedness at height two** | Characterized arithmetically by Christol's interlacing criterion across Galois conjugates, without a weight-one geometric realization. | Equivalent to every Galois conjugate of the hypergeometric local system having exactly two adjacent Hodge levels, in any rank (Proposition 3.1), which allows a weight-one realization via an abelian scheme and a family of curves matching monodromy weight $`-1`$ (Sections 4–7). |

**Status:** preprint, not refereed. Versions 1.4–1.9 were revised after AI-assisted manuscript reviews and AI-assisted development (not journal peer review); see [`docs/`](docs/) and the acknowledgement at the end of the paper. The proof has not been checked by an independent specialist. Corrections are welcome; please open an issue.

## Contents

| Path | Contents |
|---|---|
| `paper/christol_w1_v1_9_standalone.tex`, `.pdf` | **current version (1.9)**: standalone source with embedded bibliography, and PDF |
| `paper/christol_w1_v1_6_standalone.tex`, `.pdf` | v1.6 standalone source and PDF (rank three only; archived on Zenodo, DOI [10.5281/zenodo.24355840](https://doi.org/10.5281/zenodo.24355840)) |
| `paper/christol_w1_v1_5_standalone.tex` | v1.5 standalone source |
| `paper/christol_w1.tex`, `.bib`, `.bbl`, `.pdf` | legacy multi-file source (v1.5 era); superseded by the standalone files above |
| `supplementary/scripts/` | exact-arithmetic scripts for §9.1 (Christol's example), Proposition D and Appendices A–C |
| `supplementary/results/` | stored reference outputs |
| `supplementary/search/` | search code, results, explicit B2/B3 pools, and tests (Appendix C) |
| `supplementary/audit/` | audits of the search and a failure-injection test of the checks |
| `supplementary/tools/verify_extension.py` | v1.7 higher-order checks (contiguity and counting identities in ranks 3–6) |
| `supplementary/septic_companion/` | v1.8 septic companion note v1.1: PDF, TeX, scripts, audit archive, recorded outputs |
| `supplementary/run_checks.sh` | runs all checks; nonzero exit status on any failed expectation |
| `docs/v1.9/` | summary of changes from v1.6 to v1.9 |
| `docs/v1.5/`, `docs/v1.4/` | change logs, responses, verification logs and dependency tables for those versions (unchanged) |
| `releases/` | complete archives of v1.4 and v1.5, each with `SHA256SUMS` and, for v1.5, the one-command check `verify_all.sh`; the septic companion bundle v1.1 as distributed |

### Supplementary material added for v1.7 and v1.8

- **`supplementary/tools/verify_extension.py`**: the v1.7 higher-order checks (Appendix B, "Higher-order checks in version 1.7"). Uses only the standard library and runs in about two seconds. It checks 1,220 coefficients of the forward and inverse contiguity identities (ranks 3–5, $m=2,3,4,7,12$) and the counting, equal-block and reflection identities on 2,000 parameter multisets in ranks 3–6; 47 of them satisfy the global-boundedness criterion. Output: `supplementary/results/verify_extension.txt`.
- **`supplementary/septic_companion/`**: the septic companion note, *An algebraic genus-three normal form for the septic hypergeometric period* (version 1.1, 21 November 2026), cited as [SepticReconstruction] for equation (1.5) and Example 9.4. It contains the PDF, standalone TeX, verification scripts, the original audit archive `S7_quartic_audit_checks.zip`, the recorded outputs in `rerun/`, its own `README.md` with rerun instructions, and `SHA256SUMS.txt`. The files are unchanged from the distributed bundle, which is also kept byte-for-byte as `releases/S7_Quartic_Reconstruction_v1_1_Bundle.zip`.

These finite checks support the operator, counting and septic calculations. They do not certify the general geometric existence proof.

## Reproducing the computations

From a clone of this repository:

```sh
cd supplementary
sh run_checks.sh           # all checks, about 5 minutes (Python >= 3.8, NumPy)
sh run_checks.sh --quick   # about 20 seconds
python3 -I audit/audit_numerical.py --recompute-survivors   # optional, about 8 minutes
```

From the v1.5 archive (`releases/Christol_3F2_Diagonals_Paper_v1_5.zip`), checksums included:

```sh
unzip Christol_3F2_Diagonals_Paper_v1_5.zip
cd Christol_3F2_Diagonals_Paper_v1_5
sh verify_all.sh
```

SHA-256 of the archives:

- v1.5: `ae86b2470d5cc82eec60e47bf88dda51577830f1a8ba6378ff3bf204bc63f8b1`
- v1.4: `06f5ad9ce69ea592b1c99ae301051af5f7880446a5bcb4d6e7126a0fb3cc74e0`

SHA-256 of the v1.9 paper files:

- `christol_w1_v1_9_standalone.tex`: `9f7083e4fb71f3e57e0436261d51a796f37cba7f7d0e8bda2dbb0f9c95bba4d5`
- `christol_w1_v1_9_standalone.pdf`: `e746abebc8f1961c5c8291850ac37eb3af0848b4df489ad75037c902a3e71ac9`

The v1.7 checks (standard library only, about 2 seconds):

```sh
python3 supplementary/tools/verify_extension.py
```

The septic companion checks (Python ≥ 3.10 with `python-flint`, `sympy`, `mpmath`, `numpy`). Run them from a copy of `supplementary/septic_companion/` and follow its `README.md`. Regenerating the series to order 100 (`dump_series.py 100`) takes about 4 minutes; the remaining steps take under a minute.

- `S7_Quartic_Reconstruction_v1_1_Bundle.zip`: `1a443d424c639eb44908c31b635527b48970831920c7243d102d0bd98af93a8f`
- `verify_extension.py`: `c0c19e6ad6fca58021f4c759db881ff82117f55d08a9b7e872e03b2d431f6549`

The scripts check examples, the search and its bookkeeping. They do not verify the general proof of Theorem A.

## Building the paper

```sh
cd paper
pdflatex christol_w1_v1_9_standalone.tex   # run three times for references and contents
```

The bibliography is embedded, so no BibTeX run is needed. The file compiles without errors or undefined references with TeX Live 2022/2023.

## Use of AI tools

The argument, computations and text were developed with extensive assistance from large language models (principally Claude, Anthropic, and GPT-6.1 Sol, OpenAI; also Google Gemini for literature review and the arbitrary-rank extension), under the author's direction. See the statement at the end of the paper.
