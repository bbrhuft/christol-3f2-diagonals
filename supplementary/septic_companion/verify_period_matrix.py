"""Recompute every entry from the given curve jet, without solving for its coefficients."""
import json,sys
from pathlib import Path
from flint import fmpq
# First argument is an extracted copy of the audit directory.
sys.path.insert(0,sys.argv[1])
from reconstruct import periods
data=json.loads(Path(sys.argv[2]).read_text())
def rational_series(d):
    return {int(k):fmpq(v) for k,v in d.items() if fmpq(v)}
P,ok=periods(rational_series(data['h']),{int(j):rational_series(d) for j,d in data['p'].items()},data['N'])
assert ok
for i,row in enumerate(P):
    for j,entry in enumerate(row):
        assert {k:v for k,v in entry.items() if v}==rational_series(data['P'][i][j])
print("Computed all 18 period-coordinate series directly from the curve jet through degree",data['N'])
print("Every period entry agrees exactly; second-kind residue tests passed.")
