# $Id$
# Authority: dries
# Upstream: Eric Estabrooks <eric$urbanrage,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-HCE_MD5

Summary: One way hash chaining encryption using MD5
Name: perl-Crypt-HCE_MD5
Version: 0.75
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-HCE_MD5/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-HCE_MD5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements a chaining block cipher using a one
way hash.  This method of encryption is the same that is
used by radius (RFC2138) and is also described in Applied
Cryptography.

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
%{perl_vendorlib}/Crypt/HCE_MD5.pm
%{perl_vendorlib}/auto/Crypt/HCE_MD5

%changelog
* Thu Nov 16 2017 Dries Verachtert <dries.verachtert@dries.eu> - 0.75-1
- Updated to release 0.75.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.70-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.70-1
- Initial package.
