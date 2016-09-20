# $Id$
# Authority: dag
# Upstream: David Westbrook <dwestbrook@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Quantum-ClebschGordan

Summary: Perl module to calculate/list Clebsch-Gordan Coefficients
Name: perl-Quantum-ClebschGordan
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quantum-ClebschGordan/

Source: http://www.cpan.org/modules/by-module/Quantum/Quantum-ClebschGordan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Quantum-ClebschGordan is a Perl module to calculate/list Clebsch-Gordan
Coefficients.

This package contains the following Perl module:

    Quantum::ClebschGordan

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Quantum::ClebschGordan.3pm*
%{_bindir}/cg-j1j2
%dir %{perl_vendorlib}/Quantum/
%{perl_vendorlib}/Quantum/ClebschGordan.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
