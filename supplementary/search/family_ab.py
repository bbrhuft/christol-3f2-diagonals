#!/usr/bin/env python3
"""Families A and B: products of powers of polynomials, matched mod p against target 3F2's.

A2: (1-L1)^al (1-L2)^be,            L = a x + b y + c z, a, b, c in {0,1,2,3}, |alpha| <= 3
A3: (1-L1)^al (1-L2)^be (1-L3)^ga,  a, b, c in {0,1,2},                     |alpha| <= 2
A4: four factors (1-L),             a, b, c in {0,1},                       |alpha| <= 1
    Families A: distinct linear forms, taken up to a SIMULTANEOUS permutation of x, y, z
    (canon3), which is a genuine symmetry reduction because Diag is symmetric.
B2: F1^al F2^be with F1 != F2 in the RESTRICTED POOL b2_pool() (854 polynomials),  |alpha| <= 2
B3: F1^al F2^be F3^ga, distinct F_i in the RESTRICTED POOL b3_pool() (77 polynomials), |alpha| <= 1
    The pools were formed by replacing EACH factor separately by the lexicographically
    smaller of itself and its image under u <-> v (representative2).  That restricts the
    search; it is not a symmetry reduction of the products.  B2 and B3 are therefore NOT the
    complete families "products of quadratics of the stated shape, up to u <-> v".  See the
    comments before swap2() below, test_symmetry.py, and Appendix C of the paper (v1.5).
Exponents: nonzero multiples of 1/9.  (Docstring corrected in versions 1.4 and 1.5 to match
the code; the enumeration itself is unchanged since the original run, so the stored counts
and results describe exactly the candidates listed here.)

A candidate matches target T if its diagonal d satisfies d_n = c^n t_n for n <= N,
tested through the scale-free invariants d_j/d_1^j (j = 2..N) mod p.  Survivors are
re-checked to n = 50 modulo a second prime.
"""
import numpy as np, itertools, json, sys, time
from fractions import Fraction as Fr
from math import gcd
from engine import diagonal, invariants, target_invariants, hyp_coeffs_mod, P1, P2

N = 6


def r(q, p):
    q = Fr(q)
    return q.numerator % p * pow(q.denominator, p - 2, p) % p


def gb_targets():
    """All globally bounded non-resonant 3F2(a1,a2,a3; b, 1) with common denominator 3 or 9."""
    out = []
    vals = [Fr(j, 9) for j in range(1, 9)]
    for a in itertools.combinations_with_replacement(vals, 3):
        for b in vals:
            if any(x == b for x in a):
                continue
            Nd = 1
            for x in list(a) + [b]:
                Nd = Nd * x.denominator // gcd(Nd, x.denominator)
            ok = True
            for k in range(1, Nd):
                if gcd(k, Nd) != 1:
                    continue
                ak = sorted((k * x) % 1 for x in a); bk = (k * b) % 1
                if not (ak[0] < bk < ak[2]):
                    ok = False; break
            if ok:
                out.append((a, b))
    return out


TARGETS = {}
for a, b in gb_targets():
    name = "3F2(" + ",".join(str(x) for x in a) + ";" + str(b) + ",1)"
    TARGETS[name] = ([(x.numerator, x.denominator) for x in a], (b.numerator, b.denominator))
# positive control reachable by B: (1-u-v)^(-1/3) has diagonal 2F1(1/6,2/3;1;4x) = 3F2(1/6,2/3,1/2;1/2,1)
TARGETS["control 2F1(1/6,2/3;1)"] = ([(1, 6), (2, 3), (1, 2)], (1, 2))
HNAME = "3F2(1/9,4/9,5/9;1/3,1)"
assert HNAME in TARGETS

TINV = {name: np.array(target_invariants(a, b, N, P1), dtype=np.int64) for name, (a, b) in TARGETS.items()}
TMAT = np.stack(list(TINV.values()))
TNAMES = list(TINV.keys())


