"""Bounded supporting checks. No geometric existence or general theorem is certified here.
Standard-library only. Run from any directory: python tools/verify_extension.py.
"""
from fractions import Fraction as F
from math import prod, gcd, lcm
from collections import Counter
import random

cases = [
(['1/9','4/9','5/9'],['1/3']),
(['1/18','1/6','7/18','4/9'],['1/3','1/3']),
(['1/14','3/14','5/14','4/7'],['1/7','3/7']),
(['1/14','3/14','5/14','9/14','13/14'],['1/7','2/7','6/7'])]
checks=0
for astr,bstr in cases:
    a=list(map(F,astr));b=list(map(F,bstr))
    def R(t): return prod(t+x for x in a)
    def coeffs(m,N):
        c=[F(1)]
        for r in range(N):
            c.append(c[-1]*R(r)/(prod(r+x for x in b)*(r+m)*(r+1)))
        return c
    for m in [2,3,4,7,12]:
        q=m-1;prev=coeffs(m-1,61);cur=coeffs(m,60)
        assert R(-q)
        for r in range(61):
            S=(R(r)-R(-q))/(r+q)
            inverse=F(q)/R(-q)*((r+1)*prod(r+x for x in b)*prev[r+1]-S*prev[r])
            assert inverse==cur[r]
            assert (r+q)*cur[r]==q*prev[r]
            checks+=1
print('Inverse-contiguity coefficients:',checks,'passed; ranks 3,4,5; m=2,3,4,7,12.')

def frac(x):return x-(x.numerator//x.denominator)
def audit(a,b):
    N=lcm(*(x.denominator for x in a+b))
    all_nonneg=all_two=True
    for k in range(1,N):
        if gcd(k,N)!=1:continue
        aa=sorted(frac(k*x) for x in a);bb=sorted(frac(k*x) for x in b)
        values=[0]+[sum(x<=t for x in aa)-sum(x<=t for x in bb) for t in sorted(set(aa+bb))]
        alpha=[F(0),F(0)]+[1-x for x in bb];beta=sorted(1-x for x in aa)
        rho=[sum(x<y for x in alpha)-i for i,y in enumerate(beta,1)]
        assert min(values)==min(rho) and max(values)==max(rho)+1
        all_nonneg &= min(values)>=0
        all_two &= set(rho)=={0,1}
        for t in sorted(set(aa)):
            ids=[i for i,y in enumerate(beta,1) if y==1-t];p,q=min(ids),max(ids)
            left=sum(x<t for x in aa)-sum(x<t for x in bb)
            right=sum(x<=t for x in aa)-sum(x<=t for x in bb)
            assert left==rho[q-1] and right-1==rho[p-1]
        neg_a=[frac(-k*x) for x in a];neg_b=[frac(-k*x) for x in b]
        for t in sorted(set(aa+bb)):
            left=sum(x<t for x in aa)-sum(x<t for x in bb)
            reflected=sum(x<=1-t for x in neg_a)-sum(x<=1-t for x in neg_b)
            assert reflected==2-left
    assert all_nonneg==all_two
    if all_nonneg:
        assert max(Counter(a).values())<=2 and max(Counter(b).values())<=2
    return all_nonneg
rng=random.Random(20261120)
count=gb=0
while count<2000:
    n=rng.randrange(3,7);N=rng.randrange(3,19)
    grid=[F(j,N) for j in range(1,N)]
    b=rng.choices(grid,k=n-2);pool=[x for x in grid if x not in b]
    if not pool:continue
    a=rng.choices(pool,k=n)
    gb+=audit(a,b);count+=1
print('Counting/block/reflection checks:',count,'parameter multisets passed;',gb,'satisfy the GB criterion.')
print('These finite checks corroborate identities; they do not prove the arbitrary-rank geometric construction.')