import itertools, json, numpy as np
import family_ab as F
log=open('family_a3.log','a')
forms3=[L for L in itertools.product(range(3),repeat=3) if any(L)]
triples=sorted({F.canon3(c) for c in itertools.combinations(forms3,3)})
h,n=F.run_family("A3",3,[[F.lin3(L) for L in c] for c in triples],2,log)
for x in h: x["verified_to_50_mod_P2"]=F.verify(x,3)
json.dump({"sizes":{"A3":n},"hits":h},open("results_family_a3.json","w"),indent=1)
log.write("done\n")
