"""Exact curve, canonical differential and Gauss-Manin jet at the S7 boundary.
Run with Python 3 (standard library). The two formal constants X=mu*c^3 and
Y=c^7 are independent. Keys store powers of (s,u,v,X,Y).
"""
import argparse
from collections import defaultdict
from fractions import Fraction as R
from functools import lru_cache
from math import comb, prod

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--order",type=int,default=16,help="even precision in s, at least 4")
order = parser.parse_args().order
if order < 4 or order%2:
    parser.error("choose an even order >= 4")
cap = order+2


def atom(value=1,s=0,u=0,v=0,x=0,y=0):
    return {(s,u,v,x,y): R(value)} if value else {}


def clean(a):
    return {k:v for k,v in a.items() if v}


def add(*args):
    out = defaultdict(R)
    for a in args:
        for k,v in a.items():
            out[k] += v
    return clean(out)


def scale(a,c):
    return clean({k:v*c for k,v in a.items()})


def mul(a,b):
    out = defaultdict(R)
    for (s,u,v,x,y),w in a.items():
        for (S,U,V,X,Y),W in b.items():
            if s+S<=cap:
                out[s+S,u+U,v+V,x+X,y+Y] += w*W
    return clean(out)


def power(a,n):
    out = atom()
    for _ in range(n):
        out = mul(out,a)
    return out


def select(a,n):
    return {k:v for k,v in a.items() if k[0]==n}


def shift(a,ds):
    return {(s+ds,u,v,x,y):w for (s,u,v,x,y),w in a.items() if s+ds<=cap}


def inverse_unit(a):
    step = add(atom(),scale(a,-1))
    assert all(k[0]>0 for k in step)
    term = out = atom()
    while term:
        term = mul(term,step)
        out = add(out,term)
    return out


