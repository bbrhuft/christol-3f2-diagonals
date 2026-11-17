"""Check of the example in Appendix C (supplied by the referee of version 1.3).

    2F1(1/2, 116/11; 105/11; x) = (1-x)^(-1/2) + (11/210) x (1-x)^(-3/2)

is algebraic, although its parameters are reducible (116/11 - 105/11 = 1) and its
coefficient denominators contain primes (3, 5, 7, ...) that divide no parameter
denominator.  So the 'Eisenstein evidence' used for reducible cases in the search of
Appendix C is evidence only, not an obstruction to algebraicity.
Exact rational arithmetic, standard library only.  Usage: python3 -I eisenstein_counterexample.py
"""
import sys, os
from fractions import Fraction as Fr
from math import comb

N = 120
a, b, c = Fr(1, 2), Fr(116, 11), Fr(105, 11)
lhs, t = [], Fr(1)
for n in range(N):
    lhs.append(t)
    t = t * (a + n) * (b + n) / ((c + n) * (n + 1))

def binom_series(alpha, n):  # [x^n] (1-x)^(-alpha)
    r = Fr(1)
    for i in range(n):
        r = r * (alpha + i) / (i + 1)
    return r

rhs = [binom_series(Fr(1, 2), n) + (Fr(11, 210) * binom_series(Fr(3, 2), n - 1) if n >= 1 else 0)
       for n in range(N)]
ok = lhs == rhs
print('identity holds to order', N, ':', ok)
print('first coefficient:', lhs[1])
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'search'))
from hyp import classify, eisenstein_outside_primes
T, B = [a, b], [c, Fr(1)]
print('classifier verdict:', classify(T, B)[0])
print('outside primes in denominators up to n = 80:', sorted(eisenstein_outside_primes([a, b], [c, Fr(1)]))[:12], '...')
sys.exit(0 if ok and lhs[1] == Fr(58, 105) else 1)
