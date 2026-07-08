#!/usr/bin/env bash
set -euo pipefail

TEST_BIN=/usr/bin/ci-workflow-package-test

if [ ! -x "$TEST_BIN" ]; then
  echo "ERROR: $TEST_BIN is missing or not executable" >&2
  exit 1
fi

"$TEST_BIN" --help >/dev/null 2>&1 || true

echo "Smoke test passed: $TEST_BIN exists"
