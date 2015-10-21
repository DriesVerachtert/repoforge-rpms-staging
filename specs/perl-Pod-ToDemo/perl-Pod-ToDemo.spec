# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-ToDemo

Summary: Writes a demo program from a tutorial POD
Name: perl-Pod-ToDemo
Version: 1.20110709
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-ToDemo/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-ToDemo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Writes a demo program from a tutorial POD.

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
%doc %{_mandir}/man3/Pod::ToDemo.3pm*
%dir %{perl_vendorlib}/Pod/
#%{perl_vendorlib}/Pod/ToDemo/
%{perl_vendorlib}/Pod/ToDemo.pm

%changelog
* Wed Oct 21 2015 Dries Verachtert <dries.verachtert@dries.eu> - 1.20110709-1
- Updated to release 1.20110709.

* Tue Apr 28 2009 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
