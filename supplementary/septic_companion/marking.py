"""Exact cyclotomic, polarization and cycle normalization checks using SymPy."""
import sympy as S
z = S.Symbol("z")
cyclo = S.cyclotomic_poly(7,z)
def red(expr):
    n,d = S.fraction(S.cancel(expr))
    return S.rem(n*S.invert(d,cyclo,z),cyclo,z).expand()

# sin(pi*j/7) ratios: v=exp(pi*i/7)=-z^4.
v = -z**4
def sine(j):
    return red(v**j-v**(-j))
def trig_ratio(k,q,b):
    return red((z**3-1)/(z**q-1)*(sine(1)/sine(b))**2*(1+z)/(1+z**k))
assert red(trig_ratio(2,6,2)-z**(-2)) == 0
assert red(trig_ratio(4,5,3)-z) == 0
print("Gamma reflection and duplication residual cyclotomic identities verified.")
print("lambda=-5*2^(-8/7)*zeta^(-2); mu=-2^(-17/7)*zeta.")
print("c=-2^(-6/7)*zeta^2; mu*c^3=1/32; c^7=-1/64.")
# Central star of branch arcs: consecutive differences intersect with signs +-1.
base = [0,0,0,1,-1,0,0]   # order-seven generator u -> zeta^5 u
target = [2*base[i]+base[(i-1)%7]+base[(i+1)%7] for i in range(7)]
r = S.sqrt(-7)
w = (r-1)/2
k=(7+r)/2
A = S.Matrix([[0,0,1],[1,0,-w.conjugate()],[0,1,w]])
B = S.Matrix([[0,0,-1],[1,0,1],[0,1,1]])
H = S.Matrix([[0,k,r],[k.conjugate(),0,k],[-r,k.conjugate(),0]])
v0 = S.Matrix([-1,0,1])/r
assert (B**2-S.eye(3))[:,0]==v0*r
p = v0
for i in range(7):
    val = S.simplify((v0.H*H*p)[0])
    assert S.simplify((val-val.conjugate())/r)==target[i]
    p=(A*p).applyfunc(S.simplify)
gram=S.Matrix([[target[(j-i)%7] for j in range(6)] for i in range(6)])
assert gram.det()==1
print("Intersection first row, including the redundant seventh translate:",target)
print("Determinant of first six translates:",gram.det())
