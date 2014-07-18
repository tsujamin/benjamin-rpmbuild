# benjamins rpm specs

currently includes specs for:
 + [atom.io](https://github.com/atom/atom)

# how to use 
 + move relevant files to ~/rpmbuild (rpmdev-setuptree if it doesnt exist or use this repo).
 + use `spectool -g NAME.spec` to get a packages sources (preferably from the SOURCES directory).
 + call `rpmbuild -ba SPECS/NAME.spec` to create the binary and source RPM's for a package.
