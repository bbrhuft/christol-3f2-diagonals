#!/bin/sh
# Reproduce the checks reported in Appendix B of the paper (version 1.5).
# Usage (from the folder 'supplementary'):
#   sh run_checks.sh            default: all checks below, about 5 minutes
#   sh run_checks.sh --quick    skips the two longer audits and the failure-propagation test (~20 s)
# Optional, not part of the default (about 8 minutes):
#   python3 -I audit/audit_numerical.py --recompute-survivors
# Requirements: Python >= 3.8; NumPy for the search tests and audits.
# Exit status 0 iff every check passes; the first failing check stops the run with status 1.
cd "$(dirname "$0")" || exit 1
run() {
  label="$1"; shift
  echo "== $label"
  if "$@"; then :; else
    status=$?
    echo "== FAILED: $label (exit status $status)"
    exit 1
  fi
}
run "python version"                         python3 --version
run "scripts/verify.py --full"               python3 -I scripts/verify.py --full
run "scripts/hadamard_identities.py"         python3 -I scripts/hadamard_identities.py
run "scripts/eisenstein_counterexample.py"   python3 -I scripts/eisenstein_counterexample.py
run "search/test_engine.py"                  sh -c 'cd search && exec python3 test_engine.py'
run "search/test_symmetry.py"                sh -c 'cd search && exec python3 test_symmetry.py'
run "audit/audit_numerical.py (stored survivor records; bound and counts recomputed)" python3 -I audit/audit_numerical.py
if [ "$1" != "--quick" ]; then
  run "audit/audit_exclusions.py"            python3 -I audit/audit_exclusions.py
  run "audit/rerun_numerical_A2_A4.py"       python3 -I audit/rerun_numerical_A2_A4.py
  run "audit/check_failure_propagation.sh"   sh audit/check_failure_propagation.sh
fi
echo "== ALL CHECKS PASSED"
exit 0
