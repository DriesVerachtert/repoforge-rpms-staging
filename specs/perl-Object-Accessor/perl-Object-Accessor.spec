# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

### EL6 ships with perl-Object-Accessor-0.34-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Accessor

Summary: Interface to create per object accessors
Name: perl-Object-Accessor
Version: 0.48
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Accessor/

Source: http://www.cpan.org/modules/by-module/Object/Object-Accessor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Params::Check) >= 0.23
BuildRequires: perl(Test::More)
Requires: perl(Carp)
Requires: perl(Params::Check) >= 0.23
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
Object::Accessor provides an interface to create per object
accessors (as opposed to per Class accessors, as, for example,
Class::Accessor> provides.

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
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Object/
%{perl_vendorlib}/Object/Accessor.pm

%changelog
* Sun Apr 30 2017 Dries Verachtert <dries.verachtert@dries.eu> - 0.48-1
- Updated to release 0.48.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.36-1
- Updated to version 0.36.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.34-1
- Updated to version 0.34.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Sat Sep 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
