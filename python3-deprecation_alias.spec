%define		module	deprecation_alias
Summary:	A wrapper around 'deprecation' providing support for deprecated aliases
Summary(pl.UTF-8):	Obudowanie "deprecation" zapewniające obsługę przestarzałych aliasów
Name:		python3-%{module}
Version:	0.4.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/deprecation-alias/
Source0:	https://files.pythonhosted.org/packages/source/d/deprecation-alias/deprecation_alias-%{version}.tar.gz
# Source0-md5:	f0727998c5e7ebe870373d3f0ff11a82
URL:		https://pypi.org/project/deprecation-alias/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wrapper around `deprecation' providing support for deprecated
aliases.

%description -l pl.UTF-8
Obudowanie "deprecation" zapewniające obsługę przestarzałych aliasów.

%prep
%setup -q -n deprecation_alias-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
