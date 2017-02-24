# $Id$
# Authority: dries
# Upstream: Adriano Ferreira <ferreira$shoo,cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sort-Half-Maker

Summary: Create half-sort subs easily
Name: perl-Sort-Half-Maker
Version: 0.04
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sort-Half-Maker/

Source: http://www.cpan.org/modules/by-module/Sort/Sort-Half-Maker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Create half-sort subs easily.

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
%doc %{_mandir}/man3/Sort::Half::Maker*
%{perl_vendorlib}/Sort/Half/Maker.pm
%dir %{perl_vendorlib}/Sort/Half/

%changelog
* Fri Feb 24 2017 Dries Verachtert <dries.verachtert@dries.eu> - 0.04-2
- Updated to release 0.04.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
