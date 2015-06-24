Summary: Puppet Labs INIFile Module
Name: pupmod-puppetlabs-inifile
Version: 1.2.0
Release: 1
License: Apache License
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppet >= 3.3.2
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Obsoletes: pupmod-puppetlabs-inifile-test

Prefix: /etc/puppet/environments/simp/modules

%description
This is the puppetlabs INIFile module as hosted at
https://github.com/puppetlabs/puppetlabs-inifile

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/inifile

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/inifile
done

cp metadata.json %{buildroot}/%{prefix}/inifile
cp CHANGELOG.md %{buildroot}/%{prefix}/inifile
cp Gemfile %{buildroot}/%{prefix}/inifile
cp LICENSE %{buildroot}/%{prefix}/inifile
cp README.markdown %{buildroot}/%{prefix}/inifile

mkdir -p %{buildroot}/usr/share/simp/tests/modules/inifile

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/inifile

%files
%defattr(0640,root,puppet,0750)
%{prefix}/inifile

%post
#!/bin/sh

if [ -d %{prefix}/inifile/plugins ]; then
  /bin/mv %{prefix}/inifile/plugins %{prefix}/inifile/plugins.bak
fi

%postun
# Post uninstall stuff

%changelog
* Wed Jun 24 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 1.2.0-1
- Removed the obsolete Modulefile

* Mon Feb 02 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 1.2.0-0
- Incorporated puppetlabs-inifile 1.2.0 for puppetlabs-puppetdb

* Fri Jan 16 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 1.0.3-1
- Changed puppet-server requirement to puppet

* Wed May 14 2014 Nick Markowski <nmarkowski@keywcorp.com> - 1.0.3-0
- Added supported platforms to metadata.json and spec fixes.
- Bugfix for handling whitespace better.

* Mon Jan 27 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 1.0.0-0
- Incorporated and packaged from the remote repository.
