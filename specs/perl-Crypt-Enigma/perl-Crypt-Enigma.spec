# $Id$

# Authority: dries
# Upstream: Alistair Francis <alizta$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Enigma

Summary: Implementation of the WWII Enigma Machine
Name: perl-Crypt-Enigma
Version: 1.1
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Enigma/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Enigma-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains a perl implementation of the WWII Enigma machine.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Crypt::Enigma.3pm*
%{perl_vendorlib}/Crypt/Enigma.pm
%{perl_vendorlib}/Crypt/bombe.pl
%{perl_vendorlib}/Crypt/encode.pl

%changelog
* Mon Sep 26 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.1-1
- Updated to release 1.1.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
