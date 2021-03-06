# $Id$
# Authority: dries
# Upstream: John D. Porter <johndporter$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-RandPasswd

Summary: Random password generator based on FIPS-181
Name: perl-Crypt-RandPasswd
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-RandPasswd/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-RandPasswd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is an implementation of the Automated Password Generator standard,
defined in FIPS Publication 181, "Standard for Automated Password Generator":
http://www.itl.nist.gov/fipspubs/fip181.htm

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/RandPasswd.pm

%changelog
* Thu Nov 23 2017 Dries Verachtert <dries.verachtert@dries.eu> - 0.06-1
- Updated to release 0.06.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
