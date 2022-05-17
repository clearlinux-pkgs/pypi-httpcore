#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-httpcore
Version  : 0.15.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/42/98/44c3e51a0655eae75adefee028c9bada7427a90f63105e54f5e735946f50/httpcore-0.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/98/44c3e51a0655eae75adefee028c9bada7427a90f63105e54f5e735946f50/httpcore-0.15.0.tar.gz
Summary  : A minimal low-level HTTP client.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-httpcore-license = %{version}-%{release}
Requires: pypi-httpcore-python = %{version}-%{release}
Requires: pypi-httpcore-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(anyio)
BuildRequires : pypi(certifi)
BuildRequires : pypi(h11)
BuildRequires : pypi(sniffio)

%description
# HTTP Core
[![Test Suite](https://github.com/encode/httpcore/workflows/Test%20Suite/badge.svg)](https://github.com/encode/httpcore/actions)
[![Package version](https://badge.fury.io/py/httpcore.svg)](https://pypi.org/project/httpcore/)

%package license
Summary: license components for the pypi-httpcore package.
Group: Default

%description license
license components for the pypi-httpcore package.


%package python
Summary: python components for the pypi-httpcore package.
Group: Default
Requires: pypi-httpcore-python3 = %{version}-%{release}

%description python
python components for the pypi-httpcore package.


%package python3
Summary: python3 components for the pypi-httpcore package.
Group: Default
Requires: python3-core
Provides: pypi(httpcore)
Requires: pypi(anyio)
Requires: pypi(certifi)
Requires: pypi(h11)
Requires: pypi(sniffio)

%description python3
python3 components for the pypi-httpcore package.


%prep
%setup -q -n httpcore-0.15.0
cd %{_builddir}/httpcore-0.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652803312
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . h11
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-httpcore
cp %{_builddir}/httpcore-0.15.0/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-httpcore/cc8ca9a1480585587761018c62aca50f1cbb0594
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} h11
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-httpcore/cc8ca9a1480585587761018c62aca50f1cbb0594

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
