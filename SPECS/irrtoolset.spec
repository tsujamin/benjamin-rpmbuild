Name:           irrtoolset
Version:        a86c5f59bd15280dde0114bb6523ce96563da075
Release:        1%{?dist}
Summary:        The IRRToolSet is a set of tools to work with Internet routing policies. 

Group:          Networking
License:        MIT and GPLv2
URL:            https://github.com/irrtoolset/irrtoolset
Source0:        https://github.com/irrtoolset/irrtoolset/archive/%{?version}.zip

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: readline-devel
Requires:      readline

%description
The IRRToolSet is a set of tools to work with Internet routing policies. These policies are stored in Internet Routing Registries (IRR) in the Routing Policy Specification Language.

The goal of the IRRToolSet is to make routing information more convenient and useful for network engineers, by providing tools for automated router configuration, routing policy analysis, and on-going maintenance.

%prep
%setup -q


%build
autoreconf -vfi
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}
%{_docdir}
%{_mandir}


%changelog
* Mon Jul 20 2015 Benjamin Roberts - a86c5f59bd15280dde0114bb6523ce96563da075-1
- Initial build from git head

