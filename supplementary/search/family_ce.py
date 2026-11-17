#!/usr/bin/env python3
"""Exact sweeps for two shapes of explicit representation.

Family C (Proposition-D type, two variables):
    g(u, v) = (1 - u)^(-A) * phi( v / (1 - u)^k )
  Diag(g) = target  <=>  phi_n = c^n prod(T)_n/prod(B)_n with
    T = a + {(A+i)/k : i < k},  B = {b, 1} + {(A+i)/(k+1) : i <= k},
  and phi must be algebraic.

Family E (Hadamard splits):
    target = phi ⋆ psi  (coefficientwise product), phi, psi algebraic hypergeometric.
  A Hadamard product of two algebraic series is the diagonal of a rational function
  in four variables (each is a two-variable rational diagonal, Furstenberg), so a hit
  gives an explicit representation.  psi has top parameters S (size p) and bottom
  parameters {1} + R (size p - 1) from a finite grid; phi has tops a + R and
  bottoms {b, 1} + S, before cancellation.
"""
from fractions import Fraction as Fr
from itertools import combinations_with_replacement as cwr
import json, sys, time
from hyp import classify, interlace
from functools import lru_cache


def classify_fast(T, B):
    """Beukers–Heckman only: irreducible + interlacing => 'algebraic (BH)'; anything else is skipped."""
    T = list(T); B = list(B)
    for t in list(T):
        if t in B:
            T.remove(t); B.remove(t)
    if not T:
        return "algebraic (rational)"
    if any((t - b).denominator == 1 for t in T for b in B):
        return "skip (reducible psi)"
    Bn = [Fr(1) if b.denominator == 1 else b for b in B]
    if not any(b.denominator == 1 for b in B):
        return "skip (reducible psi)"
    return "algebraic (BH)" if interlace(T, Bn) else "not algebraic (BH)"


_classify = classify
@lru_cache(maxsize=None)
def _cl(key):
    return _classify(list(key[0]), list(key[1]))
def classify(T, B):
    return _cl((tuple(sorted(T)), tuple(sorted(B))))

ALG = ("algebraic (BH)", "algebraic (BH, poly)", "algebraic (polynomial)", "algebraic (rational)")


def family_c(a, b, kmax=8, qmax=36, amax=4):
    a = [Fr(x) for x in a]; b = Fr(b)
    As = sorted({Fr(p, q) for q in range(1, qmax + 1) for p in range(-amax * q, amax * q + 1)
                 if not (Fr(p, q) <= 0 and Fr(p, q).denominator == 1)})
    counts, hits, unresolved = {}, [], []
    for k in range(1, kmax + 1):
        for A in As:
            T = a + [(A + i) / k for i in range(k)]
            B = [b, Fr(1)] + [(A + i) / (k + 1) for i in range(k + 1)]
            v, T2, B2 = classify(T, B)
            counts[v] = counts.get(v, 0) + 1
            rec = {"k": k, "A": str(A), "phi_top": [str(x) for x in T2], "phi_bottom": [str(x) for x in B2], "verdict": v}
            if v in ALG:
                hits.append(rec)
            elif v == "unresolved":
                unresolved.append(rec)
    return counts, hits, unresolved


def family_e(a, b, grid, pmax=3):
    a = [Fr(x) for x in a]; b = Fr(b)
    counts, hits, unresolved = {}, [], []
    seen = set()
    for p in range(1, pmax + 1):
        for S in cwr(grid, p):
            for R in cwr(grid, p - 1):
                psiT, psiB = list(S), [Fr(1)] + list(R)
                v1 = classify_fast(psiT, psiB)
                if v1 not in ALG:
                    counts["psi " + v1] = counts.get("psi " + v1, 0) + 1
                    continue
                phiT, phiB = a + list(R), [b, Fr(1)] + list(S)
                v2, T2, B2 = classify(phiT, phiB)
                key = (tuple(sorted(T2)), tuple(sorted(B2)))
                counts["phi " + v2] = counts.get("phi " + v2, 0) + 1
                rec = {"psi_top": [str(x) for x in S], "psi_bottom": [str(x) for x in psiB],
                       "phi_top_reduced": [str(x) for x in T2], "phi_bottom_reduced": [str(x) for x in B2],
                       "psi": v1, "phi": v2}
                if key in seen:
                    continue
                seen.add(key)
                if v2 in ALG:
                    hits.append(rec)
                elif v2 == "unresolved":
                    unresolved.append(rec)
    return counts, hits, unresolved


TARGETS = {
    "AKM1 (control)": (["1/9", "4/9", "7/9"], "1/3", 18),
    "H": (["1/9", "4/9", "5/9"], "1/3", 18),
    "S7": (["1/7", "2/7", "4/7"], "1/2", 14),
    "AKM2 (control)": (["2/9", "5/9", "8/9"], "2/3", 18),
}

if __name__ == "__main__":
    out = {}
    for name, (a, b, den) in TARGETS.items():
        t0 = time.time()
        cC, hC, uC = family_c(a, b)
        grid = [Fr(j, den) for j in range(1, 2 * den + 1)]
        cE, hE, uE = family_e(a, b, grid)
        out[name] = {"C": {"counts": cC, "hits": hC, "unresolved": uC},
                     "E": {"grid": f"j/{den}, j=1..{2*den}", "counts": cE, "hits": hE, "unresolved": uE}}
        print(f"== {name}  ({time.time()-t0:.0f} s)")
        print("  Family C:", cC)
        for h in hC[:6]: print("     HIT", h)
        print("  Family E:", cE)
        for h in hE[:6]: print("     HIT", h)
        print(f"  unresolved: C {len(uC)}, E {len(uE)}")
        sys.stdout.flush()
    json.dump(out, open("results_family_ce.json", "w"), indent=1)
