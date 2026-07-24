%global debug_package %{nil}

Name:           ci-workflow-package-test
Version:        1.0.0
Release:        1%{?dist}
Summary:        Test package for reusable ci-workflows pipeline
License:        GPL-2.0+
URL:            https://github.com/lbetz/package-test-upstream
Source0:        https://github.com/lbetz/package-test-upstream/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

%description
Small test package used to validate ci-workflows RPM and DEB pipelines.

%prep
%setup -q -n package-test-upstream-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ci-workflow-package-test %{buildroot}%{_bindir}/ci-workflow-package-test

%files
%{_bindir}/ci-workflow-package-test

%changelog
* Wed Jul 08 2026 Lennart Betz <lbetz@prefork.de> 1.0.0-1
- Initial test package for reusable ci-workflows validation
