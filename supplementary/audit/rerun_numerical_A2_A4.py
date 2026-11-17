"""Partial rerun of the numerical search of Appendix C: families A2 and A4 only.
Recomputes every candidate of these two families from scratch and compares the set of
survivors with the stored output search/results_numerical_all.json.
Requires NumPy.  Usage (from the folder supplementary):  python3 -I audit/rerun_numerical_A2_A4.py
"""
import os, sys, json, itertools, io
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'search'))
import family_ab as F

forms4 = [L for L in itertools.product(range(4), repeat=3) if any(L)]
forms2 = [L for L in itertools.product(range(2), repeat=3) if any(L)]
pairs = sorted({F.canon3(c) for c in itertools.combinations(forms4, 2)})
quads = sorted({F.canon3(c) for c in itertools.combinations(forms2, 4)})
log = io.StringIO()
key = lambda h: (h['family'], json.dumps(h['factors']), tuple(h['exponents']), h['target'])
new = []
for label, sets, lim in [('A2', pairs, 3), ('A4', quads, 1)]:
    hits, n = F.run_family(label, 3, [[F.lin3(L) for L in c] for c in sets], lim, log)
    print(f'{label}: {n} candidates, {len(hits)} survivors')
    new += hits
stored = json.load(open(os.path.join(here, '..', 'search', 'results_numerical_all.json')))['hits']
old = {key(h) for h in stored if h['family'] in ('A2', 'A4')}
newk = {key(h) for h in new}
print('survivors identical to stored output:', newk == old, f'({len(newk)} new, {len(old)} stored)')
sys.exit(0 if newk == old else 1)
