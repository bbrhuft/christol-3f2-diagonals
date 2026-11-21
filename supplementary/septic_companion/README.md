# S7 quartic reconstruction, v1.1

The PDF and TeX give a standalone construction. Sections 1–4 reconstruct the marked germ and its period. Section 5 constructs the polarized integral weight-one realization and proves algebraicity. Section 6 proves existence of a generic unmarked plane quartic over Q(x). Section 7 reports exact and numerical tests. The rational functions giving such a global quartic have yet to be calculated.

## Reproduce the checks

Use Python 3.10 or later. The versions for this revision are in rerun/versions.txt. The original Opus audit is enclosed unchanged in S7_quartic_audit_checks.zip. From the extracted revision bundle:

    python -m pip install python-flint sympy mpmath numpy
    python -m zipfile -e S7_quartic_audit_checks.zip audit
    mkdir regenerated
    cd regenerated
    python ../audit/dump_series.py 100
    python ../jet_certificate.py series_N100.json
    python -c "import json; assert json.load(open('series_N100.json')) == json.load(open('../audit/series_N100.json'))"
    cd ..
    python geometry_checks.py
    python marking.py
    python quartic.py --order 26

For direct numerical period checks use the commands below. The second command uses Python solely to express the three points on the ray with cs² positive. The quadrature program takes complex input rounded through binary floating point and reports relative discrepancies, with no certified numerical error bound.

    python audit/period_check_v.py audit/series_N100.json "0.45+0.1j" 60
    python -c "import cmath,math,subprocess,sys; pts=','.join(str(r*cmath.exp(3j*math.pi/14)) for r in [.8,.9,1.]);subprocess.run([sys.executable,'audit/period_check_v.py','audit/series_N100.json',pts,'100','gamma0'],check=True)"

## Evidence

- The two reconstruction codes use different expansions. The original quartic.py is symbolic in two constants and specializes them at the end. The audit reconstruct.py uses a direct implicit-root lift in exact rational arithmetic. Its dump_series.py regenerates the nine coefficient functions and eighteen entries of the marked period matrix from the initial data.
- jet_certificate.py multiplies the six columns by the differential coefficients, restores s², and checks the Euler recurrence of the original operator on the six resulting jets. It also checks all nine congruence classes of exponents.
- geometry_checks.py verifies the matrix of B on the orbit lattice, invariance of H, the transvection and spanning identities, and the obstruction to a character twist between the rank-three summands. The proof of descent is in the note.
- rerun/ contains the results from this revision. The Padé and denominator files are exploratory and have no role in the proofs. SHA256SUMS.txt inventories the bundle contents.
