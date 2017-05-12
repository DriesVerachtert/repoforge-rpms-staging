# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-Keepalive

Summary: Manages and keeps alive client connections
Name: perl-POE-Component-Client-Keepalive
Version: 0.272
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-Keepalive/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-Keepalive-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::IP) >= 1.25
BuildRequires: perl(POE) >= 1.28
BuildRequires: perl(POE::Component::Client::DNS) >= 1.051
Requires: perl(Net::IP) >= 1.25
Requires: perl(POE) >= 1.28
Requires: perl(POE::Component::Client::DNS) >= 1.051

%filter_from_requires /^perl*/d
%filter_setup

%description
POE::Component::Client::Keepalive creates and manages connections for
other components.  It maintains a cache of kept-alive connections for
quick reuse.  It is written specifically for clients that can benefit
from kept-alive connections, such as HTTP clients.  Using it for one-
shot connections would probably be silly.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/POE::Component::Client::Keepalive.3pm*
%doc %{_mandir}/man3/POE::Component::Connection::Keepalive.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
#%{perl_vendorlib}/POE/Component/Client/Keepalive/
%{perl_vendorlib}/POE/Component/Client/Keepalive.pm
%dir %{perl_vendorlib}/POE/Component/Connection/
%{perl_vendorlib}/POE/Component/Connection/Keepalive.pm

%changelog
* Fri May 12 2017 Dries Verachtert <dries.verachtert@dries.eu> - 0.272-1
- Updated to release 0.272.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.262-1
- Updated to version 0.262.

* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 0.260-1
- Updated to version 0.260.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.25-1
- Updated to version 0.25.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.1001-1
- Updated to release 0.1001.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.1000-1
- Updated to release 0.1000.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.0901-1
- Updated to release 0.0901.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.0801-1
- Updated to release 0.0801.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.0701-1
- Updated to release 0.0701.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
