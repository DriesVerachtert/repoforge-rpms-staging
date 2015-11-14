# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-GlobalDestruction

Summary: Expose PL_dirty, the flag which marks global destruction
Name: perl-Devel-GlobalDestruction
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-GlobalDestruction/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-GlobalDestruction-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Expose PL_dirty, the flag which marks global destruction.

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
%doc %{_mandir}/man3/Devel::GlobalDestruction.3pm*
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/GlobalDestruction/
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/GlobalDestruction.pm

%changelog
* Sat Nov 14 2015 Dries Verachtert <dries.verachtert@dries.eu> - 0.13-1
- Updated to release 0.13.

* Sat Nov 29 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
