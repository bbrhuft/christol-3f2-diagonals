import numpy as np, time
from fractions import Fraction as Fr
from engine import *
p=P1
r=lambda q: Fr(q).numerator*pow(Fr(q).denominator,p-2,p)%p
# positive control: (1-x-y)^(2/3) (1-x-y-z)^(-1) -> 3F2(1/9,4/9,7/9;1/3,1;27x)
F1={(0,0,0):1,(1,0,0):-1,(0,1,0):-1}
F2={(0,0,0):1,(1,0,0):-1,(0,1,0):-1,(0,0,1):-1}
al=np.array([[r('2/3'),r('1/2')],[r(-1),r(-1)]],dtype=np.int64)
t=time.time(); d=diagonal([F1,F2],al,8,3); print('time',time.time()-t)
h=hyp_coeffs_mod([(1,9),(4,9),(7,9)],(1,3),8,p)
print([int(d[n,0]) for n in range(9)])
print([h[n]*pow(27,n,p)%p for n in range(9)])
I,good=invariants(d,p)
T=target_invariants([(1,9),(4,9),(7,9)],(1,3),8,p)
print('match col0', tuple(int(x) for x in I[:,0])==T, 'col1', tuple(int(x) for x in I[:,1])==T)
