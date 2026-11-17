# Christol's conjecture for non-resonant globally bounded ₃F₂(a₁,a₂,a₃;b,1) series

David Jordan, Maynooth University Social Sciences Institute (MUSSI), Maynooth University.

**Paper:** [`paper/christol_w1.pdf`](paper/christol_w1.pdf) (version 1.4, 17 November 2026; earlier title: *Globally bounded ₃F₂ series with one integral lower parameter are diagonals of rational functions*)

## Summary

Christol conjectured that every globally bounded, D-finite power series with rational coefficients is the diagonal of a rational function. The paper proves this for the hypergeometric series ₃F₂(a₁, a₂, a₃; b, 1; x) with rational parameters such that aᵢ, b and aᵢ − b are not integers. If such a series is globally bounded, it is the diagonal of an algebraic power series in two variables, and hence of a rational function in three variables; three is the least possible number of variables. This includes Christol's 1987 example ₃F₂(1/9, 4/9, 5/9; 1/3, 1; x), and the series ₃F₂(1/7, 2/7, 4/7; 1/2, 1; x), which Christol suggested as a possible counterexample to his conjecture. The proof is Hodge-theoretic and not constructive.

Version 1.4 expands the proofs (weight-one argument, de Rham descent, semistable model, node coordinates, a consolidated period-to-diagonal proposition), corrects Appendix C (new transcendence criterion, Lemma C.1; excluded / unresolved / not-examined cases kept apart), and adds verification audits. See [`docs/v1.4/RESPONSE_TO_REFEREE.md`](docs/v1.4/RESPONSE_TO_REFEREE.md); the "referee" there was an AI-assisted manuscript review, not journal peer review.

**Status:** preprint, not refereed. Corrections are welcome; please open an issue.

## Contents

| Path | Contents |
|---|---|
| `paper/` | LaTeX source, bibliography and compiled paper (38 pages) |
| `supplementary/` | scripts, stored outputs, search code, audits; `run_checks.sh` runs all checks |
| `docs/v1.4/` | response document, verification log, dependency table |
| `releases/Christol_3F2_Diagonals_Paper_v1_4.zip` | the complete v1.4 archive with SHA256SUMS |

## Reproducing the computations

```sh
cd supplementary
sh run_checks.sh           # all checks, about 4 minutes (Python >= 3.8, NumPy)
sh run_checks.sh --quick   # about 15 seconds
```

## Use of AI tools

The argument, computations and text were developed with extensive assistance from large language models (Claude, Anthropic), under the author's direction. See the statement at the end of the paper.