def exps(lim):
    return [Fr(j, 9) for j in range(-9 * lim, 9 * lim + 1) if j != 0]


def run_family(label, nvars, factor_sets, explim, log):
    E = exps(explim)
    hits = []
    t0 = time.time()
    for idx, fs in enumerate(factor_sets):
        k = len(fs)
        grid = list(itertools.product(E, repeat=k))
        rE = {x: r(x, P1) for x in E}
        al = np.array([[rE[g[j]] for g in grid] for j in range(k)], dtype=np.int64)
        d = diagonal(fs, al, N, nvars, P1)
        I, good = invariants(d, P1)
        # compare against all targets
        eq = (I.T[None, :, :] == TMAT[:, None, :]).all(axis=2) & good[None, :]
        for ti, gi in zip(*np.nonzero(eq)):
            hits.append({"family": label, "factors": [sorted(F.items()) for F in fs],
                         "exponents": [str(x) for x in grid[gi]], "target": TNAMES[ti]})
        if idx % 50 == 0:
            log.write(f"{label}: {idx+1}/{len(factor_sets)} factor sets, {len(hits)} hits, {time.time()-t0:.0f}s\n"); log.flush()
    return hits, len(factor_sets) * len(E) ** len(factor_sets[0]) if factor_sets else 0


def verify(hit, nvars):
    """Re-check a hit to n = 50 modulo a second prime."""
    fs = [dict((tuple(e), c) for e, c in F) for F in hit["factors"]]
    al = np.array([[r(x, P2)] for x in hit["exponents"]], dtype=np.int64)
    d = diagonal(fs, al, 50, nvars, P2)[:, 0]
    a, b = TARGETS[hit["target"]]
    t = hyp_coeffs_mod(a, b, 50, P2)
    c = int(d[1]) * pow(t[1], P2 - 2, P2) % P2
    return all(int(d[n]) == t[n] * pow(c, n, P2) % P2 for n in range(51))


def canon3(forms):
    """Canonical representative of a tuple of 3-variable linear forms under permuting variables."""
    best = None
    for perm in itertools.permutations(range(3)):
        t = tuple(sorted(tuple(L[i] for i in perm) for L in forms))
        best = t if best is None or t < best else best
    return best


def lin3(L):
    F = {(0, 0, 0): 1}
    for i, c in enumerate(L):
        if c:
            e = [0, 0, 0]; e[i] = 1; F[tuple(e)] = -c
    return F


def quad2(a, b, c, d, e):
    F = {(0, 0): 1}
    for (ex, co) in [((1, 0), a), ((0, 1), b), ((1, 1), c), ((2, 0), d), ((0, 2), e)]:
        if co:
            F[ex] = co
    return F


# ---------------------------------------------------------------------------
# Symmetry reductions versus restricted factor pools (clarified in version 1.5).
#
# Two operations must not be confused.
#  * Simultaneous canonicalization of a whole factor collection under a permutation of
#    the variables: canon3 (families A) and canon_collection2 (two variables).  Diag is
#    invariant when the SAME permutation is applied to every factor, so this is a genuine
#    symmetry reduction.
#  * Choosing a representative of each factor separately: representative2.  This is NOT
#    a symmetry reduction of a product.  Example: 1/((1-u)(1-2v)) has diagonal 1/(1-2x),
#    but replacing each factor by its representative gives 1/((1-u)(1-2u)), whose diagonal
#    is 1.  Applied to every factor it only restricts the pool of factors.
#
# Families B2 and B3 as run in November 2026 applied representative2 to every factor, so
# they enumerate products of distinct elements of b2_pool() and b3_pool().  The functions
# below reproduce those pools exactly (checked in test_symmetry.py against the original
# inline expressions); the enumeration has not been changed.

def swap2(q):
    """Coefficient vector (a, b, c, d, e) of 1+au+bv+cuv+du^2+ev^2 after exchanging u and v."""
    return (q[1], q[0], q[2], q[4], q[3])


