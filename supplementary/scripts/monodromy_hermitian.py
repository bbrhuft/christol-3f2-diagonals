"""Step 3 certificate: Levelt monodromy matrices of L_H over Z[zeta_9], local structure,
and the monodromy-invariant hermitian form (existence, uniqueness, nondegeneracy, signatures).

H = 3F2(1/9,4/9,5/9; 1/3,1; x).  Following Beukers-Heckman (Levelt's theorem), with
a_j = e(alpha_j) for the upper and b_j = e(beta_j) for the lower parameters (including the 1
from n!), A and B are the companion matrices of prod(t - a_j) and prod(t - b_j), and
    h_infinity = A,   h_0 = B^{-1},   h_1 = A^{-1} B.
Everything is exact in Q(zeta_9); signs at real places are certified by rational intervals.
"""
import json, os, sys
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from w1_tools import *

res = {}
ok = True
z = zpow(1)
w3 = zpow(3)                                     # e(1/3)

A = companion(poly_from_roots([zpow(1), zpow(4), zpow(5)]))
B = companion(poly_from_roots([zpow(3), ONE, ONE]))
Ai, Bi = mat_inv3(A), mat_inv3(B)
I3 = mat_id(3)
M0, M1, Minf = Bi, mat_mul(Ai, B), A

res["A"] = [[fmt(x) for x in r] for r in A]
res["B"] = [[fmt(x) for x in r] for r in B]
res["entries_of_A_B_and_inverses_in_Z[zeta]"] = all(is_integral(x) for M in (A, B, Ai, Bi) for r in M for x in r)
ok &= res["entries_of_A_B_and_inverses_in_Z[zeta]"]
res["product_relation_Minf*M1*M0_is_identity"] = mat_eq(mat_mul(mat_mul(Minf, M1), M0), I3)
ok &= res["product_relation_Minf*M1*M0_is_identity"]

# --- local monodromy at 0: one Jordan block J_2(1) plus the eigenvalue e(-1/3)
N0 = mat_sub(M0, I3)
S0 = mat_sub(M0, mat_scal(zpow(-3), I3))
res["M0_minimal_poly_is_(t-1)^2(t-e(-1/3))"] = (mat_is_zero(mat_mul(mat_mul(N0, N0), S0))
                                                 and not mat_is_zero(mat_mul(N0, S0)))
res["rank(M0-1)"] = rank(N0)
M0c = mat_pow(M0, 3)
Nc = mat_sub(M0c, I3)
res["M0^3_unipotent_(M0^3-1)^2=0"] = mat_is_zero(mat_mul(Nc, Nc))
res["rank(M0^3-1)"] = rank(Nc)
ok &= res["M0_minimal_poly_is_(t-1)^2(t-e(-1/3))"] and res["rank(M0-1)"] == 2
ok &= res["M0^3_unipotent_(M0^3-1)^2=0"] and res["rank(M0^3-1)"] == 1

# --- local monodromy at 1 and infinity
res["rank(M1-1)"] = rank(mat_sub(M1, I3))
res["det(M1)"] = fmt(det3(M1))
res["det(M1)_equals_e(2/9)"] = det3(M1) == zpow(2)
res["M1^9_is_identity"] = mat_eq(mat_pow(M1, 9), I3)
res["Minf^9_is_identity"] = mat_eq(mat_pow(Minf, 9), I3)
ok &= res["rank(M1-1)"] == 1 and res["det(M1)_equals_e(2/9)"] and res["M1^9_is_identity"] and res["Minf^9_is_identity"]

# --- irreducibility over the algebraic closure is the Beukers-Heckman criterion a_i != b_j:
res["no_common_eigenvalue_of_A_and_B"] = all(x != y for x in (zpow(1), zpow(4), zpow(5)) for y in (zpow(3), ONE))
ok &= res["no_common_eigenvalue_of_A_and_B"]

# --- invariant sesquilinear forms X with M^* X M = X for M = A, B (K-linear in the 9 entries of X)
def invariance_rows(M):
    Ms = mat_star(M)
    rows = []
    for i in range(3):
        for j in range(3):
            row = [ZERO] * 9
            for k in range(3):
                for l in range(3):
                    row[3 * k + l] = add(row[3 * k + l], mul(Ms[i][k], M[l][j]))
            row[3 * i + j] = sub(row[3 * i + j], ONE)
            rows.append(row)
    return rows

