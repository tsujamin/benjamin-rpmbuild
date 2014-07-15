Name:           atom
Version:        0.115.0
Release:        1%{?dist}
Summary:        Atom is a hackable text editor for the 21st century

License:        MIT
URL:            https://atom.io/
Source0:        https://github.com/atom/atom/archive/v%{version}.tar.gz
Patch0:         atom.check-buildroot.patch

BuildRequires:  make, gcc, gcc-c++, glibc-devel, nodejs, npm, libgnome-keyring-devel, git-core
#Requires:       

%description
Atom is a hackable text editor for the 21st century, built on atom-shell, and based on 
everything we love about our favorite editors. We designed it to be deeply customizable, but 
still approachable using the default configuration.


%prep
%setup -q
%patch0

%build
sudo npm config set python /usr/bin/python2 -g
npm install npm
export PATH=$(pwd)/node_modules/.bin:$PATH
sudo yum -y remove gyp
script/build
%define debug_package %{nil}
sudo yum -y install npm

%install
script/grunt install --install-dir %{buildroot}/usr

#%files
#%doc



#%changelog
#* Tue Jul 15 2014 
#- 
