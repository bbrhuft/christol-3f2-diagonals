"""Exact tools for the weight-one verification stage (standard library only).

Field K = Q(zeta), zeta = exp(2 pi i/9), realised as Q[z]/(z^6 + z^3 + 1).
Elements are tuples of 6 Fractions (coefficients of 1, z, ..., z^5).
Real inequalities are certified with rational interval arithmetic: the three
real numbers cos(2 pi k/9), k = 1, 2, 4, are the roots of 8c^3 - 6c + 1 and are
enclosed by exact bisection; no floating point is used for any claimed sign.
"""
from fractions import Fraction as Fr
from math import gcd

DEG = 6
ZERO = tuple(Fr(0) for _ in range(DEG))
ONE = (Fr(1),) + tuple(Fr(0) for _ in range(DEG - 1))


def K(*c):
    c = [Fr(x) for x in c] + [Fr(0)] * (DEG - len(c))
    return tuple(c[:DEG])


def zpow(k):
    """zeta^k for any integer k."""
    k %= 9
    # z^6 = -z^3 - 1, z^7 = -z^4 - z, z^8 = -z^5 - z^2
    if k < 6:
        return tuple(Fr(1) if i == k else Fr(0) for i in range(DEG))
    out = [Fr(0)] * DEG
    out[k - 3] = Fr(-1)
    out[k - 6] = Fr(-1)
    return tuple(out)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def scal(q, a):
    q = Fr(q)
    return tuple(q * x for x in a)


