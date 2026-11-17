"""Independent check of the Hodge numbers of hypergeometric rank-3 local systems (Step 4 input).

Fedorov's formula is compared with a direct count of square-integrable holomorphic 2-forms in the
character eigenspaces of the Euler-integral surface.  No formula from Fedorov's paper is used in
the count; it only uses the Euler integrand

    s^(a2-1) (1-s)^(b1-a2-1) t^(a3-1) (1-t)^(b2-a3-1) (1 - x s t)^(-a1) ds dt

on Y = P^1 x P^1 with branch divisor s = 0, 1, oo ; t = 0, 1, oo ; Q = {x s t = 1}.
Q meets the other components transversally except at the two triple points (s,t) = (oo,0), (0,oo),
which become normal crossings after one blow-up each.

For an exponent class c = (c1..c5) in (Q/Z)^5, every eigenform is P(s,t) * w0 with
w0 = s^p (1-s)^q t^r (1-t)^u (1-xst)^v ds dt, (p,q,r,u,v) the representatives of c in (-1, 0), and P a
polynomial.  A top-degree form is square integrable iff its order along every component of a normal
crossings model is > -1.  For the monomial s^i t^j this reads

    S_oo :  i < -(p+q+v) - 1          T_oo :  j < -(r+u+v) - 1
    E_(oo,0) :  j - i > p + q - r     E_(0,oo) :  i - j > r + u - p

and the conditions are monomial-wise, so h^{2,0}(c) is a lattice-point count.
With no integral exponent class on any of the nine components the eigenspace of H^2 is pure of
rank 3, and (h^{2,0}, h^{1,1}, h^{0,2}) = (N(c), 3 - N(c) - N(-c), N(-c)).
"""
import json, os, sys, time
from fractions import Fraction as Fr
from itertools import combinations_with_replacement, permutations
from math import gcd
sys.dont_write_bytecode = True

