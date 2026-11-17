"""Diagonal coefficients of products of powers of polynomials, modulo a prime.

f = prod_j F_j^(alpha_j),  F_j in Z[x_1..x_n] with F_j(0) = 1,  alpha_j rational.
With Q = prod F_j and P_v = sum_j alpha_j (d F_j/d x_v) prod_{i != j} F_i we have
    Q * d f/d x_v = P_v * f,
which gives each coefficient f_e from coefficients of lower total degree:
    (m_v + 1) f_{m+u_v} = sum_q P_{v,q} f_{m-q} - sum_{q != 0} Q_q (m_v - q_v + 1) f_{m-q+u_v}.
All arithmetic is mod p and vectorized over a grid of exponent vectors alpha.
Only the box [0, N]^n is needed for the diagonal coefficients d_0..d_N.
"""
import numpy as np
from itertools import product

P1 = 2147483647          # 2^31 - 1
P2 = 2147483629          # second prime below 2^31


def polymul(A, B):
    C = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            C[e] = C.get(e, 0) + ca * cb
    return {e: c for e, c in C.items() if c}


def deriv(A, v):
    D = {}
    for e, c in A.items():
        if e[v] > 0:
            e2 = list(e); e2[v] -= 1
            D[tuple(e2)] = D.get(tuple(e2), 0) + c * e[v]
    return D


def prepare(factors, nvars):
    one = {tuple([0] * nvars): 1}
    Q = one
    for F in factors:
        Q = polymul(Q, F)
    S = []  # S[j][v] = dF_j/dx_v * prod_{i!=j} F_i
    for j, F in enumerate(factors):
        rest = one
        for i, G in enumerate(factors):
            if i != j:
                rest = polymul(rest, G)
        S.append([polymul(deriv(F, v), rest) for v in range(nvars)])
    Qnz = [(e, c) for e, c in Q.items() if any(e)]
    return Qnz, S


def diagonal(factors, alphas, N, nvars, p=P1):
    """alphas: array shape (k, G) of residues mod p. Returns array (N+1, G) of d_n mod p."""
    k, G = alphas.shape
    Qnz, S = prepare(factors, nvars)
    inv = [0] + [pow(i, p - 2, p) for i in range(1, N + 2)]
    f = {}
    zero = tuple([0] * nvars)
    f[zero] = np.ones(G, dtype=np.int64)
    idx = sorted(product(range(N + 1), repeat=nvars), key=sum)
    for e in idx:
        if e == zero:
            continue
        v = next(i for i in range(nvars) if e[i] > 0)
        m = list(e); m[v] -= 1; m = tuple(m)
        acc = np.zeros(G, dtype=np.int64)
        for j in range(k):
            inner = np.zeros(G, dtype=np.int64)
            for q, c in S[j][v].items():
                src = tuple(a - b for a, b in zip(m, q))
                if min(src) < 0:
                    continue
                inner += c * f[src]
            inner %= p
            acc = (acc + alphas[j] * inner) % p
        sub = np.zeros(G, dtype=np.int64)
        for q, c in Qnz:
            src = list(a - b for a, b in zip(m, q)); src[v] += 1; src = tuple(src)
            if min(src) < 0:
                continue
            coef = c * (m[v] - q[v] + 1)
            if coef:
                sub += coef * f[src]
        sub %= p
        f[e] = ((acc - sub) % p) * inv[m[v] + 1] % p
    return np.stack([f[tuple([n] * nvars)] for n in range(N + 1)])


def powvec(x, e, p):
    r = np.ones_like(x)
    b = x % p
    while e:
        if e & 1:
            r = r * b % p
        b = b * b % p
        e >>= 1
    return r


def invariants(d, p):
    """I_j = d_j / d_1^j for j >= 2; rows where d_1 == 0 get -1."""
    d1 = d[1]
    good = d1 != 0
    inv1 = powvec(np.where(good, d1, 1), p - 2, p)
    out = []
    pw = np.ones_like(d1)
    for j in range(2, d.shape[0]):
        pw = pw * inv1 % p if j > 2 else inv1 * inv1 % p
        out.append(np.where(good, d[j] * pw % p, -1))
    return np.stack(out), good


def hyp_coeffs_mod(a, b, N, p):
    """Coefficients of 3F2(a; b, 1; x) mod p; a, b as (num, den)."""
    def r(x):
        return x[0] * pow(x[1], p - 2, p) % p
    c = [1]
    for n in range(N):
        t = c[-1]
        for x in a:
            t = t * ((r(x) + n) % p) % p
        t = t * pow((r(b) + n) % p * (n + 1) * (n + 1) % p, p - 2, p) % p
        c.append(t)
    return c


def target_invariants(a, b, N, p):
    t = hyp_coeffs_mod(a, b, N, p)
    inv1 = pow(t[1], p - 2, p)
    return tuple(t[j] * pow(inv1, j, p) % p for j in range(2, N + 1))
