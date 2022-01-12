#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-linkify_it_py
Version  : 1.0.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/37/46/8688fd6f339593836ad08b577b67896cb0567924867bd03fc883582fec16/linkify-it-py-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/37/46/8688fd6f339593836ad08b577b67896cb0567924867bd03fc883582fec16/linkify-it-py-1.0.3.tar.gz
Summary  : Links recognition library with FULL unicode support.
Group    : Development/Tools
License  : MIT
Requires: pypi-linkify_it_py-license = %{version}-%{release}
Requires: pypi-linkify_it_py-python = %{version}-%{release}
Requires: pypi-linkify_it_py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(uc_micro_py)

%description
# linkify-it-py
[![CI](https://github.com/tsutsu3/linkify-it-py/workflows/CI/badge.svg?branch=main)](https://github.com/tsutsu3/linkify-it-py/actions)
[![pypi](https://img.shields.io/pypi/v/linkify-it-py)](https://pypi.org/project/linkify-it-py/)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/linkify-it-py/badges/version.svg)](https://anaconda.org/conda-forge/linkify-it-py)
[![codecov](https://codecov.io/gh/tsutsu3/linkify-it-py/branch/main/graph/badge.svg)](https://codecov.io/gh/tsutsu3/linkify-it-py)
[![Maintainability](https://api.codeclimate.com/v1/badges/6341fd3ec5f05fde392f/maintainability)](https://codeclimate.com/github/tsutsu3/linkify-it-py/maintainability)

%package license
Summary: license components for the pypi-linkify_it_py package.
Group: Default

%description license
license components for the pypi-linkify_it_py package.


%package python
Summary: python components for the pypi-linkify_it_py package.
Group: Default
Requires: pypi-linkify_it_py-python3 = %{version}-%{release}

%description python
python components for the pypi-linkify_it_py package.


%package python3
Summary: python3 components for the pypi-linkify_it_py package.
Group: Default
Requires: python3-core
Provides: pypi(linkify_it_py)
Requires: pypi(uc_micro_py)

%description python3
python3 components for the pypi-linkify_it_py package.


%prep
%setup -q -n linkify-it-py-1.0.3
cd %{_builddir}/linkify-it-py-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642005965
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-linkify_it_py
cp %{_builddir}/linkify-it-py-1.0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-linkify_it_py/d5877e21ab96983663f54d8faa3eca337aaa24b9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-linkify_it_py/d5877e21ab96983663f54d8faa3eca337aaa24b9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
