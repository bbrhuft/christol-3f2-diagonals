"""Check the complete supplied rational jet, its weights and its PF identity."""
from fractions import Fraction as Q
from pathlib import Path
import json, sys
data=json.loads(Path(sys.argv[1]).read_text())
n=data['N']
def series(d):
    return {int(j):Q(v) for j,v in d.items() if Q(v)}
def mul(p,q):
    r={}
    for i,v in p.items():
        for j,w in q.items():
            if i+j<=n:
                r[i+j]=r.get(i+j,0)+v*w
    return {i:v for i,v in r.items() if v}
def add(p,q):
    r=p.copy()
    for i,v in q.items():
        r[i]=r.get(i,0)+v
    return {i:v for i,v in r.items() if v}
coeff=[series(p) for p in data['b']]
pars=[series(data['h'])]+[series(data['p'][str(i)]) for i in range(1,6)]
weights=[1,10,6,2,12,8,8,4,0]
assert all(all(i%14==weight for i in p) for weight,p in zip(weights,pars+coeff))
P=[[series(p) for p in row] for row in data['P']]
flat=[]
for j in range(6):
    p={}
    for i in range(3):
        p=add(p,mul(coeff[i],P[i][j]))
    flat.append({i+2:v for i,v in p.items()})
lead={2:(2,Q(1)),4:(8,Q(1,32)),5:(4,Q(5,4))}
for j,p in enumerate(flat):
    if j in lead:
        m,val=lead[j]
        assert min(p)==m and p[m]==val
    else:
        assert not p
    for d in range(n+3):
        assert (d-2)*(d-4)*(d-8)*p.get(d,0)==Q((d-14)**2*(d-7),64)*p.get(d-14,0)
print(f"All nine weights hold through s^{n}.")
print(f"All six de Rham components satisfy the original pulled-back numerator through s^{n+2}, including the three prescribed nonzero leading terms.")
