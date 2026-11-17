# Globally bounded ₃F₂ series with one integral lower parameter are diagonals of rational functions

David Jordan, Maynooth University Social Sciences Institute (MUSSI), Maynooth University.

**Paper:** [`paper/christol_w1.pdf`](paper/christol_w1.pdf) (version 1.1, 17 November 2026)

## Summary

Christol conjectured that every globally bounded, D-finite power series with rational coefficients is the diagonal of a rational function. The paper proves this for the hypergeometric series

  ₃F₂(a₁, a₂, a₃; b, 1; x)

with rational parameters such that aᵢ, b and aᵢ − b are not integers. If such a series is globally bounded, it is the diagonal of an algebraic power series in two variables, and hence of a rational function in three variables, which is the least possible number. This includes Christol's 1987 example ₃F₂(1/9, 4/9, 5/9; 1/3, 1; x).

The proof is Hodge-theoretic and not constructive. Global boundedness is shown to be equivalent to every Galois conjugate of the hypergeometric local system having two adjacent Hodge levels. That condition gives a polarized integral variation of Hodge structure of weight one, hence (by Deligne) an abelian scheme and a family of curves of which the series is a period. Expanding the period over vanishing cycles at the nodes of a regular semistable model gives the diagonal.

**Status:** preprint. The argument has not yet been reviewed by independent experts. Corrections are welcome; please open an issue.

## Contents

| Path | Contents |
|---|---|
| `paper/christol_w1.tex` | LaTeX source (amsart, natbib) |
| `paper/christol_w1.bib`, `paper/christol_w1.bbl` | Bibliography database and compiled bibliography |
| `paper/christol_w1.pdf` | Compiled paper, 25 pages |
| `supplementary/scripts/` | Exact-arithmetic Python scripts for the computations in §8.1 and Appendices A–B |
| `supplementary/results/` | Stored outputs of those scripts |

## Building the paper

```sh
cd paper
latexmk -pdf christol_w1.tex
```

## Reproducing the computations

The scripts use only the Python standard library (Python 3.8 or later) and exact rational arithmetic.

```sh
cd supplementary
python3 scripts/verify.py          # standard checks, a few seconds
python3 scripts/verify.py --full   # adds the full Hodge-number scan (221,946 cases), about 10 s
```

`verify.py` reruns each script and compares its output with the stored results:

- `monodromy_hermitian.py`: §8.1 (i)–(vi), monodromy matrices, the invariant hermitian form, signatures, and the Gram determinant 3³⁶ of the polarization for Christol's example.
- `hodge_L2_count.py`: Appendix A, an independent check of the Hodge numbers by counting square-integrable 2-forms on the Euler surfaces.
- `mechanism_controls.py`: Remark 7.2, Proposition D, and the closed form of Fedorov's ρ used in Proposition 3.1.
- `w1_tools.py`: shared arithmetic in ℚ(ζ₉) and certified sign tests.

## Use of AI tools

The argument, computations and text were developed with extensive assistance from large language models (Claude, Anthropic), under the author's direction. See the statement at the end of the paper.
