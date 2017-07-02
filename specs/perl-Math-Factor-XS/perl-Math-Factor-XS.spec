# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Factor-XS

Summary: Factorise numbers and calculate matching multiplications
Name: perl-Math-Factor-XS
Version: 0.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Factor-XS/

Source: http://www.cpan.org/modules/by-module/Math/Math-Factor-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(boolean)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Carp)
Requires: perl(Exporter)
Requires: perl(List::MoreUtils)
Requires: perl(Params::Validate)
Requires: perl(Scalar::Util)
Requires: perl(XSLoader)
Requires: perl(boolean)

%filter_from_requires /^perl*/d
%filter_setup

%description
Math::Factor::XS factorises numbers by applying modulo operator divisons.

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Math::Factor::XS.3pm*
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/Factor/
%{perl_vendorarch}/auto/Math/Factor/XS/
%dir %{perl_vendorarch}/Math/
%dir %{perl_vendorarch}/Math/Factor/
%{perl_vendorarch}/Math/Factor/XS.pm

%changelog
* Sun Jul 02 2017 Dries Verachtert <dries.verachtert@dries.eu> - 0.40-1
- Updated to release 0.40.

* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 0.37-1
- Updated to version 0.37.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Initial package.
