# $Id$
# Authority: dries
# Upstream: Marcus Ramberg <mramberg@cpan.org>
# File::IO is too old on el4!
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Body

Summary: HTTP Body parser
Name: perl-HTTP-Body
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Body/

Source: http://search.cpan.org/CPAN/authors/id/G/GE/GETTY/HTTP-Body-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(File::Temp) >= 0.14
BuildRequires: perl(HTTP::Headers)
#BuildRequires: perl(IO::File) >= 1.14
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::Deep)
#BuildRequires: perl(Test::More) >= 0.86
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
Requires: perl(Carp)
Requires: perl(File::Temp) >= 0.14
Requires: perl(HTTP::Headers)
#Requires: perl(IO::File)
#Requires: perl(IO::File) >= 1.14
Requires: perl(IO::File)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module contains a HTTP body parser.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test TEST_POD=1

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
%doc %{_mandir}/man3/HTTP::Body.3pm*
%doc %{_mandir}/man3/HTTP::Body::*.3pm*
%dir %{perl_vendorlib}/HTTP/
%{perl_vendorlib}/HTTP/Body/
%{perl_vendorlib}/HTTP/Body.pm

%changelog
* Sat Sep 02 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.22-1
- Updated to release 1.22.

* Sat Feb 06 2010 Christoph Maser <cmr@financial.com> - 1.07-2
- Remove version for dependency IO::File

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 1.07-1
- Updated to version 1.07.

* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 1.06-1
- Updated to version 1.06.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
