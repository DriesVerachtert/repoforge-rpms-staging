# $Id$
# Authority: dag
# Upstream: Greg Sabino Mullane <greg$turnstep,com>

### EL6 ships with perl-DBD-Pg-2.15.1-3.el6
### EL5 ships with perl-DBD-Pg-1.49-2.el5_3.1
### EL4 ships with perl-DBD-Pg-1.31-6
### EL3 ships with perl-DBD-Pg-1.21-2
### EL2 ships with perl-DBD-Pg-1.01-1
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Pg

Summary: DBI PostgreSQL interface
Name: perl-DBD-Pg
Version: 3.5.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Pg/

Source: http://search.cpan.org/CPAN/authors/id/T/TU/TURNSTEP/DBD-Pg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(DBI) >= 1.52
#BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.6.1
BuildRequires: perl(version)
BuildRequires: postgresql-devel
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: postgresql
Requires: perl(DBI) >= 1.52
Requires: perl >= 5.6.1
Requires: perl(version)

%filter_from_requires /^perl*/d
%filter_setup

%description
DBI PostgreSQL interface.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.dev README.win32 SIGNATURE TODO
%doc %{_mandir}/man3/DBD::Pg.3pm*
%doc %{_mandir}/man3/Bundle::DBD::Pg.3pm*
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Pg/
%dir %{perl_vendorarch}/Bundle/
%dir %{perl_vendorarch}/Bundle/DBD/
%{perl_vendorarch}/Bundle/DBD/Pg.pm
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Pg.pm

%changelog
* Fri Sep 18 2015 Dries Verachtert <dries.verachtert@dries.eu> - 3.5.1-1
- Updated to release 3.5.1.

* Thu Jun 17 2010 Christoph Maser <cmaser@gmx.de> - 2.17.1-2
- Changed perl dependency from 5.006001 to 5.6.1.

* Tue May 18 2010 Christoph Maser <cmaser@gmx.de> - 2.17.1-1
- Updated to version 2.17.1.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 2.16.1-1
- Updated to version 2.16.1.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 2.16.0-1
- Updated to version 2.16.0.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 2.15.1-1
- Updated to version 2.15.1.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 2.14.1-1
- Updated to version 2.14.1.

* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 2.13.1-1
- Updated to version 2.13.1.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 2.11.5-1
- Updated to release 2.11.5.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 2.11.1-1
- Updated to release 2.11.1.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.10.7
- Updated to release 2.10.7.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 2.8.1-1
- Updated to release 2.8.1.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.7.1-1
- Updated to release 2.7.1.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.6.4-1
- Updated to release 2.6.4.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.6.1-1
- Updated to release 2.6.1.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Updated to release 2.1.3.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.49-1
- Initial package. (using DAR)
