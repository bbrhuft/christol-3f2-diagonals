# Search for an explicit diagonal representation of Christol's H

H(x) = 3F2(1/9, 4/9, 5/9; 1/3, 1; x).  Search run 17 November 2026; exact families and families
A2, A4 recomputed for version 1.4 (see ../audit).  Plain Python 3 + NumPy.
README revised for version 1.5: families B2 and B3 are described as the restricted pools that were
actually enumerated (see "Families B2 and B3" below and test_symmetry.py).

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
| A2, A3, A4 | products of 2–4 powers (1 - L)^alpha of distinct linear forms in x, y, z, alpha in (1/9)Z, up to SIMULTANEOUS permutation of the variables (complete as described) | 7 diagonal coefficients mod p = 2^31-1, scale-free invariants; survivors to 50 terms mod 2147483629 | 25,517,916 | all excluded (no survivor for H) |
| B2 | products F1^a F2^b of two distinct elements of the RESTRICTED pool P2 (854 quadratics) | same | 472,043,376 | all enumerated candidates excluded |
| B3 | products of three distinct elements of the RESTRICTED pool P3 (77 quadratics) | same | 426,610,800 | all enumerated candidates excluded |

Targets of the numerical families: the 16 series 3F2(a1,a2,a3; b, 1) with a1 <= a2 <= a3 and b in
{1/9, 2/9, ..., 8/9} (repetitions allowed), non-resonant and globally bounded (gb_targets() in
family_ab.py), plus the control 2F1(1/6,2/3;1).

## Families B2 and B3: what was actually enumerated (corrected in version 1.5)

Each polynomial 1 + a u + b v + c uv + d u^2 + e v^2 of the described set was replaced SEPARATELY by
the lexicographic minimum of (a,b,c,d,e) and (b,a,c,e,d) (its image under u <-> v).  That is not a
symmetry reduction of a product: 1/((1-u)(1-2v)) has diagonal 1/(1-2x), but the representatives
1-u, 1-2u give 1/((1-u)(1-2u)), whose diagonal is 1.  The run therefore covers only products of
distinct elements of the pools listed in pools_B2_B3.json:

* P2: from the 1,619 polynomials with a, b in {0,1,-1,-2,-3,-4}, c in {0,+-1,+-2}, d, e in {0,+-1};
  854 elements.  B2 = 364,231 pairs, covering 364,231 of the 657,226 classes of pairs of distinct
  described polynomials under the simultaneous exchange u <-> v.  {1-u, 1-2v} is not covered.
* P3: from the 95 polynomials with a, b in {0,-1,-2,-4}, c in {0,+-1}, d in {0,1}, e = 0; 77 elements,
  30 of which contain v^2 and are not in the described set.  B3 = 73,150 triples: 45,070 equivalent
  to described triples (of 130,489 classes), 28,080 not.

Completeness therefore holds within these explicit pools, not in the larger families as first
described.  No representation of H was found among the candidates actually enumerated.  The
enumeration has not been changed, so the stored counts and results describe exactly these
candidates.  test_symmetry.py checks the counterexample, the pools and all of these counts.

## Rigour of the numerical exclusions

The numerical exclusions are rigorous provided the code computes the coefficients correctly:
|d_1| * den(d_1) <= 39,680,928 < p in every family (audit/audit_numerical.py), so d_1 = 0 mod p only
if d_1 = 0, and a true representation of a target at lambda*x satisfies the invariant equations in Q
and hence mod p.  312 survivors in total, all for the four series of Proposition D(a) or the control;
none for H.  Their 50-coefficient comparisons were stored by the original run and recomputed from
scratch for version 1.5 (../audit/audit_numerical.py --recompute-survivors; 312 agree).  Survivors
are not certified as identities.

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
- test_engine.py: positive control (Abdelaziz–Koutschan–Maillard representation must match) and
  negative control (must not match); nonzero exit status on failure
- test_symmetry.py: regression test for the B2/B3 pools (counterexample, pools, counts)
- list_pools.py, pools_B2_B3.json: explicit B2/B3 pools

Note: an earlier version of family E had a bug (an extra parameter 1 in phi), caught by the
control; all reported results are from the corrected run.  In the result files, the label
'not algebraic (Eis)' means *unresolved*; it is not a proof of transcendence (see
../scripts/eisenstein_counterexample.py).
