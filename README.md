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

| Aspect | Known Before the First Version of This Paper | What the Paper Establishes Through v1.9 (Assuming Its Proofs Are Correct) |
| :--- | :--- | :--- |
| **Christol’s conjecture** | Taking the diagonal of a rational function means keeping the coefficients whose indices are all equal. The resulting series satisfies a linear differential equation and has integer coefficients after suitable rescaling. Christol asked whether every rational-coefficient series with these two properties arises this way. | The conjecture remains open in general. The paper proves it for a whole class of hypergeometric series, including two longstanding test cases. |
| **The main result: height two in every order** | Several examples and families were known. There was no general diagonal theorem for non-resonant series of *height two*, where exactly one displayed lower parameter is a positive integer and the factorial supplies a second integer parameter. | In every order $`n\ge3`$, each globally bounded series in this class is the diagonal of a rational function over $`\mathbb Q`$ in **exactly three variables**. The proof works by realizing the series as an integral on a family of curves. It establishes existence even when the rational function itself is unknown. |
| **All non-resonant** $`{}_3F_2`$ **series with rational parameters** | The two extreme heights were understood, and some examples at the middle height had been solved. A result covering all three heights was missing. | Corollary C completes the classification for admissible lower parameters. A series is globally bounded if and only if it is a rational diagonal. The minimum is **2, 3, or 4 variables** according as **0, 1, or 2** of its displayed lower parameters are positive integers. Here *non-resonant* means that no upper parameter differs by an integer from a lower parameter, including the implicit lower parameter $`1`$. |
| **Christol’s 1987 benchmark** $`H={}_3F_2(\frac19,\frac49,\frac59;\frac13,1;x)`$ | Its coefficients were known to become integers after rescaling. Heuristic arguments suggested it was a diagonal, but no proof was known. | Corollary B proves that $`H`$ is a rational diagonal and that three variables are necessary and sufficient. An explicit rational function giving $`H`$ remains to be found. |
| **The proposed counterexample** $`S_7={}_3F_2(\frac17,\frac27,\frac47;\frac12,1;x)`$ | Christol suggested $`S_7`$ as a possible counterexample. Assuming the Rohrlich–Lang conjecture, Rivoal and Roques had ruled out a familiar way to construct it: multiplying the coefficients of finitely many algebraic series term by term (a *Hadamard product*). | Corollary B proves that $`S_7`$ is a three-variable rational diagonal, **independently of Rohrlich–Lang**. Assuming Rohrlich–Lang, it therefore gives an example of a rational diagonal that no finite Hadamard product of algebraic series can produce. An explicit diagonal remains open. |
| **A computable curve for** $`S_7`$ **(companion v1.1, summarized in v1.9)** | A classical integral formula represented $`S_7`$ using a family of surfaces. It did not supply the genus-three curve and integration cycle used in the companion. | The companion reconstructs a curve, a differential, and a cycle whose integral gives $`S_7`$ near $`x=\infty`$, where a smooth limiting curve makes the calculation possible. The diagonal proof uses $`x=0`$, where cycles shrink. The reconstruction is proved to all orders and checked computationally to finite order. An explicit global curve equation remains to be found. |
| **Earlier explicit examples and their place in the paper** | Abdelaziz, Koutschan and Maillard gave explicit diagonals for two close relatives of $`H`$ and a one-parameter family. Bostan and Yurkevich had already shown how to express these as Hadamard products of two algebraic series. | Proposition D gives alternative explicit formulas and a uniform factorization covering infinitely many neighbours. The advance for Christol’s original $`H`$ comes from the general height-two theorem. Whether $`H`$ itself is a Hadamard product of two algebraic hypergeometric series remains open. |

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
