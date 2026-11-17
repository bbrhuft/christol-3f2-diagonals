"""Controls for the node-expansion mechanism (Steps 6-8), all exact unless labelled otherwise.

1. Legendre family y^2 = t(t-x)(1-t).  In the regular chart (a, v) of the node, with a*v = x/2,
   the differential dt/y is -(1 - v(1+a)^2/2)^(-1/2) da/a, so the vanishing-cycle period is
   -2*pi*i * Diag_{a,v}[(1 - v(1+a)^2/2)^(-1/2)](x/2).  Checked: that diagonal is 2F1(1/2,1/2;1;x).
   A floating-point contour integral illustrates the same identity (illustration only).
2. The two hypergeometric series shown to be diagonals by Abdelaziz-Koutschan-Maillard,
        3F2(2/9,5/9,8/9; 2/3,1; 27x) = Diag (1-x-y)^(1/3)/(1-x-y-z),
        3F2(1/9,4/9,7/9; 1/3,1; 27x) = Diag (1-x-y)^(2/3)/(1-x-y-z),
   are diagonals of TWO-variable algebraic series
        g_r(u,v) = (1-u)^(r-1) * phi_r(v/(1-u)^2),   phi_r(s) = sum_n C(2n-r, n) s^n,   r = 1/3, 2/3,
   as the weight-one mechanism predicts for globally bounded 3F2(a;b,1).  Checked exactly: the
   coefficient identities for n <= 60 and polynomial equations satisfied by phi_r to order 60.
"""
import cmath, json, math, os, sys
from fractions import Fraction as Fr
sys.dont_write_bytecode = True

res = {}
ok = True
NMAX = 60

def poch(a, n):
    p = Fr(1)
    for j in range(n):
        p *= Fr(a) + j
    return p

def fact(n):
    return math.factorial(n)

def binom_gen(top, k):
    p = Fr(1)
    for j in range(k):
        p *= (Fr(top) - j)
    return p / fact(k)

# ---------------------------------------------------------------- 1. Legendre node
leg = True
for n in range(0, NMAX + 1):
    # [a^n v^n] (1 - v (1+a)^2/2)^(-1/2)  =  C(-1/2, n) (-1/2)^n * C(2n, n)
    coeff = binom_gen(Fr(-1, 2), n) * Fr(-1, 2) ** n * math.comb(2 * n, n)
    target = (poch(Fr(1, 2), n) / fact(n)) ** 2          # coefficient of x^n in 2F1(1/2,1/2;1;x)
    leg &= coeff * Fr(1, 2) ** n == target                 # a*v = x/2
res["legendre_node_diagonal_equals_2F1(1/2,1/2;1;x)_n<=60"] = leg
ok &= leg

def f21_half(x, terms=400):
    s = 0.0; c = 1.0
    for n in range(terms):
        s += c
        c *= ((n + 0.5) / (n + 1)) ** 2 * x
    return s
x0 = 0.3; r = 0.6; M = 4000                         # contour |t| = r with x0 < r < 1
acc = 0j
for m in range(M):
    t = r * cmath.exp(2j * math.pi * m / M)
    acc += 1.0 / (cmath.sqrt(1 - x0 / t) * cmath.sqrt(1 - t))   # (dt/t) / (sqrt(1-x/t) sqrt(1-t)) / (i dtheta)
val = acc / M                                         # = (1/(2 pi i)) contour integral
res["legendre_contour_illustration_float"] = {"x": x0, "contour_value": val.real, "2F1": f21_half(x0),
                                              "abs_difference": abs(val - f21_half(x0))}
ok &= abs(val - f21_half(x0)) < 1e-12

# ---------------------------------------------------------------- 2. AKM series as 2-variable algebraic diagonals
def series_mul(p, q, N):
    out = [Fr(0)] * (N + 1)
    for i, x in enumerate(p[:N + 1]):
        if x:
            for j, y in enumerate(q[:N + 1 - i]):
                if y:
                    out[i + j] += x * y
    return out

def series_pow_rational(B, rho, N):
    """P = B^rho for B(0) = 1, via B P' = rho B' P."""
    P = [Fr(1)] + [Fr(0)] * N
    for n in range(1, N + 1):
        s = Fr(0)
        for k in range(1, n + 1):
            s += (Fr(rho) * k - (n - k)) * B[k] * P[n - k]
        P[n] = s / n
    return P

catalan = [Fr(math.comb(2 * n, n), n + 1) for n in range(NMAX + 1)]       # B(s), B = 1 + s B^2
central = [Fr(math.comb(2 * n, n)) for n in range(NMAX + 1)]              # (1-4s)^(-1/2)
one_minus_4s = [Fr(1), Fr(-4)] + [Fr(0)] * (NMAX - 1)
one_minus_2s = [Fr(1), Fr(-2)] + [Fr(0)] * (NMAX - 1)
s_ser = [Fr(0), Fr(1)] + [Fr(0)] * (NMAX - 1)
s2_ser = [Fr(0), Fr(0), Fr(1)] + [Fr(0)] * (NMAX - 2)

