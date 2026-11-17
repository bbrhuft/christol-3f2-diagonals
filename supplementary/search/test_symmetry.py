"""Regression test for the symmetry handling of families B2 and B3 (added in version 1.5).

1. The counterexample: 1/((1-u)(1-2v)) has diagonal 1/(1-2x), whereas the individually
   canonicalized factors 1-u, 1-2u give 1/((1-u)(1-2u)), whose diagonal is 1.  Checked in
   exact integer arithmetic and with the modular engine used by the search.
2. Simultaneous canonicalization (canon_collection2) preserves the diagonal.
3. The pools b2_pool(), b3_pool() reproduce exactly the inline expressions of the original
   run, and the pair {1-u, 1-2v} is NOT enumerated in B2, even up to simultaneous u <-> v.
4. The counts quoted in Appendix C (version 1.5): pool sizes, numbers of factor sets, and
   their coverage of the originally described families modulo simultaneous exchange.
Exit status 0 iff every expectation holds.  Usage (from this folder): python3 test_symmetry.py
"""
import itertools, sys
import numpy as np
from engine import diagonal, P1
import family_ab as F

N = 12
fails = []


def check(name, cond):
    print(('PASS: ' if cond else 'FAIL: ') + name)
    if not cond:
        fails.append(name)


def exact_diag_two_linear(c1, c2, N):
    """Diag of 1/((1 - c1.(u,v)) (1 - c2.(u,v))) for linear forms c = (cu, cv), exactly."""
    def series(c):  # coefficients of 1/(1 - cu u - cv v): binom(i+j, i) cu^i cv^j
        return lambda i, j: (c[0] ** i) * (c[1] ** j) * (1 if i + j == 0 else
                                                        __import__('math').comb(i + j, i))
    s1, s2 = series(c1), series(c2)
    out = []
    for n in range(N + 1):
        out.append(sum(s1(i, j) * s2(n - i, n - j) for i in range(n + 1) for j in range(n + 1)))
    return out


# 1. the counterexample, exactly
d_true = exact_diag_two_linear((1, 0), (0, 2), N)          # (1-u)(1-2v)
d_canon = exact_diag_two_linear((1, 0), (2, 0), N)         # (1-u)(1-2u)
check('exact: Diag 1/((1-u)(1-2v)) = 1/(1-2x)', d_true == [2 ** n for n in range(N + 1)])
check('exact: Diag 1/((1-u)(1-2u)) = 1', d_canon == [1] + [0] * N)

# ... and with the modular engine of the search
one_minus_u, one_minus_2v, one_minus_2u = F.quad2(-1, 0, 0, 0, 0), F.quad2(0, -2, 0, 0, 0), F.quad2(-2, 0, 0, 0, 0)
al = np.array([[P1 - 1], [P1 - 1]], dtype=np.int64)       # exponents -1, -1
e_true = [int(x) for x in diagonal([one_minus_u, one_minus_2v], al, N, 2, P1)[:, 0]]
e_canon = [int(x) for x in diagonal([one_minus_u, one_minus_2u], al, N, 2, P1)[:, 0]]
check('engine: Diag (1-u)^-1 (1-2v)^-1 = 2^n mod p', e_true == [pow(2, n, P1) for n in range(N + 1)])
check('engine: Diag (1-u)^-1 (1-2u)^-1 = 1', e_canon == [1] + [0] * N)
check('individual representatives change the product: representative2(1-2v) = 1-2u',
      F.representative2((0, -2, 0, 0, 0)) == (-2, 0, 0, 0, 0))

# 2. simultaneous canonicalization preserves the diagonal
cc = F.canon_collection2([(-1, 0, 0, 0, 0), (0, -2, 0, 0, 0)])
e_cc = [int(x) for x in diagonal([F.quad2(*q) for q in cc], al, N, 2, P1)[:, 0]]
check('simultaneous canonicalization preserves the diagonal', e_cc == e_true)

# 3. the pools are exactly those of the original run
orig_b3 = sorted({min(q, (q[1], q[0], q[2], q[4], q[3])) for q in itertools.product([0, -1, -2, -4], [0, -1, -2, -4], [0, -1, 1], [0, 1], [0]) if any(q)})
orig_b2 = [q for q in itertools.product([0, 1, -1, -2, -3, -4], [0, 1, -1, -2, -3, -4], [-2, -1, 0, 1, 2], [0, 1, -1], [0, 1, -1]) if any(q)]
orig_b2 = sorted({min(q, (q[1], q[0], q[2], q[4], q[3])) for q in orig_b2})
P2, P3 = F.b2_pool(), F.b3_pool()
check('b2_pool() equals the pool of the original run', P2 == orig_b2)
check('b3_pool() equals the pool of the original run', P3 == orig_b3)
enum2 = {F.canon_collection2(c) for c in itertools.combinations(P2, 2)}
ce = F.canon_collection2([(-1, 0, 0, 0, 0), (0, -2, 0, 0, 0)])
check('the pair {1-u, 1-2v} is not enumerated in B2, even up to simultaneous u<->v', ce not in enum2)
import json, os
if os.path.exists('pools_B2_B3.json'):
    stored = json.load(open('pools_B2_B3.json'))
    check('stored pools_B2_B3.json agrees with the pools', [tuple(q) for q in stored['B2_pool']] == P2
          and [tuple(q) for q in stored['B3_pool']] == P3)
check('both factors 1-u and 1-2v belong to the originally described B2 polynomials',
      {(-1, 0, 0, 0, 0), (0, -2, 0, 0, 0)} <= set(F.b2_advertised()))

# 4. counts quoted in Appendix C
adv2, adv3 = F.b2_advertised(), F.b3_advertised()
adv2_orbits = {F.canon_collection2(c) for c in itertools.combinations(adv2, 2)}
adv3_orbits = {F.canon_collection2(c) for c in itertools.combinations(adv3, 3)}
enum3 = list(itertools.combinations(P3, 3))
enum3_orbits = {F.canon_collection2(c) for c in enum3}
counts = {
    'B2 described polynomials': len(adv2), 'B2 pool': len(P2),
    'B2 pairs enumerated': len(list(itertools.combinations(P2, 2))),
    'B2 classes of described pairs': len(adv2_orbits), 'B2 classes hit': len(enum2 & adv2_orbits),
    'B3 described polynomials': len(adv3), 'B3 pool': len(P3),
    'B3 pool outside described set': sum(1 for q in P3 if q not in set(adv3)),
    'B3 triples enumerated': len(enum3), 'B3 classes of described triples': len(adv3_orbits),
    'B3 classes hit': len(enum3_orbits & adv3_orbits), 'B3 enumerated outside described family': len(enum3_orbits - adv3_orbits),
}
expected = {
    'B2 described polynomials': 1619, 'B2 pool': 854, 'B2 pairs enumerated': 364231,
    'B2 classes of described pairs': 657226, 'B2 classes hit': 364231,
    'B3 described polynomials': 95, 'B3 pool': 77, 'B3 pool outside described set': 30,
    'B3 triples enumerated': 73150, 'B3 classes of described triples': 130489,
    'B3 classes hit': 45070, 'B3 enumerated outside described family': 28080,
}
for k in expected:
    check(f'{k}: {counts[k]} (expected {expected[k]})', counts[k] == expected[k])
check('candidate counts: B2 = 364,231 x 36^2, B3 = 73,150 x 18^3',
      364231 * 36 ** 2 == 472043376 and 73150 * 18 ** 3 == 426610800)

print('ALL SYMMETRY CHECKS PASSED' if not fails else f'{len(fails)} FAILURE(S)')
sys.exit(1 if fails else 0)