def representative2(q):
    """Representative of a SINGLE factor (lexicographic minimum of q and swap2(q)).
    Using it on each factor separately restricts the pool; it is not a symmetry reduction."""
    return min(q, swap2(q))


def canon_collection2(qs):
    """Canonical form of a whole COLLECTION of factors under the simultaneous exchange u <-> v.
    This is a genuine symmetry reduction (not used by the November 2026 run)."""
    a = tuple(sorted(qs))
    b = tuple(sorted(swap2(q) for q in qs))
    return min(a, b)


def b2_advertised():
    """The 1,619 nonconstant polynomials described for B2: a, b in {0,1,-1,-2,-3,-4},
    c in {-2,...,2}, d, e in {0,1,-1}."""
    return [q for q in itertools.product([0, 1, -1, -2, -3, -4], [0, 1, -1, -2, -3, -4], [-2, -1, 0, 1, 2], [0, 1, -1], [0, 1, -1]) if any(q)]


def b3_advertised():
    """The 95 nonconstant polynomials described for B3: a, b in {0,-1,-2,-4}, c in {0,-1,1},
    d in {0,1}, e = 0."""
    return [q for q in itertools.product([0, -1, -2, -4], [0, -1, -2, -4], [0, -1, 1], [0, 1], [0]) if any(q)]


def b2_pool():
    """The pool actually used for B2 (854 polynomials, a subset of b2_advertised())."""
    return sorted({representative2(q) for q in b2_advertised()})


def b3_pool():
    """The pool actually used for B3 (77 polynomials; 30 of them have a v^2 term and are not
    in b3_advertised())."""
    return sorted({representative2(q) for q in b3_advertised()})


if __name__ == "__main__":
    log = open("family_ab.log", "a")
    log.write(f"targets: {len(TARGETS)} ({', '.join(TNAMES)})\n"); log.flush()
    allhits, sizes = [], {}
    def go(label, nv, sets, lim):
        global allhits
        h, n = run_family(label, nv, sets, lim, log); allhits += h; sizes[label] = n
        json.dump({"N_filter": N, "sizes": sizes, "targets": TNAMES, "hits": allhits}, open("results_family_ab_partial.json", "w"), indent=1)
    forms4 = [L for L in itertools.product(range(4), repeat=3) if any(L)]
    forms3 = [L for L in itertools.product(range(3), repeat=3) if any(L)]
    forms2 = [L for L in itertools.product(range(2), repeat=3) if any(L)]
    pairs = sorted({canon3(c) for c in itertools.combinations(forms4, 2)})
    go("A2", 3, [[lin3(L) for L in c] for c in pairs], 3)
    quads = sorted({canon3(c) for c in itertools.combinations(forms2, 4)})
    go("A4", 3, [[lin3(L) for L in c] for c in quads], 1)
    # B3: triples of distinct elements of the restricted pool b3_pool() (see above)
    shortB = b3_pool()
    go("B3", 2, [[quad2(*q) for q in c] for c in itertools.combinations(shortB, 3)], 1)
    # B2: pairs of distinct elements of the restricted pool b2_pool() (see above).
    # This is NOT the full family of pairs of quadratics up to swapping u and v.
    qs = b2_pool()
    go("B2", 2, [[quad2(*x), quad2(*y)] for x, y in itertools.combinations(qs, 2)], 2)
    triples = sorted({canon3(c) for c in itertools.combinations(forms3, 3)})
    go("A3", 3, [[lin3(L) for L in c] for c in triples], 2)
    log.write(f"filter stage done: {len(allhits)} hits; candidates tested {sizes}\n"); log.flush()
    for hit in allhits:
        hit["verified_to_50_mod_P2"] = verify(hit, 3 if hit["family"].startswith("A") else 2)
    json.dump({"N_filter": N, "sizes": sizes, "targets": TNAMES, "hits": allhits}, open("results_family_ab.json", "w"), indent=1)
    log.write("done\n")
