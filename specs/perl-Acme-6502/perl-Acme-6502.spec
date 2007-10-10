# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-6502

Summary: Pure Perl 65C02 simulator
Name: perl-Acme-6502
Version: 0.0.6
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-6502/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-6502-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Pure Perl 65C02 simulator.

%prep
%setup -n %{real_name}-v%{version}

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Acme::6502.3pm*
%doc %{_mandir}/man3/Acme::6502::Tube.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/6502/
%{perl_vendorlib}/Acme/6502.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.000006-1
- Initial package. (using DAR)
