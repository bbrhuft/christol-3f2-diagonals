"""Exact integral representation and finite-index commutant inputs. Requires SymPy."""
import sympy as S
r=S.sqrt(-7); w=(r-1)/2; k=(7+r)/2
A=S.Matrix([[0,0,1],[1,0,-S.conjugate(w)],[0,1,w]])
B=S.Matrix([[0,0,-1],[1,0,1],[0,1,1]])
H=S.Matrix([[0,k,r],[S.conjugate(k),0,k],[-r,S.conjugate(k),0]])
def red(m):
    return m.applyfunc(S.simplify)
def restriction(column):
    imag=red((column-column.conjugate())/r)
    return red(column-w*imag).col_join(imag)
v=S.Matrix([-1,0,1]); vstar=v/r
cols=[vstar]
for i in range(5):
    cols.append(red(A*cols[-1]))
P=S.Matrix.hstack(*(restriction(z) for z in cols))
BB=P.inv()*S.Matrix.hstack(*(restriction(B*z) for z in cols))
assert all(z.is_Integer for z in BB) and abs(BB.det())==1
assert red(A.H*H*A)==H and red(B.H*H*B)==H
assert S.simplify(H.det())==49 and H[0,0]==0
assert red(A**7)==S.eye(3) and red(A+A**2+A**4)==w*S.eye(3)
N=B**2-S.eye(3)
assert N==v*S.ones(1,3) and N*N==S.zeros(3)
assert S.simplify(S.Matrix.hstack(v,A*v,A**2*v).det())==r
assert S.simplify((v.H*H*A*v)[0])==7
assert all({(e+j)%7 for e in [1,2,4]}!={3,5,6} for j in range(7))
print("B in the integral A-orbit basis:")
print(BB)
print("Both generators preserve the Hermitian form; det(H)=49 and e1 is isotropic.")
print("Transvection span determinant sqrt(-7), consecutive pairing 7, no scalar twist at A.")
