"""Audit of the 'not algebraic (BH)' verdicts in Appendix C (families (i) and (ii), target H).
Each excluded case is put in one of:
  P0  irreducible after cancelling equal parameters, no polynomial factor removed,
      the only integer lower parameter equals 1 -> Beukers-Heckman Thm 4.8 applies verbatim
  P1  as P0 but polynomial factors (b+m)_n/(b)_n removed           -> needs Lemma C.1(a)
  P2  integer lower parameter(s) present but none equal to 1 after reduction -> needs Lemma C.1(b)
  P3  more than one integer lower parameter (interlacing fails trivially)    -> Lemma C.1 (Jordan block)
Also re-derives every count from scratch (re-runs the classification, not the search).
"""
import sys, collections
from fractions import Fraction as Fr
from itertools import combinations_with_replacement as cwr
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'search'))
from hyp import classify, interlace

def detail(T, B):
    T = [Fr(x) for x in T]; B = [Fr(x) for x in B]
    for t in list(T):
        if t in B: T.remove(t); B.remove(t)
    poly = False; changed = True
    while changed:
        changed = False
        for t in T:
            for b in B:
                m = t - b
                if m.denominator == 1 and m >= 1:
                    T.remove(t); B.remove(b); poly = True; changed = True; break
            if changed: break
    ints = [b for b in B if b.denominator == 1]
    if len(ints) >= 2: return 'P3'
    if ints and ints[0] != 1: return 'P2'
    return 'P1' if poly else 'P0'

a = [Fr(1,9), Fr(4,9), Fr(5,9)]; b = Fr(1,3)
# family (i)
cnt = collections.Counter(); sub = collections.Counter()
As = sorted({Fr(p,q) for q in range(1,37) for p in range(-4*q,4*q+1) if not (Fr(p,q)<=0 and Fr(p,q).denominator==1)})
for k in range(1,9):
    for A in As:
        T = a + [(A+i)/k for i in range(k)]; B = [b, Fr(1)] + [(A+i)/(k+1) for i in range(k+1)]
        v,_,_ = classify(T,B); cnt[v]+=1
        if v == 'not algebraic (BH)': sub[detail(T,B)] += 1
print('family (i):', dict(cnt), 'subtypes of BH exclusions:', dict(sub))
# family (ii): psi side and phi side
grid = [Fr(j,18) for j in range(1,37)]
def psi_fast(S, R):
    T = list(S); B = [Fr(1)] + list(R)
    for t in list(T):
        if t in B: T.remove(t); B.remove(t)
    if not T: return 'algebraic (rational)', None
    if any((t-x).denominator == 1 for t in T for x in B): return 'skip', None
    if not any(x.denominator == 1 for x in B): return 'skip', None
    Bn = [Fr(1) if x.denominator == 1 else x for x in B]
    return ('algebraic (BH)' if interlace(T, Bn) else 'not algebraic (BH)'), (T, B)
cpsi = collections.Counter(); psisub = collections.Counter(); cphi = collections.Counter(); phisub = collections.Counter()
for p in range(1,4):
    for S in cwr(grid, p):
        for R in cwr(grid, p-1):
            v, tb = psi_fast(S, R); cpsi[v] += 1
            if v == 'not algebraic (BH)':
                psisub[detail(list(S), [Fr(1)]+list(R))] += 1
                continue
            if v not in ('algebraic (BH)', 'algebraic (rational)'): continue
            phiT, phiB = a + list(R), [b, Fr(1)] + list(S)
            w,_,_ = classify(phiT, phiB); cphi[w] += 1
            if w == 'not algebraic (BH)': phisub[detail(phiT, phiB)] += 1
print('family (ii) psi:', dict(cpsi), 'subtypes of psi exclusions:', dict(psisub))
print('family (ii) phi:', dict(cphi), 'subtypes of phi exclusions:', dict(phisub))

# ---- comparison with the counts stated in Appendix C of the paper (version 1.4)
expected = {
    'family (i)': ({'not algebraic (BH)': 25266, 'not algebraic (Eis)': 46}, {'P0': 25221, 'P1': 43, 'P2': 2}),
    'psi': ({'algebraic (BH)': 34600, 'algebraic (rational)': 703, 'skip': 1457968, 'not algebraic (BH)': 4149117},
            {'P0': 3658432, 'P3': 472957, 'P2': 17728}),
    'phi': ({'not algebraic (BH)': 31495, 'not algebraic (Eis)': 3808}, {'P0': 28783, 'P3': 703, 'P1': 2009}),
}
got = {'family (i)': (dict(cnt), dict(sub)), 'psi': (dict(cpsi), dict(psisub)), 'phi': (dict(cphi), dict(phisub))}
ok = got == expected
print('counts agree with Appendix C:', ok)
sys.exit(0 if ok else 1)
