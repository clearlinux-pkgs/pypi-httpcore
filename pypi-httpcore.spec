#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-httpcore
Version  : 0.16.3
Release  : 51
URL      : https://files.pythonhosted.org/packages/61/42/5c456b02816845d163fab0f32936b6a5b649f3f915beff6f819f4f6c90b2/httpcore-0.16.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/42/5c456b02816845d163fab0f32936b6a5b649f3f915beff6f819f4f6c90b2/httpcore-0.16.3.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n httpcore-0.16.3
cd %{_builddir}/httpcore-0.16.3
pushd ..
cp -a httpcore-0.16.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672279880
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . h11
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . h11
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-httpcore
cp %{_builddir}/httpcore-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-httpcore/cc8ca9a1480585587761018c62aca50f1cbb0594 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} h11
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
