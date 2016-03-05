# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

### EL6 ships with perl-Params-Check-0.26-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Params-Check

Summary: Generic input parsing/checking mechanism
Name: perl-Params-Check
Version: 0.38
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Params-Check/

Source: http://www.cpan.org/modules/by-module/Params/Params-Check-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Allows for generic input checking and validating using a powerfull
templating system, providing default values and so on.

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
%dir %{perl_vendorlib}/Params/
%{perl_vendorlib}/Params/Check.pm

%changelog
* Sat Mar 05 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.38-1
- Updated to release 0.38.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.

