# $Id$
# Authority: dries
# Upstream: Dave Cross <dave$mag-sol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-Compare

Summary: Perl extension for comparing arrays
Name: perl-Array-Compare
Version: 2.12
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-Compare/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/Array-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Moose)
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Module::Build)
Requires: perl(Carp)
Requires: perl(Moose)
Requires: perl >= 0:5.6.0

%filter_from_requires /^perl*/d
%filter_setup

%description
Array::Compare is a Perl module which allows you to compare two arrays.

It has a number of features which allow you to control the way that the
arrays are compared:

* white space in array elements can be significant or ignored.
* particular columns in the arrays can be ignored.

Additionally you can get a simple true/false return value or the number
of columns which differ or an array containing the indexes of the
differing columns.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Array::Compare.3pm*
%dir %{perl_vendorlib}/Array/
%{perl_vendorlib}/Array/Compare.pm

%changelog
* Wed Sep 21 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.12-2
- Updated to release 2.12.

* Wed Sep 21 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.12-1
- Updated to release 2.12.

* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 2.01-1
- Updated to version 2.01.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
