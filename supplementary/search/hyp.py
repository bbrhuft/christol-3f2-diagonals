"""Shared tools: algebraicity of hypergeometric series with rational parameters.

A series  phi(s) = sum_n prod_i (t_i)_n / prod_j (b_j)_n  s^n  (equal numbers of
top and bottom parameters; n! counts as a bottom parameter 1) is classified as:

  'algebraic (BH)'      irreducible after cancellation, interlacing holds for every
                        m coprime to the common denominator: algebraic by
                        Beukers–Heckman (1989), Theorem 4.8.  Rigorous.
  'algebraic (BH, poly)' as above after removing factors (b+m)_n/(b)_n with m >= 1,
                        which are polynomials in n; multiplying coefficients by a
                        polynomial in n preserves algebraicity.  Rigorous.
  'not algebraic (BH)'  irreducible, interlacing fails: infinite monodromy, so
                        transcendental (Beukers–Heckman).  Rigorous.
  'not algebraic (Eis)' reducible case in which at least three distinct primes that
                        divide no parameter denominator occur among the denominators of
                        the first NMAX coefficients.  This is evidence only, and the case
                        is UNRESOLVED: by Eisenstein's theorem an algebraic series has only
                        finitely many distinct denominator primes, but it may have several
                        (see ../scripts/eisenstein_counterexample.py).  [Docstring revised in
                        version 1.5; the code is unchanged.]
  'unresolved'          anything else; listed for manual inspection.
"""
from fractions import Fraction as Fr
from math import gcd

NMAX = 80


def lcm(a, b):
    return a // gcd(a, b) * b


def frac(t):
    return t - (t.numerator // t.denominator)


def _primes(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


PRIMES = _primes(20000)


def interlace(T, B):
    D = 1
    for x in T + B:
        D = lcm(D, x.denominator)
    for m in range(1, max(D, 2)):
        if gcd(m, D) != 1:
            continue
        pts = sorted([(frac(m * t), 0) for t in T] + [(frac(m * b), 1) for b in B])
        lab = [l for _, l in pts]
        if any(lab[i] == lab[i + 1] for i in range(len(lab) - 1)):
            return False
    return True


def eisenstein_outside_primes(T, B, nmax=NMAX):
    """Primes not dividing the parameter denominators that occur in coefficient denominators."""
    D = 1
    for x in T + B:
        D = lcm(D, x.denominator)
    c = Fr(1)
    found = set()
    for n in range(nmax):
        for t in T:
            c *= (t + n)
        for b in B:
            if b + n == 0:
                return None  # undefined series
            c /= (b + n)
        if c == 0:
            return set()  # polynomial
        d = c.denominator
        for p in PRIMES:
            if d == 1:
                break
            if d % p == 0:
                if D % p:
                    found.add(p)
                while d % p == 0:
                    d //= p
        if d != 1:
            found.add(d)  # composite/large leftover: definitely outside
    return found


def classify(T, B):
    T = [Fr(x) for x in T]
    B = [Fr(x) for x in B]
    for t in list(T):
        if t in B:
            T.remove(t)
            B.remove(t)
    if any(t <= 0 and t.denominator == 1 for t in T):
        return "algebraic (polynomial)", T, B
    if not T:
        return "algebraic (rational)", T, B
    # remove polynomial factors (b+m)_n/(b)_n, m >= 1
    poly = False
    changed = True
    while changed:
        changed = False
        for t in T:
            for b in B:
                m = t - b
                if m.denominator == 1 and m >= 1:
                    T.remove(t)
                    B.remove(b)
                    poly = True
                    changed = True
                    break
            if changed:
                break
    # normalize so that an integer bottom parameter is present
    reducible = any((t - b).denominator == 1 for t in T for b in B)
    if not reducible:
        if not any(b.denominator == 1 for b in B):
            reducible = True  # forced extra parameter 1 on top and bottom
    if not reducible:
        Bn = [Fr(1) if b.denominator == 1 else b for b in B]
        if interlace(T, Bn):
            return ("algebraic (BH, poly)" if poly else "algebraic (BH)"), T, B
        return "not algebraic (BH)", T, B
    out = eisenstein_outside_primes(T, B)
    if out is None:
        return "undefined", T, B
    if len(out) >= 3:
        return "not algebraic (Eis)", T, B
    return "unresolved", T, B
