# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-HTTP

Summary: Non-blocking/concurrent HTTP queries with POE
Name: perl-POE-Component-Client-HTTP
Version: 0.949
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-HTTP/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCAPUTO/POE-Component-Client-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request) >= 1.3
BuildRequires: perl(HTTP::Response) >= 1.37
BuildRequires: perl(Net::HTTP::Methods) >= 0.02
BuildRequires: perl(POE) >= 1.28
BuildRequires: perl(POE::Component::Client::Keepalive) >= 0.261
BuildRequires: perl(Test::POE::Server::TCP)
BuildRequires: perl(URI) >= 1.24
Requires: perl(HTTP::Request) >= 1.3
Requires: perl(HTTP::Response) >= 1.37
Requires: perl(Net::HTTP::Methods) >= 0.02
Requires: perl(POE) >= 1.28
Requires: perl(POE::Component::Client::Keepalive) >= 0.261
Requires: perl(Test::POE::Server::TCP)
Requires: perl(URI) >= 1.24

%filter_from_requires /^perl*/d
%filter_setup

%description
A HTTP user-agent component.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CHANGES.OLD MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Component::Client::HTTP.3pm*
%doc %{_mandir}/man3/POE::Component::Client::HTTP::*.3pm*
%doc %{_mandir}/man3/POE::Filter::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
%{perl_vendorlib}/POE/Component/Client/HTTP/
%{perl_vendorlib}/POE/Component/Client/HTTP.pm
%{perl_vendorlib}/POE/Filter/

%changelog
* Wed Nov 25 2015 Dries Verachtert <dries.verachtert@dries.eu> - 0.949-1
- Updated to release 0.949.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.894-1
- Updated to version 0.894.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.893-1
- Updated to version 0.893.

* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 0.890-1
- Updated to version 0.890.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.88-1
- Updated to version 0.88.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.83-1
- Updated to release 0.83.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Sat Jan 06 2007 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Initial package.
