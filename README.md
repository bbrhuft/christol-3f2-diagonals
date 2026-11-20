# Christol's conjecture for non-resonant globally bounded $`{}_3F_2(a_1,a_2,a_3;b,1)`$ series

David Jordan, Maynooth University Social Sciences Institute (MUSSI), Maynooth University.

**Paper:** [`paper/christol_w1.pdf`](paper/christol_w1.pdf) (version 1.5, 17 November 2026, 39 pages)

## Summary

Christol conjectured that every globally bounded, D-finite power series with rational coefficients is the diagonal of a rational function. The paper proves this for the hypergeometric series

$${}_3F_2(a_1, a_2, a_3; b, 1; x)$$

with rational parameters such that $`a_i`$, $b$, and $`a_i - b`$ are not integers. If such a series is globally bounded, it is the diagonal of an algebraic power series in two variables, and hence of a rational function in three variables; three is the least possible number of variables. This includes Christol's 1987 example $`{}_3F_2(1/9, 4/9, 5/9; 1/3, 1; x)`$, and the series $`{}_3F_2(1/7, 2/7, 4/7; 1/2, 1; x)`$, which Christol suggested as a possible counterexample to his conjecture.

By a result of Rivoal and Roques (2014), assuming the Rohrlich–Lang conjecture, the $1/7$ series is not a Hadamard product of finitely many algebraic series. Conditionally on that conjecture alone, the paper therefore gives a diagonal of a rational function with infinite Hadamard grade (Corollary E).

The proof is Hodge-theoretic and **not constructive**: it shows that the diagonal representations exist but does not produce them. Global boundedness is equivalent to every Galois conjugate of the hypergeometric local system having two adjacent Hodge levels. That condition gives a polarized integral variation of Hodge structure of weight one, hence (by Deligne) an abelian scheme and a family of curves of which the series is a period. Expanding the period over vanishing cycles at the nodes of a regular semistable model gives the diagonal.

Proposition D observes that some neighbouring series, including the two treated by Abdelaziz, Koutschan and Maillard (2020), are Hadamard products of two algebraic series, for an elementary reason. Christol's series is not of this kind. A computer search (Appendix C) found no explicit representation of it **among the candidates it enumerated**. That search gives no lower bound for the complexity of a representation. Its numerical families B2 and B3 cover only explicit restricted factor pools, which are smaller than first described; see Appendix C and `supplementary/search/README.md`.

| **Aspect** | **Known Before** | **Known Now (Assuming the Paper Is Correct)** |
| --- | --- | --- |
| **General Christol's conjecture** | Open in general; every diagonal of a rational function is D-finite and globally bounded, while the converse was unsolved even for hypergeometric series. | Still open in general, as well as for higher-order $`{}_nF_{n-1}`$ ($n \ge 4$), resonant parameters, and integral lower parameters $n \ge 2$. |
| **Non-resonant $`{}_3F_2(a_1,a_2,a_3;b,1;x)`$ (intermediate weight)** | Widely open; only isolated examples and a one-parameter family were known to be diagonals. The classical Euler integral gave a family of surfaces (minimum monodromy weight $-2$), mismatching the series' weight $-1$ so Christol's theorem did not apply. | Proved (Theorem A): every globally bounded series in this class is the diagonal of a 2-variable algebraic power series over $\mathbb{Q}$ and of a 3-variable rational function over $\mathbb{Q}$ regular at the origin (non-constructively). |
| **Non-resonant $`{}_3F_2(a_1,a_2,a_3;b_1,b_2;x)`$ with $`b_1,b_2 \in (\mathbb{Q}\setminus\mathbb{Z})\cup\{1\}`$** | Settled only at the two extremes: when $`b_1,b_2 \notin \mathbb{Z}`$ (globally bounded $\iff$ algebraic $\iff$ 2-variable rational diagonal) and when $`b_1=b_2=1`$ (Hadamard product of binomial series $\iff$ diagonal). | Completely settled (Corollary C): the series is globally bounded if and only if it is the diagonal of a rational function over $\mathbb{Q}$ regular at the origin. |
| **Christol's 1987 test case $`H(x) = {}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{5}{9};\tfrac{1}{3},1;x)`$** | Not known to be a diagonal; only heuristic arguments existed. Known unconditionally that $\operatorname{dg}(H) \ge 2$ and $\operatorname{hg}(H) \ge 2$. | Proved to be the diagonal of a 2-variable algebraic series and a 3-variable rational function over $\mathbb{Q}$, with $\operatorname{dg}(H) = 2$ (Corollary B). No explicit representation is known, and whether $H$ is a Hadamard product of two algebraic hypergeometric series remains open. |
| **Potential counterexample $`S_7(x) = {}_3F_2(\tfrac{1}{7},\tfrac{2}{7},\tfrac{4}{7};\tfrac{1}{2},1;x)`$** | Suggested by Christol as a possible counterexample; not known whether it is a diagonal. Under the Rohrlich–Lang conjecture, known not to be a Hadamard product of finitely many algebraic power series over $\overline{\mathbb{Q}}$ ($`\operatorname{hg}(S_7) = \infty`$). | Ruled out as a counterexample (Corollary B): proved non-constructively to be the diagonal of a 2-variable algebraic series and a 3-variable rational function over $\mathbb{Q}$, with $`\operatorname{dg}(S_7) = 2`$. |
| **Diagonals vs. Hadamard products of algebraic series** | Every Hadamard product of $k$ algebraic series is a diagonal in $k+1$ rational variables. The failure of the converse was known only conditionally on *both* Christol's conjecture and the Rohrlich–Lang conjecture. | Christol's conjecture is removed as a hypothesis (Corollary E): assuming *only* the Rohrlich–Lang conjecture, $`S_7`$ is a 3-variable rational diagonal with $`\operatorname{hg}(S_7) = \infty`$, so series of finite Hadamard grade form a proper subset of diagonals. |
| **Minimal number of rational variables (diagonal grade $\operatorname{dg}$)** | For non-resonant $`{}_3F_2(a;b,1;x)`$, the lower bound $`\operatorname{dg}(F_{a;b}) \ge 2`$ (at least 3 rational variables) was known unconditionally, but no general upper bound was known. | Exact diagonal grade established (Theorem A): every globally bounded non-resonant $`{}_3F_2(a;b,1;x)`$ has $`\operatorname{dg}(F_{a;b}) = 2`$ (3 rational variables are both sufficient and necessary). |
| **Known explicit $`{}_3F_2`$ examples (Abdelaziz–Koutschan–Maillard 2020)** | $`{}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{7}{9};\tfrac{1}{3},1;x)`$, $`{}_3F_2(\tfrac{2}{9},\tfrac{5}{9},\tfrac{8}{9};\tfrac{2}{3},1;x)`$, and a one-parameter family were given as explicit 3-variable algebraic and 6-variable rational diagonals. A footnote claimed $`{}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{7}{9};\tfrac{2}{3},1;x)`$ is not a Hadamard product. | Shown elementarily (Proposition D) that those series—including $`{}_3F_2(\tfrac{1}{9},\tfrac{4}{9},\tfrac{7}{9};\tfrac{2}{3},1;x)`$ and infinitely many neighbours—are Hadamard products of two algebraic series ($\operatorname{hg} = 2$), and the one-parameter family is an explicit 2-variable algebraic diagonal (hence 3-variable rational). |
| **Hodge-theoretic meaning of global boundedness for $`{}_3F_2(a;b,1)`$** | Characterized arithmetically by Christol's interlacing criterion across Galois conjugates, without a weight-one geometric realization. | Equivalent to every Galois conjugate of the hypergeometric local system having two adjacent Hodge levels (Section 3), which allows a weight-one realization via an abelian scheme and a family of curves matching monodromy weight $-1$ (Sections 4–6). |