def frac(x):
    x = Fr(x)
    return x - (x.numerator // x.denominator)

def ceil_strict_upper(bound):
    """largest integer n with n < bound"""
    b = Fr(bound)
    f = b.numerator // b.denominator            # floor
    return f - 1 if f == b else f

def classes(a1, a2, a3, b1, b2):
    return [frac(a2), frac(b1 - a2), frac(a3), frac(b2 - a3), frac(-a1)]

def nonresonant(a1, a2, a3, b1, b2):
    c = classes(a1, a2, a3, b1, b2)
    extra = [frac(a1 - b1), frac(a1 - b2), frac(a3 - b1), frac(a2 - b2)]
    return all(x != 0 for x in c + extra)

def h20(c):
    p, q, r, u, v = [x - 1 for x in c]            # representatives in (-1, 0); needs c_i != 0
    imax = ceil_strict_upper(-(p + q + v) - 1)
    jmax = ceil_strict_upper(-(r + u + v) - 1)
    n = 0
    for i in range(0, imax + 1):
        for j in range(0, jmax + 1):
            if (j - i) > (p + q - r) and (i - j) > (r + u - p):
                n += 1
    return n

def surface_hodge(a1, a2, a3, b1, b2, k=1):
    c = [frac(k * x) for x in classes(a1, a2, a3, b1, b2)]
    cm = [frac(-x) for x in c]
    n, m = h20(c), h20(cm)
    return (n, 3 - n - m, m)

def fedorov(a, b, k=1):
    """Fedorov Thm 1 for prod(D - alpha) - z prod(D - beta), alpha = {0,1-b1,1-b2}, beta = {-a_i} (mod 1)."""
    alpha = sorted([Fr(0)] + [frac(k * (1 - Fr(x))) for x in b])
    beta = sorted(frac(-k * Fr(x)) for x in a)
    rho = [sum(1 for al in alpha if al < be) - (i + 1) for i, be in enumerate(beta)]
    hi, lo = max(rho), min(rho)
    return tuple(rho.count(p) for p in range(hi, lo - 1, -1))

def strip(t):
    t = list(t)
    while t and t[0] == 0: t.pop(0)
    while t and t[-1] == 0: t.pop()
    return tuple(t)

def units(N):
    return [k for k in range(1, N + 1) if gcd(k, N) == 1]

T0 = time.process_time()
res = {}
ok = True

# ---------------------------------------------------------------- the target and controls
def report(a, b1, b2, N):
    out = {}
    for k in units(N):
        triples = set()
        for (x1, x2, x3) in set(permutations(a)):
            for (y1, y2) in ((b1, b2), (b2, b1)):
                if nonresonant(k * x1, k * x2, k * x3, k * y1, k * y2):
                    triples.add(surface_hodge(x1, x2, x3, y1, y2, k))
        out[str(k)] = {"surface_(h20,h11,h02)_over_all_role_assignments": sorted(triples),
                       "fedorov_top_to_bottom": list(fedorov(a, (b1, b2), k))}
    return out

H = (Fr(1, 9), Fr(4, 9), Fr(5, 9))
res["H_3F2(1/9,4/9,5/9;1/3,1)"] = report(H, Fr(1, 3), Fr(1), 9)
res["control_AKM_3F2(1/9,4/9,7/9;1/3,1)"] = report((Fr(1, 9), Fr(4, 9), Fr(7, 9)), Fr(1, 3), Fr(1), 9)
res["control_MUM_3F2(1/2,1/2,1/2;1,1)"] = report((Fr(1, 2),) * 3, Fr(1), Fr(1), 2)
res["control_not_GB_3F2(1/9,4/9,5/9;2/3,1)"] = report(H, Fr(2, 3), Fr(1), 9)

def consistent(rep):
    """Every role assignment gives the same Hodge numbers up to a shift of the grading, and they are
    Fedorov's numbers read in the opposite order (the surface eigenspace is the dual local system)."""
    good = True
    for k, v in rep.items():
        ts = {strip(t) for t in v["surface_(h20,h11,h02)_over_all_role_assignments"]}
        f = tuple(v["fedorov_top_to_bottom"])
        good &= ts == {strip(f[::-1])}
    return good
for name in list(res):
    res[name + "__agrees_with_Fedorov_up_to_shift_and_duality"] = consistent(res[name])
    ok &= res[name + "__agrees_with_Fedorov_up_to_shift_and_duality"]

hrep = res["H_3F2(1/9,4/9,5/9;1/3,1)"]
res["H_every_conjugate_has_h20*h02=0_(two_adjacent_levels)"] = all(
    t[0] * t[2] == 0 for v in hrep.values() for t in v["surface_(h20,h11,h02)_over_all_role_assignments"])
ok &= res["H_every_conjugate_has_h20*h02=0_(two_adjacent_levels)"]

# ---------------------------------------------------------------- scans (integer arithmetic, numerators mod N)
def h20_int(c, N):
    P, Q, R, U, V = [x - N for x in c]            # N * representative, each in (-N, 0)
    n = 0
    i = 0
    while N * i < -(P + Q + V + N):
        j = 0
        while N * j < -(R + U + V + N):
            if N * (j - i) > P + Q - R and N * (i - j) > R + U - P:
                n += 1
            j += 1
        i += 1
    return n

def surface_int(a1, a2, a3, b1, b2, N):
    """numerators mod N (b = 0 encodes an integral lower parameter); None if resonant."""
    c = [a2 % N, (b1 - a2) % N, a3 % N, (b2 - a3) % N, (-a1) % N]
    extra = [(a1 - b1) % N, (a1 - b2) % N, (a3 - b1) % N, (a2 - b2) % N]
    if 0 in c or 0 in extra:
        return None
    n, m = h20_int(c, N), h20_int([(-x) % N for x in c], N)
    return (n, 3 - n - m, m)

def fedorov_int(a, b, N):
    alpha = sorted([0] + [(-x) % N for x in b])
    beta = sorted((-x) % N for x in a)
    rho = [sum(1 for al in alpha if al < be) - (i + 1) for i, be in enumerate(beta)]
    hi, lo = max(rho), min(rho)
    return tuple(rho.count(q) for q in range(hi, lo - 1, -1))

def scan(N, one_integral_b):
    vals = list(range(1, N))
    bvals = [(b, 0) for b in vals] if one_integral_b else list(combinations_with_replacement(vals, 2))
    tested = cases = mismatch = shift_only = 0
    orient = {"dual": 0, "same": 0, "palindromic": 0}
    for a in combinations_with_replacement(vals, 3):
        perms = set(permutations(a))
        for (b1, b2) in bvals:
            if any((x - y) % N == 0 for x in a for y in (b1, b2)):
                continue                          # reducible
            tested += 1
            for k in units(N):
                ak = tuple((k * x) % N for x in a); bk = ((k * b1) % N, (k * b2) % N)
                f = fedorov_int(ak, bk, N)
                triples = set()
                for (x1, x2, x3) in perms:
                    for (y1, y2) in {(b1, b2), (b2, b1)}:
                        t = surface_int(k * x1, k * x2, k * x3, k * y1, k * y2, N)
                        if t is not None:
                            triples.add(t)
                if not triples:
                    continue
                cases += 1
                st = {strip(t) for t in triples}
                if len(triples) > 1 and len(st) == 1:
                    shift_only += 1
                fs, fr = strip(f), strip(f[::-1])
                if st == {fs} == {fr}: orient["palindromic"] += 1
                elif st == {fr}: orient["dual"] += 1
                elif st == {fs}: orient["same"] += 1
                else: mismatch += 1
    return {"N": N, "one_lower_parameter_equal_to_1": one_integral_b, "parameter_sets": tested,
            "conjugate_cases_compared": cases, "cases_where_role_assignments_differ_by_a_shift_only": shift_only,
            "mismatches": mismatch, "orientation_counts": orient}

# cross-check the integer implementation against the Fraction one on the target
for k in units(9):
    t_int = {surface_int(k * x1, k * x2, k * x3, k * y1, k * y2, 9)
             for (x1, x2, x3) in set(permutations((1, 4, 5))) for (y1, y2) in ((3, 0), (0, 3))} - {None}
    ok &= sorted(map(list, t_int)) == [list(t) for t in hrep[str(k)]["surface_(h20,h11,h02)_over_all_role_assignments"]]
    ok &= list(fedorov_int(tuple((k * x) % 9 for x in (1, 4, 5)), ((3 * k) % 9, 0), 9)) == hrep[str(k)]["fedorov_top_to_bottom"]
res["integer_and_fraction_implementations_agree_on_H"] = bool(ok)

FULL = "--full" in sys.argv
scans = []
for N in ((3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 18) if FULL else (3, 4, 5, 6, 7, 8, 9, 10, 12)):
    scans.append(scan(N, True))
for N in ((3, 4, 5, 6, 7, 8, 9, 10) if FULL else (3, 4, 5, 6, 7, 8, 9)):
    scans.append(scan(N, False))
res["scans"] = scans
tot = {"parameter_sets": sum(s["parameter_sets"] for s in scans),
       "conjugate_cases_compared": sum(s["conjugate_cases_compared"] for s in scans),
       "mismatches": sum(s["mismatches"] for s in scans)}
for key in ("dual", "same", "palindromic"):
    tot[key] = sum(s["orientation_counts"][key] for s in scans)
res["scan_totals"] = tot
ok &= tot["mismatches"] == 0 and tot["same"] == 0

res["all_checks_pass"] = bool(ok)
res["full_scan"] = FULL
res["cpu_seconds"] = round(time.process_time() - T0, 2)
print(json.dumps(res, indent=1))
sys.exit(0 if ok else 1)
