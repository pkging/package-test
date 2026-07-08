# package-test

This repository is a dedicated integration target for the reusable workflow in lbetz/ci-workflows.

## CI Pinning

The workflow is pinned to:

- reusable workflow: lbetz/ci-workflows/.github/workflows/package.yml@main
- ci_workflows_ref input: main

The complete package pipeline, including tag-gating, matrix expansion, build, test, and Pulp upload, now lives in lbetz/ci-workflows/.github/workflows/package.yml@main.

The Pulp upload job runs only on tag pushes that match `semver-<text>`, for example `1.0.0-main` or `2.7.4-rc2`.
For manual testing, you can use workflow_dispatch with run_upload=true.
Manual runs default to ci-rpm-test and ci-deb-test so production repos stay untouched.

## What It Builds

- RPM package from package-test.spec
- DEB package from the debian/ directory

## Upstream Source

- Remote upstream repository: lbetz/package-test-upstream
- Local upstream seed in this workspace: src/package-test-upstream

The package installs a test binary:

- /usr/bin/ci-workflow-package-test