def frobenius(j):
    a = {}
    val = R(1)
    for n in range(cap//14+1):
        a.update(atom(val,s=14*n,y=n))
        d = j+7*n
        val *= -R(d*d)*(d+R(7,2))/prod(d+7-e for e in (1,2,4))
    return a


H = {j:frobenius(j) for j in (1,2,4)}
a = mul(atom(R(5,4),s=2),mul(H[2],inverse_unit(H[1])))
b = mul(atom(s=6,x=1),mul(H[4],inverse_unit(H[1])))

@lru_cache(None)
def half_binom(twice,n):
    return prod((R(twice,2)-i)/(i+1) for i in range(n))


@lru_cache(None)
def reduce(j,d):
    """Class of u^j v^(2d-1)du relative to e_(j%7), on v^2=u^7-1."""
    if j%7==6:
        return R(0)
    if d>0:
        return sum((-1)**(d-i)*comb(d,i)*reduce(j+7*i,0) for i in range(d+1))
    val = prod((R(2*(j+1),7*(2*i-1))-1 for i in range(1,-d+1)),start=R(1))
    while j>=7:
        val *= R(2*(j-6),2*j-5)
        j -= 7
    return val


def curve_data(h,p):
    z = add(atom(u=2),mul(h,atom(v=1)))
    # G is the change in the radicand at fixed u and formal v
    g = add(mul(atom(u=1),power(z,3)),atom(-1,u=7))
    for j in range(1,6):
        g = add(g,mul(p[j],mul(atom(u=j%2),power(z,j//2))))
    return z,g


def periods(h,p):
    z,g = curve_data(h,p)
    numerators = [atom(),atom(u=1),z]
    out = [[defaultdict(R) for j in range(6)] for i in range(3)]
    gp = atom()
    n = 0
    while gp:
        for i,num in enumerate(numerators):
            for (s,j,k,x,y),w in mul(num,gp).items():
                if k%2 or j%7==6: # odd-k residues are polynomial; index six is exact
                    continue
                val = half_binom(k-1,n)*reduce(j,k//2-n)
                out[i][j%7][s,0,0,x,y] += val*w
        gp = mul(gp,g)
        n += 1
    return [[clean(col) for col in row] for row in out]


def discrepancies(P):
    out = {}
    for i,row in enumerate(P):
        for j,want in [(3,add(scale(mul(a,row[0]),R(1,5)),scale(mul(b,row[1]),R(1,3)))),
                       (4,mul(b,row[2])),(5,mul(a,row[2]))]:
            out[i,j] = add(want,scale(row[j],-1))
    return out


p = {j:{} for j in range(1,6)}
h = atom(s=1)
for n in range(2,order+1,2):
    cap = n
    err = {ij:select(r,n) for ij,r in discrepancies(periods(h,p)).items()}
    delta_h2 = add(scale(err[0,3],4),scale(err[1,4],R(-4,3)))
    p[3] = add(p[3],scale(delta_h2,3),scale(err[0,3],-14))
    if n==2:
        assert not delta_h2
    else:
        h = add(h,shift(scale(delta_h2,R(1,2)),-1))
    for j,(i,k) in {1:(2,3),2:(1,3),4:(0,4),5:(0,5)}.items():
        p[j] = add(p[j],scale(err[i,k],R(14,5-2*k)))
    P = periods(h,p)
    assert all(not r for r in discrepancies(P).values())
print("All nine Hodge graph entries verified modulo s^%d." % (order+1))
print("Each line (s-degree, X-degree, Y-degree, coefficient). X=mu*c^3; Y=c^7.")
def output(name,poly):
    print(name,[(s,x,y,str(w)) for (s,u,v,x,y),w in sorted(poly.items())])
output("h",h)
for j in p:
    output("p%d"%j,p[j])

# Solve for canonical differential with e_0,e_1,e_2 coordinates (0,0,1).
d = [{},{},atom()]
for n in range(1,order+1):
    observed = [select(add(*(mul(d[i],P[i][j]) for i in range(3))),n) for j in range(3)]
    d = [add(d[j],scale(observed[j],-1)) for j in range(3)]
print("omega/(kappa*c*s^2) in the three adjunction forms:")
coeffs = [mul(H[1],term) for term in d]
for j,coef in enumerate(coeffs):
    output("coefficient %d"%j,coef)

# Independent period computation: Hensel-expand the actual moving root at fixed
# u. Write v_moving = V*W, where V^2=u^7-1, W(0)=1. Here keys can have negative
# V powers. This calculation uses no implicit-residue formula or graph inverse.
Z = atom(u=2)
V = atom(v=1)
U = atom(u=1)
W = atom()
for n in range(1,order+1):
    Z = add(atom(u=2),mul(h,mul(V,W)))
    Frel = add(mul(U,power(Z,3)),atom(-1,u=7))
    for j in p:
        Frel = add(Frel,mul(p[j],mul(atom(u=j%2),power(Z,j//2))))
    equation = add(power(W,2),atom(-1),scale(mul(atom(v=-2),Frel),-1))
    W = add(W,scale(select(equation,n),R(-1,2)))
Z = add(atom(u=2),mul(h,mul(V,W)))
Fz = mul(atom(3,u=1),power(Z,2))
for j in p:
    k = j//2
    if k:
        Fz = add(Fz,mul(p[j],mul(atom(k,u=j%2),power(Z,k-1))))
den = add(W,scale(mul(atom(v=-1),mul(h,Fz)),R(-1,2)))
num = add(coeffs[0],mul(coeffs[1],U),mul(coeffs[2],Z))
density = mul(atom(v=-1),mul(num,inverse_unit(den)))
# Scalar constant kappa*c suppressed. Multiplication by s^2 restored below.
classes = [defaultdict(R) for _ in range(6)]
for (s,j,k,x,y),w in density.items():
    if k%2==0:
        # An even negative V power must cancel or have a rational exact
        # primitive. Independent PF comparison below uses the odd projection.
        continue
    if j%7<6:
        classes[j%7][s,0,0,x,y] += w*reduce(j,(k+1)//2)
classes = [clean(col) for col in classes]
expected = [{},{},mul(atom(),H[1]),{},mul(atom(s=6,x=1),H[4]),mul(atom(R(5,4),s=2),H[2])]
assert all(add(aa,scale(bb,-1))=={} for aa,bb in zip(classes,expected))
# Check the even projection as a rational differential too. Reduce V^2=u^7-1,
# group by s,X,Y and clear denominators; polynomial differentials are exact.
even = defaultdict(list)
for (s,j,k,x,y),w in density.items():
    if k%2==0:
        even[s,x,y].append((j,k//2,w))
for terms in even.values():
    denom = max(0,-min(d for j,d,w in terms))
    numerator = defaultdict(R)
    for j,d,w in terms:
        for i in range(d+denom+1):
            numerator[j+7*i] += w*comb(d+denom,i)*(-1)**(d+denom-i)
    # Polynomial plus partial fractions with pole orders up to denom.
    # Rational primitives exist iff residues vanish at all seven simple roots.
    # For u^j/(u^7-1)^denom substitute q=u^7-1 near a root.
    if denom:
        res=defaultdict(R)
        for j,w in numerator.items():
            exponent=R(j-6,7)
            binom=prod((exponent-i)/(i+1) for i in range(denom-1))
            res[(j-6)%7] += w*binom
        assert not clean(res)

# Apply 8 times the pulled-back numerator operator by Euler coefficient action:
# (D-2)(D-4)(D-8)+Y*s^14*D^2*(D+7), with D=s*d/ds.
for col in classes:
    op=defaultdict(R)
    for (s,u,v,x,y),w in col.items():
        d=s+2
        op[d,x,y] += (d-2)*(d-4)*(d-8)*w
        if d+14<=order+2:
            op[d+14,x,y+1] += d*d*(d+7)*w
    assert not clean(op)
print("Independent moving-root de Rham reduction and original operator verified through s^%d."%(order+2))

def specialize(poly):
    row = defaultdict(R)
    for (s,u,v,x,y),w in poly.items():
        row[s] += w*R(1,32)**x*R(-1,64)**y
    return clean(row)

print("Rational S7 specialization for x=64/s^14:")
for name,poly in [("h",h)]+[("p%d"%j,p[j]) for j in p]+[("b%d"%j,q) for j,q in enumerate(coeffs)]:
    print(name,[(s,str(v)) for s,v in sorted(specialize(poly).items())])
