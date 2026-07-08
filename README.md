# package-test

This repository is a dedicated integration target for the reusable workflow in lbetz/ci-workflows.

## CI Pinning

The workflow is pinned to:

- reusable workflow: lbetz/ci-workflows/.github/workflows/build.yml@main
- ci_workflows_ref input: main

## What It Builds

- RPM package from package-test.spec
- DEB package from the debian/ directory

## Upstream Source

- Remote upstream repository: lbetz/package-test-upstream
- Local upstream seed in this workspace: src/package-test-upstream

The package installs a test binary:

- /usr/bin/ci-workflow-package-test
