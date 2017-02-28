# $Id$
# Authority: dries
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-ChiSquare

Summary: Chi Squared test
Name: perl-Statistics-ChiSquare
Version: 1.0000
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-ChiSquare/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-ChiSquare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements to Chi Squared test, using pre-computed tables.

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
%doc ARTISTIC.txt CHANGELOG GPL2.txt MANIFEST.* META.* README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Statistics/ChiSquare.pm

%changelog
* Tue Feb 28 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.0000-2
- Updated to release 1.0000.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
