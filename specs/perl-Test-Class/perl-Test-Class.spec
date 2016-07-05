# $Id$
# Authority: dries
# Upstream: Adrian Howard <adrianh$quietstars,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Class

Summary: Easily create test classes in an xUnit/JUnit style
Name: perl-Test-Class
Version: 0.50
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Class/

Source: http://www.cpan.org/modules/by-module/Test/Test-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 1:5.6.1

%description
Easily create test classes in an xUnit/JUnit style.

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
%doc %{_mandir}/man3/Test::Class.3pm*
%doc %{_mandir}/man3/Test::Class::*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Class/
%{perl_vendorlib}/Test/Class.pm

%changelog
* Tue Jul 05 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.50-1
- Updated to release 0.50.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.31-1
- Updated to version 0.31.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
