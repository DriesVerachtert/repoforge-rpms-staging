# $Id$
# Authority: dries
# Upstream: Ruslan U. Zakirov <Ruslan.Zakirov@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Quoted

Summary: Extract the structure of a quoted mail message
Name: perl-Text-Quoted
Version: 2.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Quoted/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/Text-Quoted-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Autoformat)
BuildRequires: perl >= 5.6.0
Requires: perl(Text::Autoformat)
Requires: perl >= 5.6.0

%filter_from_requires /^perl*/d
%filter_setup


%description
Extract the structure of a quoted mail message.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::Quoted.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Quoted/
%{perl_vendorlib}/Text/Quoted.pm

%changelog
* Wed Apr 12 2017 Dries Verachtert <dries.verachtert@dries.eu> - 2.09-1
- Updated to release 2.09.

* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 2.06-1
- Updated to version 2.06.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Sat Aug 25 2007 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.8-1
- Initial package.