ns = nullspace(invariance_rows(A) + invariance_rows(B))
res["dim_K_of_invariant_sesquilinear_forms"] = len(ns)
ok &= len(ns) == 1
X0 = [ns[0][0:3], ns[0][3:6], ns[0][6:9]]
Hm = mat_add(X0, mat_star(X0))
if mat_is_zero(Hm):
    Hm = mat_scal(sub(z, conj(z)), X0)
# clear denominators / normalise: scale by a rational so entries are integral with content 1
den = 1
for r in Hm:
    for x in r:
        for c in x:
            den = den * c.denominator // gcd(den, c.denominator)
Hm = [[scal(den, x) for x in r] for r in Hm]
g = 0
for r in Hm:
    for x in r:
        for c in x:
            g = gcd(g, abs(c.numerator))
Hm = [[scal(Fr(1, g), x) for x in r] for r in Hm]
res["h"] = [[fmt(x) for x in r] for r in Hm]
res["h_is_hermitian"] = mat_eq(Hm, mat_star(Hm))
res["h_invariant_under_A_and_B"] = all(mat_eq(mat_mul(mat_mul(mat_star(M), Hm), M), Hm) for M in (A, B))
d = det3(Hm)
res["det(h)"] = fmt(d)
res["det(h)_nonzero"] = not is_zero(d)
res["det(h)_real"] = is_real(d)
ok &= res["h_is_hermitian"] and res["h_invariant_under_A_and_B"] and res["det(h)_nonzero"]

# --- signatures at the three complex places (k and -k give the same signature)
def minors(Hx):
    d1 = Hx[0][0]
    d2 = sub(mul(Hx[0][0], Hx[1][1]), mul(Hx[0][1], Hx[1][0]))
    return [d1, d2, det3(Hx)]

sig = {}
for k in (1, 2, 4, 5, 7, 8):
    # sigma_k(h) is the hermitian matrix of the conjugate local system L_k; certified signs of
    # its leading principal minors give the signature by Jacobi's rule (all minors nonzero).
    ms = minors(Hm)
    signs = [certified_sign(m, k) for m in ms]
    assert all(s != 0 for s in signs)
    seq = [1] + signs
    negs = sum(1 for i in range(3) if seq[i] * seq[i + 1] < 0)
    sig[str(k)] = {"minor_signs": signs, "signature_(pos,neg)": [3 - negs, negs],
                   "minors_approx": [approx(m, k) for m in ms]}
res["signatures"] = sig
res["all_places_indefinite_with_|p-q|=1"] = all(sorted(v["signature_(pos,neg)"]) == [1, 2] for v in sig.values())
ok &= res["all_places_indefinite_with_|p-q|=1"]

# --- the invariant line Im(M0^3 - 1): fixed by M0 and h-isotropic.  The form is (x, y) -> x^* h y,
#     which is the convention under which M^* h M = h expresses invariance.
def form(x, y):
    s_ = ZERO
    for i in range(3):
        for j in range(3):
            s_ = add(s_, mul(mul(conj(x[i]), Hm[i][j]), y[j]))
    return s_

def apply(M, v):
    return [add(add(mul(M[i][0], v[0]), mul(M[i][1], v[1])), mul(M[i][2], v[2])) for i in range(3)]

col = next([Nc[i][j] for i in range(3)] for j in range(3) if not all(is_zero(Nc[i][j]) for i in range(3)))
res["generator_v_of_Im(M0^3-1)"] = [fmt(x) for x in col]
res["h(v,v)"] = fmt(form(col, col))
res["Im(M0^3-1)_isotropic"] = is_zero(form(col, col))
res["Im(M0^3-1)_fixed_by_M0"] = all(is_zero(sub(a_, b_)) for a_, b_ in zip(apply(M0, col), col))
ok &= res["Im(M0^3-1)_isotropic"] and res["Im(M0^3-1)_fixed_by_M0"]

# --- sign patterns: eta = a + b*theta + c*theta^2 in K^+ with prescribed signs at the 3 real places
theta = add(z, conj(z))
patterns = {}
from itertools import product
for target in product((1, -1), repeat=3):
    found = None
    for a_, b_, c_ in product(range(-3, 4), repeat=3):
        eta = add(add(scal(a_, ONE), scal(b_, theta)), scal(c_, mul(theta, theta)))
        if is_zero(eta):
            continue
        try:
            if all(certified_sign(eta, k) == s for k, s in zip((1, 2, 4), target)):
                found = [a_, b_, c_]; break
        except ArithmeticError:
            continue
    patterns["".join("+" if s > 0 else "-" for s in target)] = found