def ser_pow_int(p, e):
    out = [Fr(1)] + [Fr(0)] * NMAX
    for _ in range(e):
        out = series_mul(out, p, NMAX)
    return out

def add_s(p, q): return [x + y for x, y in zip(p, q)]
def sub_s(p, q): return [x - y for x, y in zip(p, q)]
def is0(p): return all(x == 0 for x in p)

akm = {}
for r, uppers, lower in ((Fr(1, 3), (Fr(2, 9), Fr(5, 9), Fr(8, 9)), Fr(2, 3)),
                         (Fr(2, 3), (Fr(1, 9), Fr(4, 9), Fr(7, 9)), Fr(1, 3))):
    entry = {}
    phi = [binom_gen(2 * n - r, n) for n in range(NMAX + 1)]
    # (a) three-variable diagonal coefficient [x^n y^n z^n] (1-x-y)^r/(1-x-y-z) = (n+1-r)_{2n}/n!^2
    c3 = [poch(n + 1 - r, 2 * n) / fact(n) ** 2 for n in range(NMAX + 1)]
    hyp = [Fr(27) ** n * poch(uppers[0], n) * poch(uppers[1], n) * poch(uppers[2], n)
           / (poch(lower, n) * fact(n) ** 2) for n in range(NMAX + 1)]
    entry["three_variable_diagonal_equals_3F2(27x)"] = c3 == hyp
    # (b) two-variable diagonal of g_r: [u^n v^n] = phi_n * [u^n](1-u)^(r-1-2n)
    c2 = [phi[n] * binom_gen(r - 1 - 2 * n, n) * (-1) ** n for n in range(NMAX + 1)]
    entry["two_variable_diagonal_equals_3F2(27x)"] = c2 == hyp
    # (c) phi_r = B^(-r) (1-4s)^(-1/2)
    entry["phi_equals_B^(-r)/sqrt(1-4s)"] = series_mul(series_pow_rational(catalan, -r, NMAX), central, NMAX) == phi
    # (d) polynomial equation.  With W = B^(-2):  W^2 + (2s-1) W + s^2 = 0.
    Z = series_mul(ser_pow_int(phi, 6), ser_pow_int(one_minus_4s, 3), NMAX)       # phi^6 (1-4s)^3 = B^(-6r)
    if r == Fr(1, 3):                                                             # Z = W
        lhs = add_s(add_s(series_mul(Z, Z, NMAX), series_mul(sub_s(series_mul([Fr(2)], s_ser, NMAX), [Fr(1)] + [Fr(0)] * NMAX), Z, NMAX)), s2_ser)
        entry["polynomial_equation"] = "Z^2 + (2s-1) Z + s^2 = 0 with Z = phi^6 (1-4s)^3"
    else:                                                                         # Z = W^2
        zs = add_s(Z, s2_ser)
        lhs = sub_s(series_mul(Z, series_mul(one_minus_2s, one_minus_2s, NMAX), NMAX), series_mul(zs, zs, NMAX))
        entry["polynomial_equation"] = "Z (1-2s)^2 - (Z + s^2)^2 = 0 with Z = phi^6 (1-4s)^3"
    entry["polynomial_equation_holds_to_order_60"] = is0(lhs)
    entry["first_coefficients_of_phi"] = [str(x) for x in phi[:5]]
    akm[f"r={r}"] = entry
    ok &= all(v for k, v in entry.items() if isinstance(v, bool))
res["AKM_series_as_two_variable_algebraic_diagonals"] = akm

# ---------------------------------------------------------------- 3. the two-level / global boundedness lemma
# For 3F2(a1,a2,a3; b,1) with fractional parts in (0,1): Fedorov's rho is
#   (1 + [amax < b], [amid < b], -1 + [amin < b]); Christol's criterion at one conjugate is amin < b.
def frac(x):
    x = Fr(x); return x - (x.numerator // x.denominator)
def lemma_case(N):
    bad = 0; tested = 0
    from itertools import combinations_with_replacement
    vals = [Fr(j, N) for j in range(1, N)]
    for a in combinations_with_replacement(vals, 3):
        for b in vals:
            if b in a:
                continue
            tested += 1
            amin, amid, amax = sorted(a)
            rho = (1 + (amax < b), int(amid < b), -1 + (amin < b))
            alpha = sorted([Fr(0), Fr(0), frac(1 - b)]); beta = sorted(frac(-x) for x in a)
            rho_def = tuple(sum(1 for al in alpha if al < be) - (i + 1) for i, be in enumerate(beta))
            bad += tuple(rho) != rho_def
    return tested, bad
t, bcount = 0, 0
for N in range(3, 19):
    a_, b_ = lemma_case(N); t += a_; bcount += b_
res["closed_form_of_Fedorov_rho_for_3F2(a;b,1)"] = {"parameter_sets": t, "failures": bcount}
ok &= bcount == 0

res["all_checks_pass"] = bool(ok)
print(json.dumps(res, indent=1))
sys.exit(0 if ok else 1)
