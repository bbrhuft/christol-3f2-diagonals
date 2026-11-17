#!/usr/bin/env python3
"""Family C: exact sweep of Proposition-D-type representations.

Candidate shape (two variables, algebraic):
    g(u, v) = (1 - u)^beta * phi( v / (1 - u)^k ),   k = 1, 2, ..., beta = -A rational,
with phi an algebraic power series whose coefficients form a hypergeometric term.

Since [u^n] (1 - u)^(beta - k n) = (A + k n)_n / n!  with A = -beta,
    [u^n v^n] g = phi_n * (A)_{(k+1)n} / ((A)_{kn} n!).
Requiring this to equal c^n * h_n, where h_n are the coefficients of the target
3F2(a1, a2, a3; b, 1; x), forces
    phi_n = c'^n * prod(T)_n / prod(B)_n,
    T = {a1, a2, a3} + {(A+i)/k : 0 <= i < k},
    B = {b, 1} + {(A+i)/(k+1) : 0 <= i <= k}.
So a representation of this shape exists iff this hypergeometric series is
algebraic.  For irreducible parameters this is decided exactly by the
Beukers–Heckman interlacing criterion (Invent. Math. 95, 1989, Thm 4.8).
Reducible cases are listed separately for inspection.

Proposition D of the paper is the case k = 2, A = 1 - r.
"""
from fractions import Fraction as Fr
from math import gcd
import itertools, json, sys


def lcm(a, b):
    return a // gcd(a, b) * b


def frac(t):
    return t - (t.numerator // t.denominator)


def classify(T, B):
    """Return 'algebraic', 'not algebraic' or 'reducible' for sum prod(T)_n/prod(B)_n s^n."""
    T, B = list(T), list(B)
    # cancel identical parameters
    for t in list(T):
        if t in B:
            T.remove(t)
            B.remove(t)
    if not T:  # sum of s^n with polynomial-ratio 1: geometric series, rational
        return "algebraic", T, B
    if any(t <= 0 and t.denominator == 1 for t in T):
        return "algebraic (polynomial)", T, B
    if not any(b.denominator == 1 for b in B):
        T.append(Fr(1))
        B.append(Fr(1))
    for t in T:
        for b in B:
            if (t - b).denominator == 1:
                return "reducible", T, B
    D = 1
    for x in T + B:
        D = lcm(D, x.denominator)
    for m in range(1, D):
        if gcd(m, D) != 1:
            continue
        pts = sorted([(frac(m * t), 0) for t in T] + [(frac(m * b), 1) for b in B])
        labels = [l for _, l in pts]
        if any(labels[i] == labels[i + 1] for i in range(len(labels) - 1)):
            return "not algebraic", T, B
    return "algebraic", T, B


def sweep(a, b, kmax=8, qmax=36, amax=4):
    a = [Fr(x) for x in a]
    b = Fr(b)
    results = []
    As = set()
    for q in range(1, qmax + 1):
        for p in range(-amax * q, amax * q + 1):
            A = Fr(p, q)
            if A <= 0 and A.denominator == 1:
                continue
            As.add(A)
    tested = 0
    for k in range(1, kmax + 1):
        for A in sorted(As):
            T = a + [(A + i) / k for i in range(k)]
            B = [b, Fr(1)] + [(A + i) / (k + 1) for i in range(k + 1)]
            verdict, T2, B2 = classify(T, B)
            tested += 1
            if verdict != "not algebraic":
                results.append({"k": k, "A": str(A), "beta": str(-A), "verdict": verdict,
                                "phi_top": [str(x) for x in T2], "phi_bottom": [str(x) for x in B2]})
    return tested, results


TARGETS = {
    "H = 3F2(1/9,4/9,5/9;1/3,1)": (["1/9", "4/9", "5/9"], "1/3"),
    "S7 = 3F2(1/7,2/7,4/7;1/2,1)": (["1/7", "2/7", "4/7"], "1/2"),
    "control AKM1 = 3F2(1/9,4/9,7/9;1/3,1)": (["1/9", "4/9", "7/9"], "1/3"),
    "control AKM2 = 3F2(2/9,5/9,8/9;2/3,1)": (["2/9", "5/9", "8/9"], "2/3"),
}

if __name__ == "__main__":
    out = {}
    for name, (a, b) in TARGETS.items():
        tested, res = sweep(a, b)
        out[name] = {"tested": tested, "hits": res}
        print(f"{name}: {tested} (k, A) pairs tested, {len(res)} not ruled out")
        for r in res[:20]:
            print("   ", r)
    json.dump(out, open("results_family_c.json", "w"), indent=1)
