# $Id$
# Authority: dries

Summary: SRCP server for model railways
Name: srcpd
Version: 2.1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://srcpd.sourceforge.net/

Source: http://dl.sf.net/project/srcpd/srcpd/%{version}/srcpd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel

%description
SRCP is an comminication protocol designed to integrate all model railroad 
systems. Further key features are full multiuser capabilities and simplified 
user interface development.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man8/srcpd.8*
%doc %{_mandir}/man5/srcpd.conf.5*
%doc %{_mandir}/*/man8/srcpd.8*
%doc %{_mandir}/*/man5/srcpd.conf.5*
%{_sbindir}/srcpd
%{_sysconfdir}/udev/rules.d/10-liusb.rules
%config(noreplace) %{_sysconfdir}/srcpd.conf

%changelog
* Thu Jan 16 2014 Dries Verachtert <dries.verachtert@dries.eu> - 2.1.2
- Update to release 2.1.2.

* Sun Dec 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.10-1
- Initial package.
