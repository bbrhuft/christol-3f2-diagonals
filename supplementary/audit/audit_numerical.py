"""Audit of the numerical families in Appendix C.
(1) Re-derive family sizes from the enumeration logic in family_ab.py / run_a3.py / run_b2.py.
(2) Bound |d_1| * den(d_1) to show d_1 = 0 (mod p) only if d_1 = 0 in Q.
    d_1 = [x y z] f (3 variables) or [u v] f (2 variables), f = prod F_j^{alpha_j}.
    |d_1| <= [monomial] prod (1 - |M_j|)^(-|alpha_j|), where F_j = 1 - M_j and |M_j| replaces each
    coefficient by its absolute value (|binom(alpha,k)| <= binom(|alpha|+k-1,k)).
    den(d_1) divides 9^3 * 3! (3 variables) or 9^2 * 2! (2 variables).
(3) Count survivors (candidates that passed the 7-coefficient screen) and their 50-term checks.
"""
import sys, itertools, json, collections
from fractions import Fraction as Fr
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'search'))
import family_ab as F

def canon3(forms): return F.canon3(forms)
forms4=[L for L in itertools.product(range(4),repeat=3) if any(L)]
forms3=[L for L in itertools.product(range(3),repeat=3) if any(L)]
forms2=[L for L in itertools.product(range(2),repeat=3) if any(L)]
pairs=sorted({canon3(c) for c in itertools.combinations(forms4,2)})
triples=sorted({canon3(c) for c in itertools.combinations(forms3,3)})
quads=sorted({canon3(c) for c in itertools.combinations(forms2,4)})
shortB=sorted({min(q,(q[1],q[0],q[2],q[4],q[3])) for q in itertools.product([0,-1,-2,-4],[0,-1,-2,-4],[0,-1,1],[0,1],[0]) if any(q)})
qs=[q for q in itertools.product([0,1,-1,-2,-3,-4],[0,1,-1,-2,-3,-4],[-2,-1,0,1,2],[0,1,-1],[0,1,-1]) if any(q)]
qs=sorted({min(q,(q[1],q[0],q[2],q[4],q[3])) for q in qs})
nB3=len(list(itertools.combinations(shortB,3))); nB2=len(qs)*(len(qs)-1)//2
E=lambda lim: 18*lim
sizes={'A2':len(pairs)*E(3)**2,'A3':len(triples)*E(2)**3,'A4':len(quads)*E(1)**4,'B2':nB2*E(2)**2,'B3':nB3*E(1)**3}
print('sets:',{'A2':len(pairs),'A3':len(triples),'A4':len(quads),'B2':nB2,'B3':nB3})
print('sizes:',sizes,'total',sum(sizes.values()))

# (2) majorant bound
def series_coeff(maj_terms, m, target, nvars):
    """[target] (1 - S)^(-m), S = sum c_e x^e (c_e >= 0); m rational >= 0."""
    from math import factorial
    deg=sum(target); total=Fr(0)
    # expand sum_k (m)_k/k! S^k, k <= deg
    poly={tuple([0]*nvars):Fr(1)}; pk={tuple([0]*nvars):Fr(1)}
    coef=Fr(0)
    for k in range(0,deg+1):
        if k>0:
            new={}
            for e1,c1 in pk.items():
                for e2,c2 in maj_terms.items():
                    e=tuple(a+b for a,b in zip(e1,e2))
                    if all(a<=t for a,t in zip(e,target)): new[e]=new.get(e,0)+c1*c2
            pk=new
        poch=Fr(1)
        for i in range(k): poch*= (m+i)
        coef+= poch/factorial(k)*pk.get(tuple(target),0)
    return coef
p=2147483647
fam={
 'A2':(3,{(1,0,0):3,(0,1,0):3,(0,0,1):3},2*3,(1,1,1),9**3*6),
 'A3':(3,{(1,0,0):2,(0,1,0):2,(0,0,1):2},3*2,(1,1,1),9**3*6),
 'A4':(3,{(1,0,0):1,(0,1,0):1,(0,0,1):1},4*1,(1,1,1),9**3*6),
 'B2':(2,{(1,0):4,(0,1):4,(1,1):2,(2,0):1,(0,2):1},2*2,(1,1),9**2*2),
 'B3':(2,{(1,0):4,(0,1):4,(1,1):1,(2,0):1},3*1,(1,1),9**2*2),
}
for k,(nv,S,m,t,den) in fam.items():
    B=series_coeff(S,Fr(m),t,nv)
    print(f'{k}: |d_1| <= {B}, den | {den}, |numerator| <= {B*den} < p: {B*den < p}')
# (3) survivors
d=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'search', 'results_numerical_all.json')))
c=collections.Counter((h['family'],h['target']) for h in d['hits'])
print('survivors total',len(d['hits']),'all verified to 50 mod P2:',all(h['verified_to_50_mod_P2'] for h in d['hits']))
for k,v in sorted(c.items()): print('  ',k,v)

# ---- comparison with the statements of Appendix C (version 1.4)
ok = (sum(sizes.values()) == 924172092
      and all(series_coeff(S, Fr(m), t, nv) * den < p for (nv, S, m, t, den) in fam.values())
      and max(series_coeff(S, Fr(m), t, nv) * den for (nv, S, m, t, den) in fam.values()) == 39680928
      and len(d['hits']) == 312 and all(h['verified_to_50_mod_P2'] for h in d['hits'])
      and not any(h['target'] == '3F2(1/9,4/9,5/9;1/3,1)' for h in d['hits']))
print('statements of Appendix C confirmed:', ok)
sys.exit(0 if ok else 1)
