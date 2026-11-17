"""Rerun the computations quoted in the paper and compare them with the stored outputs.

Usage, from the 'supplementary' directory:   python3 scripts/verify.py [--full]
Standard library only; exact arithmetic.  Timing fields and the one labelled
floating-point illustration are ignored in the comparison.
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = "--full" in sys.argv
VOLATILE = ("cpu_seconds", "legendre_contour_illustration_float", "minors_approx")

def strip(d):
    if isinstance(d, dict):
        return {k: strip(v) for k, v in d.items() if k not in VOLATILE}
    if isinstance(d, list):
        return [strip(x) for x in d]
    return d

jobs = [("monodromy_hermitian.py", [], "monodromy_hermitian.json",
         "Section 8.1 (i)-(vi): monodromy, hermitian form, signatures, Gram determinant 3^36"),
        ("hodge_L2_count.py", [], "hodge_L2_count.json",
         "Appendix A: Hodge numbers for H, three controls and 9,086 parameter sets"),
        ("mechanism_controls.py", [], "mechanism_controls.json",
         "Remark 7.2, Proposition D (order 60), closed form of rho in Proposition 3.1")]
if FULL:
    jobs.append(("hodge_L2_count.py", ["--full"], "hodge_L2_count_full.json",
                 "Appendix A, full scan: 38,164 parameter sets, 221,946 conjugate cases"))
fails = 0
for script, args, stored, desc in jobs:
    p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", script), *args],
                       capture_output=True, text=True, cwd=ROOT)
    try:
        new = strip(json.loads(p.stdout))
        old = strip(json.load(open(os.path.join(ROOT, "results", stored))))
        ok = p.returncode == 0 and new == old and new.get("all_checks_pass") is True
    except Exception as exc:  # noqa
        ok = False
        desc += " (" + repr(exc) + ")"
    print(("PASS: " if ok else "FAIL: ") + desc)
    fails += not ok
print("ALL CHECKS PASSED" if fails == 0 else f"{fails} CHECK(S) FAILED")
sys.exit(1 if fails else 0)
