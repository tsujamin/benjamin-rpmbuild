Name:           atom
Version:        0.115.0
Release:        0%{?dist}
Summary:        Atom is a hackable text editor for the 21st century

License:        MIT
URL:            https://atom.io/

##
# atom is built from snapshots and npm is installed using the default script
# atom must be patched such that the .desktop file points at the right image/executable 
Source0:        https://github.com/atom/atom/archive/v%{version}.tar.gz
Source1:        https://npmjs.org/install.sh
Patch0:         atom.check-buildroot.patch


##
# System provided node-gyp causes npm plugin compilation to fail 
# (https://github.com/TooTallNate/node-gyp/issues/363)
# Automatic requirement generation fails as spidermonkey and ruby are detected when 
# not required.
BuildConflicts: gyp 
BuildRequires:  make, gcc, gcc-c++, glibc-devel, nodejs, curl, git-core, libgnome-keyring-devel
Requires:       libgnome-keyring
AutoReqProv:    no

%description
Atom is a hackable text editor for the 21st century, built on atom-shell, and based on 
everything we love about our favorite editors. We designed it to be deeply customizable, but 
still approachable using the default configuration.

%prep
%setup -q
%patch0

%build
##
# atom build stage (script/build)
# Debug packages are disabled
# Downloads and installs a local version of npm as current rpms are out of date (1.4 required)
# This npm and any subsequently installed package binaries are added to the path
%define debug_package %{nil}
npm_config_prefix=`pwd`/npm sh %SOURCE1
export PATH=`pwd`/node_modules/.bin:`pwd`/npm/bin:$PATH
script/build


%install
##
# atom install stage
# remove previous build (if exists) and "install" atom to the buildroot prefix
# include relevent libraries, binaries and doc/license files
script/grunt install --install-dir %{buildroot}/usr
%files
%doc README.md LICENSE.md CONTRIBUTING.md
%{_bindir}/*
%{_datadir}/*
