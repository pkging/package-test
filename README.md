# package-test

This repository is a dedicated integration target for the reusable workflow in pkging/ci-workflows.

## CI Pinning

The workflow is pinned to:

- reusable workflow: pkging/ci-workflows/.github/workflows/package.yml@main
- ci_workflows_ref input: main

The complete package pipeline, including tag-gating, matrix expansion, build, test, and Pulp upload, now lives in pkging/ci-workflows/.github/workflows/package.yml@main.

The Pulp upload job runs only on tag pushes that match `semver-<text>`, for example `1.0.0-main` or `2.7.4-rc2`.
For manual testing, you can use workflow_dispatch with run_upload=true.
Target resolution is now centralized in ci-workflows via TARGET_TYPE/TARGET_FAMILY/TARGET_VERSION derived from the distro matrix.
Debian-based builds keep distro-specific version suffixes so `debian12` and `ubuntu24` uploads can coexist in their mapped APT targets.

## What It Builds

- RPM package from package-test.spec
- DEB package from the debian/ directory

## Upstream Source

- Remote upstream repository: pkging/package-test-upstream
- Local upstream seed in this workspace: src/package-test-upstream

The package installs a test binary:

- /usr/bin/ci-workflow-package-test
