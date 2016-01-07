%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id \{3d7eb24f-2740-49df-8937-200b1cc08f8a\}
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}

Name:           mozilla-flashblock
Version:        1.5.20
Release:        1%{?dist}
Summary:        Flash blocking extension for Mozilla Firefox

Group:          Applications/Internet
License:        MPL 1.1 or GPL 2.0 or LGPL 2.1
URL:            http://flashblock.mozdev.org
Source0:        https://addons.cdn.mozilla.net/user-media/addons/433/flashblock-%{version}-fx.xpi
#Source1:	whitelist.js

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
Extension for Firefox which blocks all flash content by default, and replaces
with a black box. To play, simply click the on the play button.

%prep
%setup -q -c

%build

rm -rf %{buildroot}
#install -Dp -m 644 install.rdf %{buildroot}%{inst_dir}/install.rdf
#install -Dp -m 644 chrome.manifest %{buildroot}%{inst_dir}/chrome.manifest
#install -Dp -m 644 chrome/flashblock.jar %{buildroot}%{inst_dir}/chrome/flashblock.jar
#install -Dp -m 644 defaults/preferences/flashblock.js %{buildroot}%{inst_dir}/defaults/preferences/flashblock.js
#install -Dp -m 644 %{SOURCE1} %{buildroot}%{inst_dir}/defaults/preferences/whitelist.js
install -Dp -m 644 %{SOURCE0} %{buildroot}%{inst_dir}.xpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{inst_dir}.xpi

%changelog
* Thu Jan 7 2016 Chris Smart <csmart@kororaproject.org>- 1.5.20-1
- Update to version 1.5.20.
- Use signed xpi from mozilla so it works with Firefox 43

* Wed Feb 04 2015 Matthew Weaver <matthew@kororaproject.org>- 1.5.18-2
- Add whitelist for youtube to workaround flashblock bug with html5

* Fri Dec 19 2014 Ian Firns <firnsy@kororaproject.org>- 1.5.18-1
- Update to 1.5.18 release.

* Sun Jun 30 2013 Chris Smart <csmart@kororaproject.org>- 1.5.17-1
- Update to 1.5.17 release.

* Mon Jul 02 2012 Chris Smart <chris@kororaa.org>- 1.5.16-1
- Update to 1.5.16 release.

* Sat Mar 18 2011 Chris Smart <chris@kororaa.org>- 1.5.14.2-1
- Initial port.
