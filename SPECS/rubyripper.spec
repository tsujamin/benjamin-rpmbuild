Name:           rubyripper
Version:        0.6.1
Release:        1%{?dist}
Summary:        Delivers high quality rips from audio Cd's using cdparanoia

License:        GPLv3+
URL:            https://github.com/tsujamin/rubyripper
Source0:        https://github.com/tsujamin/rubyripper/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  ruby-devel
BuildRequires:  rubygem-gettext
BuildRequires:  rubygem-gtk2
BuildRequires:  cdparanoia
Requires:       ruby
Requires:       rubygem-gtk2
Requires:       cdparanoia
Requires:       cd-discid

%description
Rubyripper aims to deliver high quality rips from audio Cd's to your computer
drive. It tries to do so by ripping the same track with cdparanoia multiple 
times and then comparing the results. It currently has a gtk2 and a command-
line interface.

%prep
%setup -q


%build
ruby ./configure --prefix=/usr --enable-gtk2 --enable-cli --enable-lang-all

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc README
%{_bindir}/*
%{_datadir}/*


%changelog
* Wed Apr  8 2015 Benjamin Roberts <Benjamin@BGRoberts.id.au>
- 0.6.1-1
- added freedb support for ruby-2.X
- fixed error when prime character present in song title
- corrected rubydir prefix handling in configure script
