# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Multimethods

Summary: Support multimethods and subroutine overloading in Perl
Name: perl-Class-Multimethods
Version: 1.701
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Multimethods/

Source: http://www.cpan.org/modules/by-module/Class/Class-Multimethods-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Support multimethods and subroutine overloading in Perl.

%prep
%setup -n %{real_name}-1.700

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Class/Multimethods.p*

%changelog
* Mon Oct 30 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.701-1
- Updated to release 1.701.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.70-1
- Initial package.
