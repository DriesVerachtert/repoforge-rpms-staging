# $Id$
# Authority: dries
# Upstream: Bob Faist <bob,faist$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-MusicBrainz

Summary: Web service API to MusicBrainz database
Name: perl-WebService-MusicBrainz
Version: 1.0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-MusicBrainz/

Source: http://search.cpan.org/CPAN/authors/id/B/BF/BFAIST/WebService-MusicBrainz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.7
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 1:5.7

%description
This module will search the MusicBrainz database through their web service 
and return objects with the found data.

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
%doc Changes MANIFEST META.* README.md
%doc %{_mandir}/man3/WebService::MusicBrainz.3pm*
%doc %{_mandir}/man3/WebService::MusicBrainz::*.3pm*
%dir %{perl_vendorlib}/WebService/
%{perl_vendorlib}/WebService/MusicBrainz/
%{perl_vendorlib}/WebService/MusicBrainz.pm

%changelog
* Tue Feb 14 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.0.3-1
- Updated to release 1.0.3.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.22-1
- Updated to version 0.22.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
