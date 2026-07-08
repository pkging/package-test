#!/usr/bin/env bash
set -euo pipefail

source /workspace/.ci-workflows/hooks/lib/distro.sh
source /workspace/.ci-workflows/hooks/lib/common.sh || true

log "package-test pre_test hook on distro: $ID"
