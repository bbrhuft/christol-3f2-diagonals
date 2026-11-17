#!/usr/bin/env python3
"""Families A and B: products of powers of polynomials, matched mod p against target 3F2's.

A2: (1-L1)^al (1-L2)^be,            L = a x + b y + c z, a, b, c in {0,1,2,3}, |alpha| <= 3
A3: (1-L1)^al (1-L2)^be (1-L3)^ga,  a, b, c in {0,1,2},                     |alpha| <= 2
A4: four factors (1-L),             a, b, c in {0,1},                       |alpha| <= 1
B2: F1^al F2^be,       F = 1 + a u + b v + c uv + d u^2 + e v^2 (small coefficients), |alpha| <= 2
B3: F1^al F2^be F3^ga, F from a short list of natural quadratics,                 |alpha| <= 1
Exponents: nonzero multiples of 1/9.  (Docstring corrected in version 1.4 to match the code
below and Table 4 of the paper; the code itself is unchanged.)

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
    # B3: triples of natural quadratics in two variables
    shortB = sorted({min(q, (q[1], q[0], q[2], q[4], q[3])) for q in itertools.product([0, -1, -2, -4], [0, -1, -2, -4], [0, -1, 1], [0, 1], [0]) if any(q)})
    go("B3", 2, [[quad2(*q) for q in c] for c in itertools.combinations(shortB, 3)], 1)
    # B2: pairs of quadratics with small coefficients, up to swapping u and v
    qs = [q for q in itertools.product([0, 1, -1, -2, -3, -4], [0, 1, -1, -2, -3, -4], [-2, -1, 0, 1, 2], [0, 1, -1], [0, 1, -1]) if any(q)]
    qs = sorted({min(q, (q[1], q[0], q[2], q[4], q[3])) for q in qs})
    go("B2", 2, [[quad2(*x), quad2(*y)] for x, y in itertools.combinations(qs, 2)], 2)
    triples = sorted({canon3(c) for c in itertools.combinations(forms3, 3)})
    go("A3", 3, [[lin3(L) for L in c] for c in triples], 2)
    log.write(f"filter stage done: {len(allhits)} hits; candidates tested {sizes}\n"); log.flush()
    for hit in allhits:
        hit["verified_to_50_mod_P2"] = verify(hit, 3 if hit["family"].startswith("A") else 2)
    json.dump({"N_filter": N, "sizes": sizes, "targets": TNAMES, "hits": allhits}, open("results_family_ab.json", "w"), indent=1)
    log.write("done\n")
