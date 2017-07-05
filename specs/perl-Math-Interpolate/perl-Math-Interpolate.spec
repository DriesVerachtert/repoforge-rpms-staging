# $Id$
# Authority: dries
# Upstream: Blair Zajac <blair$orcaware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Interpolate

Summary: Interpolate values
Name: perl-Math-Interpolate
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Interpolate/

Source: http://www.cpan.org/modules/by-module/Math/Math-Interpolate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains several useful routines for interpolating data
sets and finding where a given value lies in a sorted list.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Interpolate.pm
%{perl_vendorlib}/Math/IntervalSearch.pm

%changelog
* Wed Jul 05 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.06-1
- Updated to release 1.06.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
