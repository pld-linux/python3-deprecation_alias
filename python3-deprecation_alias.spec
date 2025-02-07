%define		module	deprecation_alias
Summary:	A wrapper around 'deprecation' providing support for deprecated aliases
Name:		python3-%{module}
Version:	0.3.3
Release:	1
License:	Apache
Group:		Libraries/Python
Source0:	https://pypi.debian.net/deprecation-alias/deprecation-alias-%{version}.tar.gz
# Source0-md5:	c5799e74197ed7b064dd8608c240a18c
URL:		https://pypi.org/project/deprecation-alias/
BuildRequires:	python3-modules >= 1:3.2
#BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wrapper around ‘deprecation' providing support for deprecated
aliases.

%prep
%setup -q -n deprecation-alias-%{version}

%build
%py3_build
# deprecated target, but sometimes still used: %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
