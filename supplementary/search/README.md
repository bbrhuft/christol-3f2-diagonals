# Search for an explicit diagonal representation of Christol's H

H(x) = 3F2(1/9, 4/9, 5/9; 1/3, 1; x).  Run 17 November 2026.  Plain Python 3 + numpy.

## Families searched

| Family | Shape | Method | Size | Result for H |
|---|---|---|---|---|
| C | (1-u)^(-A) * phi(v/(1-u)^k), phi algebraic hypergeometric; k <= 8, A = p/q, q <= 36, |A| <= 4 | exact: reduces to Beukers–Heckman | 25,312 (k, A) | none: 25,266 excluded rigorously, 46 by Eisenstein evidence |
| E | H = phi ⋆ psi, both algebraic hypergeometric; psi has <= 3 top parameters in (1/18)Z ∩ (0, 2] | exact: Beukers–Heckman on both factors | 5.6 million psi | none |
| A2, A3, A4 | products of 2–4 powers (1 - L)^alpha, L linear in x, y, z with small coefficients, alpha in (1/9)Z | diagonal coefficients mod p, 6 terms, then 50 terms mod a second prime | 25.5 million | none |
| B2, B3 | products of 2–3 powers of quadratics in u, v with small coefficients, alpha in (1/9)Z | same | 899 million | none |

Total: about 924 million numerical candidates plus the exact sweeps.

## Controls (all recovered)
- (1-x-y)^(2/3)/(1-x-y-z) -> 3F2(1/9,4/9,7/9;1/3,1;27x) (Abdelaziz–Koutschan–Maillard 2020) found in A2.
- (1-u-v)^(-1/3) -> 2F1(1/6,2/3;1;4x) found in A2, A3, B2, B3.

## By-products (verified; see Proposition D(a) of the paper)
3F2(1/9,4/9,7/9;1/3,1), 3F2(2/9,5/9,8/9;2/3,1), 3F2(1/9,4/9,7/9;2/3,1) and 3F2(2/9,5/9,8/9;1/3,1)
are Hadamard products of two algebraic series, e.g.
  3F2(1/9,4/9,7/9;1/3,1; x) = 3F2(1/9,4/9,7/9;1/3,2/3; x) ⋆ (1-x)^(-2/3),
where the first factor is algebraic by Beukers–Heckman.  Hence each is the diagonal of a
two-variable algebraic function with separated variables.  This may be known to specialists.

## Files
- hadamard identities: see ../scripts/hadamard_identities.py
- hyp.py: algebraicity classifier (Beukers–Heckman, Eisenstein check)
- family_ce.py: families C and E; results_family_ce.json
- engine.py: modular diagonal engine; family_ab.py, run_a3.py, run_b2.py: families A and B
- results_numerical_all.json: every numerical match (families A2, A3, A4, B2, B3), each verified to 50 coefficients mod 2147483629
- test_engine.py: reproduces the published Abdelaziz–Koutschan–Maillard representation

Note: an earlier version of family E had a bug (an extra parameter 1 in phi), caught by the
control; all reported results are from the corrected run.
