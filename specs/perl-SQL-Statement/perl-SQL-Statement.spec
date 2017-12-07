# $Id$
# Authority: dries
# Upstream: Jens Rehsack <rehsack@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Statement

Summary: SQL parsing and processing engine
Name: perl-SQL-Statement
Version: 1.412
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Statement/

Source: http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/SQL-Statement-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(Clone) >= 0.30
BuildRequires: perl(DBD::File) >= 0.37
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Params::Util) >= 1.00
BuildRequires: perl(Scalar::Util) >= 1.0
#BuildRequires: perl(Test::Simple) >= 0.86
BuildRequires: perl(Test::Simple) 
Requires: perl(Carp)
Requires: perl(Clone) >= 0.30
Requires: perl(DBD::File) >= 0.37
Requires: perl(Data::Dumper)
Requires: perl(Params::Util) >= 1.00
Requires: perl(Scalar::Util) >= 1.0
#BuildRequires: perl(Test::Simple) >= 0.86
Requires: perl(Test::Simple)

%filter_from_requires /^perl*/d
%filter_setup


%description
These modules can be used stand-alone to parse SQL statements
or used with DBI and DBD::CSV, DBD::AnyData or other drivers to
create, modify, and query data in many kinds of formats including
XML, CSV, Fixed Length, Excel Spreadsheets and many others.

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
%{perl_vendorlib}/SQL

%changelog
* Thu Dec 07 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.412-1
- Updated to release 1.412.

* Mon Feb 27 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.410-1
- Updated to release 1.410.

* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 1.33-1
- Updated to version 1.33.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to version 1.23.

* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 1.22-1
- Updated to version 1.22.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Initial package.
