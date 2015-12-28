# $Id$
# Authority: cmr
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name namespace-autoclean

Summary: Keep imports out of your namespace
Name: perl-namespace-autoclean
Version: 0.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/namespace-autoclean/

Source: http://www.cpan.org/modules/by-module/namespace/namespace-autoclean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
Requires: perl(B::Hooks::EndOfScope) >= 0.07
Requires: perl(Class::MOP) >= 0.80
Requires: perl(List::Util)
Requires: perl(namespace::clean) >= 0.11


%description
Keep imports out of your namespace.

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
%doc Changes CONTRIBUTING INSTALL LICENCE MANIFEST META.yml README
%doc %{_mandir}/man3/namespace::autoclean.3pm*
%dir %{perl_vendorlib}/namespace/
#%{perl_vendorlib}/namespace/autoclean/
%{perl_vendorlib}/namespace/autoclean.pm

%changelog
* Mon Dec 28 2015 Dries Verachtert <dries.verachtert@dries.eu> - 0.28-1
- Updated to release 0.28.

* Tue Sep 15 2009 Christoph Maser <cmr@financial.com> - 0.09-1
- Updated to version 0.09.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Initial package. (using DAR)
