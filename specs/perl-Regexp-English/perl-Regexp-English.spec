# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-English

Summary: Create regular expressions more verbosely
Name: perl-Regexp-English
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-English/

Source: http://www.cpan.org/modules/by-module/Regexp/Regexp-English-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl module to create regular expressions more verbosely.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Regexp/English.pm

%changelog
* Mon Nov 07 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.01-1
- Updated to release 1.01.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Updated to release 1.00.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