**Status:** preprint, not refereed. Versions 1.4 and 1.5 were revised after AI-assisted manuscript reviews (not journal peer review); see [`docs/`](docs/). The proof has not been checked by an independent specialist. Corrections are welcome; please open an issue.

## Contents

| Path | Contents |
|---|---|
| `paper/christol_w1.tex`, `.bib`, `.bbl` | LaTeX source (amsart, natbib numeric) and bibliography |
| `paper/christol_w1.pdf` | compiled paper |
| `paper/christol_w1_v1_5_standalone.tex` | v1.5 source with the bibliography embedded; compiles with pdflatex alone (no `.bib` or BibTeX needed) |
| `paper/christol_w1_v1_6_standalone.tex`, `.pdf` | v1.6 standalone source and PDF: expanded AI-assistance acknowledgement; bibliography with hyperlinked DOIs and arXiv identifiers, added DOIs/URLs, updated publication data (Hassani–Maillard–Zenine 2025, Kelly–Voight 2026, Fürnsinn–Yurkevich 2024) and a note on the Dettweiler–Sabbah erratum |
| `supplementary/scripts/` | exact-arithmetic scripts for §8.1, Proposition D and Appendices A–C |
| `supplementary/results/` | stored reference outputs |
| `supplementary/search/` | search code, results, explicit B2/B3 pools, and tests (Appendix C) |
| `supplementary/audit/` | audits of the search and a failure-injection test of the checks |
| `supplementary/run_checks.sh` | runs all checks; nonzero exit status on any failed expectation |
| `docs/v1.5/` | change log and response, verification log, dependency/status table |
| `docs/v1.4/` | the corresponding documents for version 1.4 (unchanged) |
| `releases/` | complete archives of v1.4 and v1.5, each with `SHA256SUMS` and, for v1.5, the one-command check `verify_all.sh` |

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

The scripts check examples, the search and its bookkeeping. They do not verify the general proof of Theorem A.

## Building the paper

```sh
cd paper
latexmk -pdf christol_w1.tex
```

`christol_w1.bib` and `christol_w1.bbl` have not changed since v1.3 (48 entries), which is why GitHub shows the v1.3 commit beside them. If you compile `christol_w1.tex` somewhere that holds an older `christol_w1.bib`, the references will be wrong; `christol_w1_v1_5_standalone.tex` avoids this.

## Use of AI tools

The argument, computations and text were developed with extensive assistance from large language models (Claude, Anthropic), under the author's direction. See the statement at the end of the paper.
