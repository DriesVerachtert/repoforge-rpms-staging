# $Id$
# Authority: dag
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Caller

Summary: meatier versions of C<caller>
Name: perl-Devel-Caller
Version: 2.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Caller/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Caller-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)

%description
meatier versions of C<caller>.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Devel::Caller.3pm*
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/Caller/
%dir %{perl_vendorarch}/Devel/
%{perl_vendorarch}/Devel/Caller.pm

%changelog
* Fri Nov 25 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.06-1
- Updated to release 2.06.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Wed Jan 02 2008 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.11-2
- Added a missing BuildRequires: perl(Module::Build) to build in Mock 
- Added a missing BuildRequires: perl(ExtUtils::CBuilder)

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
