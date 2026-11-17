#!/bin/sh
# Reproduce every check reported in Appendix B of the paper (version 1.4).
# Usage:  sh run_checks.sh            (from the folder 'supplementary'; about 5 minutes)
#         sh run_checks.sh --quick    (skips the two longer audits; about 15 seconds)
# Requirements: Python >= 3.8; NumPy for the search audits.  Exit status 0 iff all checks pass.
set -e
cd "$(dirname "$0")"
echo "== python version"; python3 --version
echo "== scripts/verify.py --full";            python3 -I scripts/verify.py --full
echo "== scripts/hadamard_identities.py";      python3 -I scripts/hadamard_identities.py
echo "== scripts/eisenstein_counterexample.py"; python3 -I scripts/eisenstein_counterexample.py
echo "== search/test_engine.py";               (cd search && python3 test_engine.py)
echo "== audit/audit_numerical.py";            python3 -I audit/audit_numerical.py
if [ "$1" != "--quick" ]; then
  echo "== audit/audit_exclusions.py";         python3 -I audit/audit_exclusions.py
  echo "== audit/rerun_numerical_A2_A4.py";    python3 -I audit/rerun_numerical_A2_A4.py
fi
echo "== ALL CHECKS COMPLETED"
