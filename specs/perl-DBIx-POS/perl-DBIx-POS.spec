# $Id$
# Authority: dag
# Upstream: Michael Alan Dorman <mdorman$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-POS

Summary: Perl module to define a dictionary of SQL statements in a POD dialect (POS)
Name: perl-DBIx-POS
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-POS/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-POS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-DBIx-POS is a Perl module to define a dictionary of SQL statements
in a POD dialect (POS).

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
%doc %{_mandir}/man3/DBIx::POS.3pm*
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/POS.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
