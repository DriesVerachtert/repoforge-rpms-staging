# $Id$
# Authority: dries
# Upstream: Luis Mu&#241;oz <luismunoz$cpan,org>

### EL6 ships with perl-Crypt-PasswdMD5-1.3-6.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-PasswdMD5

Summary: Provides interoperable MD5-based crypt() functions
Name: perl-Crypt-PasswdMD5
Version: 1.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-PasswdMD5/

Source: http://search.cpan.org/CPAN/authors/id/R/RS/RSAVAGE/Crypt-PasswdMD5-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This  code  provides  various  crypt()-compatible  interfaces  to  the
MD5-based crypt() function found in  various *nixes.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/PasswdMD5.pm

%changelog
* Wed Nov 22 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.40-1
- Updated to release 1.40.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
