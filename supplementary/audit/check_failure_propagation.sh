#!/bin/sh
# Failure-injection test for run_checks.sh (version 1.5).
# Copies the folder 'supplementary' to a temporary directory, injects one failed expectation at a
# time into the COPY (the preserved files are never modified), runs 'sh run_checks.sh --quick' on
# the copy and requires a nonzero exit status.  An unmodified copy must exit with status 0.
# Exit status 0 iff all expectations hold.
SRC="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)" || exit 1
trap 'rm -rf "$TMP"' EXIT INT TERM
fails=0
attempt() {   # attempt <label> <expected: pass|fail> <python injection code or empty>
  label="$1"; expect="$2"; inject="$3"
  rm -rf "$TMP/s"; cp -R "$SRC" "$TMP/s"
  if [ -n "$inject" ]; then
    (cd "$TMP/s" && python3 -c "$inject") || { echo "FAIL: could not inject ($label)"; fails=$((fails+1)); return; }
  fi
  if sh "$TMP/s/run_checks.sh" --quick > "$TMP/out.txt" 2>&1; then got=pass; else got=fail; fi
  if [ "$got" = "$expect" ]; then
    echo "PASS: $label -> run_checks.sh --quick ${got}ed as expected"
    [ "$got" = fail ] && grep "== FAILED" "$TMP/out.txt" | sed 's/^/        /'
  else echo "FAIL: $label -> expected $expect, got $got"; tail -5 "$TMP/out.txt"; fails=$((fails+1)); fi
}
sub='import sys
def sub(path, old, new):
    s = open(path).read()
    if s.count(old) < 1: sys.exit("pattern not found in " + path)
    open(path, "w").write(s.replace(old, new, 1))
'
attempt "unmodified copy" pass ""
attempt "positive control of search/test_engine.py broken" fail "$sub
sub('search/test_engine.py', \"r('2/3'), r('1/2')\", \"r('1/3'), r('1/2')\")"
attempt "negative control of search/test_engine.py made to match" fail "$sub
sub('search/test_engine.py', \"r('2/3'), r('1/2')\", \"r('2/3'), r('2/3')\")"
attempt "stored reference output results/mechanism_controls.json altered (copy only)" fail "$sub
sub('results/mechanism_controls.json', 'true', 'false')"
attempt "expected pool size in search/test_symmetry.py altered" fail "$sub
sub('search/test_symmetry.py', \"'B2 pool': 854\", \"'B2 pool': 853\")"
attempt "expected candidate total in audit/audit_numerical.py altered" fail "$sub
sub('audit/audit_numerical.py', 'sum(sizes.values()) == 924172092', 'sum(sizes.values()) == 924172093')"
if [ "$fails" -eq 0 ]; then echo "FAILURE PROPAGATION VERIFIED"; exit 0; fi
echo "$fails FAILURE-PROPAGATION CHECK(S) FAILED"; exit 1
