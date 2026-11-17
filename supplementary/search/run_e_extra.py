from fractions import Fraction as Fr
import family_ce as M
for name,(a,b) in {"3F2(2/9,5/9,8/9;1/3,1)":(["2/9","5/9","8/9"],"1/3"),"3F2(1/9,4/9,7/9;2/3,1)":(["1/9","4/9","7/9"],"2/3")}.items():
    c,h,u=M.family_e(a,b,[Fr(j,18) for j in range(1,37)])
    print(name, "Hadamard splits found:", len(h), "| unresolved:", len(u))
    for x in h[:3]: print("   ", x["psi_top"], x["psi_bottom"], "->", x["phi_top_reduced"], x["phi_bottom_reduced"])
