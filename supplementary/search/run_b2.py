import itertools, json, sys
import family_ab as F
part=int(sys.argv[1]); nparts=int(sys.argv[2])
log=open(f'family_b2_{part}.log','a')
qs=[q for q in itertools.product([0,1,-1,-2,-3,-4],[0,1,-1,-2,-3,-4],[-2,-1,0,1,2],[0,1,-1],[0,1,-1]) if any(q)]
qs=sorted({min(q,(q[1],q[0],q[2],q[4],q[3])) for q in qs})
pairs=list(itertools.combinations(qs,2))[part::nparts]
h,n=F.run_family("B2",2,[[F.quad2(*x),F.quad2(*y)] for x,y in pairs],2,log)
for x in h: x["verified_to_50_mod_P2"]=F.verify(x,2)
json.dump({"sizes":{"B2":n},"hits":h},open(f"results_family_b2_{part}.json","w"),indent=1)
log.write("done\n")
