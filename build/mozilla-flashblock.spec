%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id \{3d7eb24f-2740-49df-8937-200b1cc08f8a\}
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}

Name:           mozilla-flashblock
Version:        1.5.18
Release:        1%{?dist}
Summary:        Flash blocking extension for Mozilla Firefox

Group:          Applications/Internet
License:        MPL 1.1 or GPL 2.0 or LGPL 2.1
URL:            http://flashblock.mozdev.org
Source0:        http://downloads.mozdev.org/flashblock/flashblock-%{version}.xpi

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
#Requires:       firefox
BuildRequires:  sed

%description
Extension for Firefox which blocks all flash content by default, and replaces
with a black box. To play, simply click the on the play button.

%prep
%setup -q -c

#dodgy hack to up compatibility with firefox 10
sed -i 's/<em:maxVersion>8./<em:maxVersion>10./' install.rdf

%build

rm -rf %{buildroot}
install -Dp -m 644 install.rdf %{buildroot}%{inst_dir}/install.rdf
install -Dp -m 644 chrome.manifest %{buildroot}%{inst_dir}/chrome.manifest
install -Dp -m 644 chrome/flashblock.jar %{buildroot}%{inst_dir}/chrome/flashblock.jar
install -Dp -m 644 defaults/preferences/flashblock.js %{buildroot}%{inst_dir}/defaults/preferences/flashblock.js


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{inst_dir}

%changelog
* Fri Dec 19 2014 Ian Firns <firnsy@kororaproject.org>- 1.5.18-1
- Update to 1.5.18 release.

* Sun Jun 30 2013 Chris Smart <csmart@kororaproject.org>- 1.5.17-1
- Update to 1.5.17 release.

* Mon Jul 02 2012 Chris Smart <chris@kororaa.org>- 1.5.16-1
- Update to 1.5.16 release.

* Sat Mar 18 2011 Chris Smart <chris@kororaa.org>- 1.5.14.2-1
- Initial port.