res["sign_patterns_eta=(a,b,c)"] = patterns
res["all_8_sign_patterns_realised"] = all(v is not None for v in patterns.values())
ok &= res["all_8_sign_patterns_realised"]
# xi0 = zeta - zeta^{-1} is purely imaginary with Im sigma_k(xi0) = 2 sin(2 pi k/9) > 0 for k = 1,2,4
xi0 = sub(z, conj(z))
res["xi0_anti-invariant"] = is_zero(add(xi0, conj(xi0)))
ok &= res["xi0_anti-invariant"]

# --- the alternating Q-form psi = Tr_{K/Q}(xi * x^* h y) on V_Q = K^3 with xi = zeta - zeta^{-1}:
#     integrality on the lattice Z[zeta]^3, invariance, nondegeneracy (18 x 18 Gram determinant).
def trace(a):
    # Tr_{K/Q}: Tr(1) = 6, Tr(z^3) = -3, Tr(z^j) = 0 for j = 1, 2, 4, 5
    return 6 * a[0] - 3 * a[3]

basis = []
for j in range(3):
    for i in range(6):
        v = [ZERO, ZERO, ZERO]
        v[j] = zpow(i)
        basis.append(v)
gram = [[trace(mul(xi0, form(x, y))) for y in basis] for x in basis]
res["psi_integral_on_Z[zeta]^3"] = all(g_.denominator == 1 for r in gram for g_ in r)
res["psi_alternating"] = all(gram[i][j] == -gram[j][i] for i in range(18) for j in range(18))
def det_rational(M):
    M = [list(r) for r in M]
    n = len(M); d = Fr(1)
    for c in range(n):
        p_ = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p_ is None:
            return Fr(0)
        if p_ != c:
            M[c], M[p_] = M[p_], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            if M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d
dg = det_rational(gram)
res["det_Gram(psi)"] = str(dg)
res["psi_nondegenerate"] = dg != 0
def psi_invariant(M):
    return all(trace(mul(xi0, form(apply(M, x), apply(M, y)))) == gram[i][j]
               for i, x in enumerate(basis) for j, y in enumerate(basis))
res["psi_invariant_under_A_and_B"] = psi_invariant(A) and psi_invariant(B)
ok &= res["psi_integral_on_Z[zeta]^3"] and res["psi_alternating"] and res["psi_nondegenerate"] and res["psi_invariant_under_A_and_B"]

# --- required sign of eta (xi = eta * xi0) at the places k = 1, 4, 7; eta is called lambda in the paper.
#     For psi(x,y) = Tr(xi x^* h y) and X in F^1 (paper, proof of Theorem 4.3, Step 3):
#         i psi_C(X, Xbar) = - sum_k i sigma_k(xi) <X_k, X_k>_k ,   <a,b>_k = a^* sigma_k(h) b,
#     so positivity needs  -i sigma_k(xi) * (sign of sigma_k(h) on the top Hodge piece of S_k) > 0.
#     i*sigma_k(xi0) = -2 sin(2 pi k/9): negative for k = 1, 2, 4 and positive for k = 5, 7, 8.
def required_eta_signs(top_dim):            # top_dim[k] = rank of the top Hodge piece of L_k
    out = {}
    for k in (1, 4, 7):                      # one representative of each conjugate pair
        pos, negn = sig[str(k)]["signature_(pos,neg)"]
        sign_h_on_top = 1 if pos == top_dim[k] else -1
        sign_i_xi0 = -1 if k in (1, 2, 4) else 1
        place = k if k in (1, 2, 4) else 9 - k          # sigma_k(eta) = sigma_{9-k}(eta)
        out[place] = -sign_h_on_top * sign_i_xi0         # need sigma_place(eta) of this sign
    return "".join("+" if out[p_] > 0 else "-" for p_ in (1, 2, 4))
patA = required_eta_signs({1: 1, 4: 1, 7: 1})
patB = required_eta_signs({1: 2, 4: 2, 7: 2})
res["eta_sign_pattern_if_top_rank_1_at_k=1,4,7"] = patA
res["eta_sign_pattern_if_top_rank_2_at_k=1,4,7"] = patB
res["explicit_eta_for_each_convention"] = [patterns[patA], patterns[patB]]
res["required_signs_uniform_so_plus_or_minus_psi0_is_a_polarization"] = {patA, patB} == {"+++", "---"}
ok &= res["required_signs_uniform_so_plus_or_minus_psi0_is_a_polarization"]

res["all_checks_pass"] = bool(ok)
print(json.dumps(res, indent=1))
sys.exit(0 if ok else 1)
