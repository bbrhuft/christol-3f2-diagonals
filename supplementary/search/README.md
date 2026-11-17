# Search for an explicit diagonal representation of Christol's H

H(x) = 3F2(1/9, 4/9, 5/9; 1/3, 1; x).  Search run 17 November 2026; exact families and families
A2, A4 recomputed for version 1.4 (see ../audit).  Plain Python 3 + NumPy.

Terminology (Appendix C of the paper):
* **excluded** – a complete argument shows the candidate is not a representation;
* **unresolved** – the computation does not decide the candidate (Eisenstein-type evidence only);
* **not examined** – outside the scope of the test;
* **survivor** – passed all numerical tests; not thereby proved to be a representation.

## Families searched

| Family | Shape | Method | Size | Result for H |
|---|---|---|---|---|
| C (= family (i) of App. C) | (1-u)^(-A) phi(v/(1-u)^k), phi algebraic hypergeometric; k <= 8, A = p/q, q <= 36, abs(A) <= 4 | exact: Lemma C.1 (Beukers–Heckman) | 25,312 (k, A) | 25,266 excluded; 46 unresolved |
| E (= family (ii)) | H = phi * psi (Hadamard), psi = Phi(S; {1} u R), abs(S) <= 3, parameters in (1/18)Z, 0 < p <= 2 | exact: Lemma C.1 on psi and on phi | 5,642,388 psi | psi transcendental (excluded): 4,149,117; psi reducible (not examined): 1,457,968; psi algebraic: 35,303, of which phi transcendental (excluded) 31,495, unresolved 3,808 |
| A2, A3, A4 | products of 2–4 powers (1 - L)^alpha, L linear in x, y, z, alpha in (1/9)Z | 7 diagonal coefficients mod p = 2^31-1, scale-free invariants; survivors to 50 terms mod 2147483629 | 25,517,916 | excluded (no survivor for H) |
| B2, B3 | products of 2–3 powers of quadratics in u, v, alpha in (1/9)Z | same | 898,654,176 | excluded (no survivor for H) |

The numerical exclusions are rigorous provided the code computes the coefficients correctly:
|d_1| * den(d_1) <= 39,680,928 < p in every family (audit/audit_numerical.py), so d_1 = 0 mod p only
if d_1 = 0, and a true representation of a target at lambda*x satisfies the invariant equations in Q
and hence mod p.  312 survivors in total, all for the four series of Proposition D(a) or the control;
none for H.  Survivors are not certified individually.

## Controls (all recovered)
- (1-x-y)^(2/3)/(1-x-y-z) -> 3F2(1/9,4/9,7/9;1/3,1;27x) (Abdelaziz–Koutschan–Maillard 2020), family A2.
- (1-u-v)^(-1/3) -> 2F1(1/6,2/3;1;4x), families A2, A3, B2, B3.

## By-product (proved in the paper, Proposition D(a))
3F2(1/9,4/9,7/9;1/3,1), 3F2(2/9,5/9,8/9;2/3,1), 3F2(1/9,4/9,7/9;2/3,1) and 3F2(2/9,5/9,8/9;1/3,1)
are Hadamard products of two algebraic series, e.g.
  3F2(1/9,4/9,7/9;1/3,1; x) = T_{1/3}(x) * (1-x)^(-2/3).

## S7 = 3F2(1/7,2/7,4/7;1/2,1)
Family C: 25,260 excluded, 52 unresolved.  Family E (grid j/14): psi excluded 1,128,113; psi reducible
514,632 (not examined); psi algebraic 17,011, of which 14,539 excluded and 2,472 unresolved.

## Files
- hyp.py: classifier (Lemma C.1 branch = 'not algebraic (BH)'; 'not algebraic (Eis)' = unresolved)
- family_ce.py, family_c.py, run_e_extra.py: families C and E; results_family_ce.json
- engine.py: modular diagonal engine; family_ab.py, run_a3.py, run_b2.py: families A and B
- results_numerical_all.json: all 312 survivors, each checked to 50 coefficients mod 2147483629
- test_engine.py: reproduces the published Abdelaziz–Koutschan–Maillard representation

Note: an earlier version of family E had a bug (an extra parameter 1 in phi), caught by the
control; all reported results are from the corrected run.  In the result files, the label
'not algebraic (Eis)' means *unresolved*; it is not a proof of transcendence (see
../scripts/eisenstein_counterexample.py).