def mul(a, b):
    prod = [Fr(0)] * (2 * DEG - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    prod[i + j] += x * y
    for d in range(2 * DEG - 2, DEG - 1, -1):      # reduce z^d = -z^(d-3) - z^(d-6)
        c = prod[d]
        if c:
            prod[d] = Fr(0)
            prod[d - 3] -= c
            prod[d - 6] -= c
    return tuple(prod[:DEG])


def galois(a, k):
    """sigma_k : zeta -> zeta^k (k coprime to 9)."""
    out = ZERO
    for i, x in enumerate(a):
        if x:
            out = add(out, scal(x, zpow(i * k)))
    return out


def conj(a):
    return galois(a, -1)


def is_zero(a):
    return all(x == 0 for x in a)


def solve_rational(M, rhs):
    """Solve a square rational system by Gauss-Jordan; M nonsingular."""
    n = len(M)
    A = [list(map(Fr, M[i])) + [Fr(rhs[i])] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        A[c] = [x / piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[i][n] for i in range(n)]


def inv(a):
    if is_zero(a):
        raise ZeroDivisionError
    cols = [mul(a, zpow(j)) for j in range(DEG)]          # multiplication-by-a matrix
    M = [[cols[j][i] for j in range(DEG)] for i in range(DEG)]
    return tuple(solve_rational(M, list(ONE)))


def div(a, b):
    return mul(a, inv(b))


# ---------------------------------------------------------------- matrices over K
def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = [[ZERO] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            s = ZERO
            for k in range(m):
                s = add(s, mul(A[i][k], B[k][j]))
            out[i][j] = s
    return out


def mat_add(A, B):
    return [[add(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]


def mat_sub(A, B):
    return [[sub(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]


def mat_scal(c, A):
    return [[mul(c, x) for x in r] for r in A]


def mat_id(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def mat_T(A):
    return [list(r) for r in zip(*A)]


def mat_star(A):
    """conjugate transpose."""
    return [[conj(x) for x in r] for r in mat_T(A)]


def mat_galois(A, k):
    return [[galois(x, k) for x in r] for r in A]


def mat_is_zero(A):
    return all(is_zero(x) for r in A for x in r)


def mat_eq(A, B):
    return mat_is_zero(mat_sub(A, B))


def mat_pow(A, e):
    R = mat_id(len(A))
    for _ in range(e):
        R = mat_mul(R, A)
    return R


def rref(A):
    """Reduced row echelon form over K; returns (R, pivot_columns)."""
    A = [list(r) for r in A]
    rows, cols = len(A), len(A[0])
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if not is_zero(A[i][c])), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        iv = inv(A[r][c])
        A[r] = [mul(iv, x) for x in A[r]]
        for i in range(rows):
            if i != r and not is_zero(A[i][c]):
                f = A[i][c]
                A[i] = [sub(x, mul(f, y)) for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return A, piv


def rank(A):
    return len(rref(A)[1])


def nullspace(A):
    R, piv = rref(A)
    cols = len(A[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [ZERO] * cols
        v[f] = ONE
        for i, pc in enumerate(piv):
            v[pc] = neg(R[i][f])
        basis.append(v)
    return basis


def det3(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    t1 = mul(a, sub(mul(e, i), mul(f, h)))
    t2 = mul(b, sub(mul(d, i), mul(f, g)))
    t3 = mul(c, sub(mul(d, h), mul(e, g)))
    return add(sub(t1, t2), t3)


def mat_inv3(A):
    """inverse via solving A X = I column by column (rref of augmented matrix)."""
    n = len(A)
    aug = [list(A[i]) + mat_id(n)[i] for i in range(n)]
    R, piv = rref(aug)
    assert piv == list(range(n))
    return [r[n:] for r in R]


def companion(coeffs):
    """Companion matrix of t^n + c_{n-1} t^{n-1} + ... + c_0, coeffs = [c_0, ..., c_{n-1}]."""
    n = len(coeffs)
    M = [[ZERO] * n for _ in range(n)]
    for i in range(1, n):
        M[i][i - 1] = ONE
    for i in range(n):
        M[i][n - 1] = neg(coeffs[i])
    return M


def poly_from_roots(roots):
    """monic polynomial prod (t - r); returns [c_0, ..., c_{n-1}] (without leading 1)."""
    p = [ONE]                                   # low -> high
    for r in roots:
        q = [ZERO] * (len(p) + 1)
        for i, c in enumerate(p):
            q[i + 1] = add(q[i + 1], c)
            q[i] = sub(q[i], mul(r, c))
        p = q
    return p[:-1]


def is_integral(a):
    """a in Z[zeta]  (the power basis 1..z^5 is an integral basis of Z[zeta_9])."""
    return all(x.denominator == 1 for x in a)


def fmt(a):
    terms = []
    for i, x in enumerate(a):
        if x:
            terms.append((str(x) if i == 0 else (("" if x == 1 else "-" if x == -1 else str(x) + "*") + ("z" if i == 1 else f"z^{i}"))))
    return " + ".join(terms).replace("+ -", "- ") if terms else "0"


# ---------------------------------------------------------------- certified real embeddings
def _bisect_root(lo, hi, steps=200):
    f = lambda c: 8 * c ** 3 - 6 * c + 1
    flo = f(lo)
    assert flo * f(hi) < 0
    for _ in range(steps):
        mid = (lo + hi) / 2
        fm = f(mid)
        if fm == 0:
            return mid, mid
        if (fm > 0) == (flo > 0):
            lo = mid
        else:
            hi = mid
    return lo, hi

# cos(2pi/9) in (3/4, 4/5), cos(4pi/9) in (1/10, 1/4), cos(8pi/9) in (-1, -9/10)
_C = {1: _bisect_root(Fr(3, 4), Fr(4, 5)), 2: _bisect_root(Fr(1, 10), Fr(1, 4)), 4: _bisect_root(Fr(-1), Fr(-9, 10))}


def cos_interval(j):
    """certified enclosure of cos(2 pi j/9)."""
    j %= 9
    if j == 0:
        return Fr(1), Fr(1)
    if j in (3, 6):
        return Fr(-1, 2), Fr(-1, 2)
    j = min(j, 9 - j)          # 1, 2 or 4
    return _C[j]


def real_part_interval(a, k):
    """certified enclosure of Re sigma_k(a) = sum a_i cos(2 pi k i/9)."""
    lo = hi = Fr(0)
    for i, x in enumerate(a):
        if x:
            cl, ch = cos_interval(k * i)
            if x > 0:
                lo += x * cl; hi += x * ch
            else:
                lo += x * ch; hi += x * cl
    return lo, hi


def is_real(a):
    return is_zero(sub(a, conj(a)))


def certified_sign(a, k):
    """sign of sigma_k(a) for a real element (a = conj(a)); 0 only if a == 0."""
    assert is_real(a)
    if is_zero(a):
        return 0
    lo, hi = real_part_interval(a, k)
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    raise ArithmeticError("interval too wide")


def approx(a, k):
    lo, hi = real_part_interval(a, k)
    return float((lo + hi) / 2)
