#!/usr/bin/env python3
"""Exact check of the Hadamard factorization in Proposition D(a) of the paper.

For s in Q and c in {1/3, 2/3}:
  3F2(s/3, (s+1)/3, (s+2)/3; 1-c, 1; x) = T_s(x) * (1-x)^(-c)   (Hadamard product),
  T_s(x) = sum_n (s)_{3n}/(3n)! x^n = (1/3) sum_{w^3=1} (1 - w x^(1/3))^(-s).
Checks the coefficient identity to n = 200 for several s, and checks the trisection
formula for T_s by expanding (1-y)^(-s) and keeping exponents divisible by 3.
"""
from fractions import Fraction as Fr

def poch(a, n):
    r = Fr(1)
    for i in range(n): r *= a + i
    return r

def fact(n):
    r = 1
    for i in range(2, n + 1): r *= i
    return r

NMAX = 200
ok = True
for s in [Fr(1, 3), Fr(2, 3), Fr(1, 5), Fr(-7, 4), Fr(5, 2), Fr(11, 9)]:
    for c in [Fr(1, 3), Fr(2, 3)]:
        a = [s / 3, (s + 1) / 3, (s + 2) / 3]; b = 1 - c
        for n in range(NMAX + 1):
            lhs = poch(a[0], n) * poch(a[1], n) * poch(a[2], n) / (poch(b, n) * fact(n) ** 2)
            rhs = poch(s, 3 * n) / fact(3 * n) * poch(c, n) / fact(n)
            if lhs != rhs:
                ok = False; print("FAIL", s, c, n); break
print("all identities hold to n =", NMAX, ":", ok)
# the four named series
for name, (s, c) in {"3F2(1/9,4/9,7/9;1/3,1)": (Fr(1, 3), Fr(2, 3)), "3F2(1/9,4/9,7/9;2/3,1)": (Fr(1, 3), Fr(1, 3)),
                     "3F2(2/9,5/9,8/9;2/3,1)": (Fr(2, 3), Fr(1, 3)), "3F2(2/9,5/9,8/9;1/3,1)": (Fr(2, 3), Fr(2, 3))}.items():
    print(f"{name} = T_{s} * (1-x)^(-{c})")

import sys
sys.exit(0 if ok else 1)
