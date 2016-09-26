# $Id$
# Authority: dries
# Upstream: Rafael R. Sevilla <sevillar$team,ph,inter,net>
# Upstream: Brian D Foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Rijndael

Summary: Crypt::CBC compliant Rijndael encryption module
Name: perl-Crypt-Rijndael
Version: 1.13
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Rijndael/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/Crypt-Rijndael-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Manifest) >= 1.14
BuildRequires: perl(Test::More)
Requires: perl(Test::Manifest) >= 1.14
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
This is Crypt::Rijndael, an XS-based implementation of the newly-selected
Advanced Encryption Standard algorithm Rijndael, designed by Joan Daemen
and Vincent Rijmen.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
#find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes LICENSE MANIFEST META.yml NEWS README
%doc %{_mandir}/man3/Crypt::Rijndael.3*
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Rijndael/
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/Rijndael.pm

%changelog
* Mon Sep 26 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.13-1
- Updated to release 1.13.

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.09-1
- Updated to version 1.09.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.08-1
- Updated to version 1.08.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Sun May 04 2008 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Fri Jul 06 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
