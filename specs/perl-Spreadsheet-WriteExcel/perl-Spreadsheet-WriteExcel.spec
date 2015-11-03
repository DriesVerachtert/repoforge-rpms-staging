# $Id$
# Authority: dries
# Upstream: John McNamara <plan9$eircom,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spreadsheet-WriteExcel

Summary: Write to a cross platform Excel binary file
Name: perl-Spreadsheet-WriteExcel
Version: 2.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spreadsheet-WriteExcel/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMCNAMARA/Spreadsheet-WriteExcel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(OLE::Storage_Lite) >= 0.19
BuildRequires: perl(Parse::RecDescent)
Requires: perl(File::Temp)
Requires: perl(OLE::Storage_Lite) >= 0.19
Requires: perl(Parse::RecDescent)

%filter_from_requires /^perl*/d
%filter_setup

%description
The Spreadsheet::WriteExcel module can be used to create a cross-
platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers,
formulas, hyperlinks and images can be written to the cells.

TThe Excel file produced by this module is compatible with 97,
2000, 2002 and 2003.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man1/chartex.1*
%doc %{_mandir}/man3/Spreadsheet::WriteExcel.3pm*
%doc %{_mandir}/man3/Spreadsheet::WriteExcel::*.3pm*
%{_bindir}/chartex
%dir %{perl_vendorlib}/Spreadsheet/
%{perl_vendorlib}/Spreadsheet/WriteExcel/
%{perl_vendorlib}/Spreadsheet/WriteExcel.pm

%changelog
* Tue Nov 03 2015 Dries Verachtert <dries.verachtert@dries.eu> - 2.40-1
- Updated to release 2.40.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 2.37-1
- Updated to version 2.37.

* Mon Jan 11 2010 Christoph Maser <cmr@financial.com> - 2.35-1
- Updated to version 2.35.

* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 2.34-1
- Updated to version 2.34.

* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 2.33-1
- Updated to version 2.33.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 2.32-1
- Updated to version 2.32.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 2.31-1
- Updated to version 2.31.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 2.30-1
- Updated to version 2.30.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 2.25-1
- Updated to version 2.25.

* Tue Sep  9 2008 Dries Verachtert <dries@ulyssis.org> - 2.24-1
- Updated to release 2.24.

* Mon Aug 18 2008 Dries Verachtert <dries@ulyssis.org> - 2.23-1
- Updated to release 2.23.

* Mon Jul 28 2008 Dries Verachtert <dries@ulyssis.org> - 2.22-1
- Updated to release 2.22.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 2.21-1
- Updated to release 2.21.

* Mon Oct 22 2007 Dries Verachtert <dries@ulyssis.org> - 2.20-1
- Updated to release 2.20.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.18-1
- Updated to release 2.18.

* Tue May 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Updated to release 2.16.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
