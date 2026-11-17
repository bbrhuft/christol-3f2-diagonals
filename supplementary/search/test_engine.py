"""Test of the modular diagonal engine (made enforcing in version 1.5).

Positive control: f = (1-x-y)^(2/3) (1-x-y-z)^(-1), whose diagonal is
3F2(1/9,4/9,7/9;1/3,1;27x) (Abdelaziz-Koutschan-Maillard 2020).  Its diagonal coefficients
and scale-free invariants must match the target.
Negative control: the same factors with exponents (1/2, -1) must NOT match the target.
Exit status 0 iff both expectations hold.  Usage (from this folder): python3 test_engine.py
"""
import sys
import numpy as np
from fractions import Fraction as Fr
from engine import diagonal, hyp_coeffs_mod, invariants, target_invariants, P1

p = P1
r = lambda q: Fr(q).numerator * pow(Fr(q).denominator, p - 2, p) % p
F1 = {(0, 0, 0): 1, (1, 0, 0): -1, (0, 1, 0): -1}
F2 = {(0, 0, 0): 1, (1, 0, 0): -1, (0, 1, 0): -1, (0, 0, 1): -1}
# column 0: exponents (2/3, -1) (positive control); column 1: exponents (1/2, -1) (negative control)
al = np.array([[r('2/3'), r('1/2')], [r(-1), r(-1)]], dtype=np.int64)
d = diagonal([F1, F2], al, 8, 3)
h = hyp_coeffs_mod([(1, 9), (4, 9), (7, 9)], (1, 3), 8, p)
coeffs_pos = [int(d[n, 0]) for n in range(9)]
coeffs_target = [h[n] * pow(27, n, p) % p for n in range(9)]
I, good = invariants(d, p)
T = target_invariants([(1, 9), (4, 9), (7, 9)], (1, 3), 8, p)
inv_pos = bool(good[0]) and tuple(int(x) for x in I[:, 0]) == T
inv_neg = bool(good[1]) and tuple(int(x) for x in I[:, 1]) == T

fails = []
for name, ok in [('positive control: coefficients equal 3F2(1/9,4/9,7/9;1/3,1;27x) to order 8', coeffs_pos == coeffs_target),
                 ('positive control: invariants match the target', inv_pos),
                 ('negative control: invariants do not match the target', not inv_neg)]:
    print(('PASS: ' if ok else 'FAIL: ') + name)
    if not ok:
        fails.append(name)
print('ENGINE TEST PASSED' if not fails else f'{len(fails)} FAILURE(S)')
sys.exit(1 if fails else 0)
