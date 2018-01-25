# $Id$
# Authority: dag
# Upstream: Lincoln Stein <lstein$cshl,edu>

### EL6 ships with perl-Devel-Cycle-1.10-3.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Cycle

Summary: Find memory cycles in objects
Name: perl-Devel-Cycle
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Cycle/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Cycle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
Requires: perl

%description
Devel-Cycle is a Perl module to find memory cycles in objects.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Devel::Cycle.3pm*
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/Cycle.pm

%changelog
* Thu Jan 25 2018 Dries Verachtert <dries.verachtert@dries.eu> - 1.12-1
- Updated to release 1.12.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 1.11-1
- Updated to version 1.11.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Initial package. (using DAR)
