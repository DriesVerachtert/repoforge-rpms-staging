# $Id$
# Authority: dag
# Upstream: Makamaka Hannyaharamitu <makamaka$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-BeyondPerl-ToSQL

Summary: Perl module to have RDBMS calculate instead of Perl
Name: perl-Acme-BeyondPerl-ToSQL
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-BeyondPerl-ToSQL/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-BeyondPerl-ToSQL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Acme-BeyondPerl-ToSQL is a Perl module to have RDBMS calculate
instead of Perl.

This package contains the following Perl modules:

    Acme::BeyondPerl::ToSQL
    Acme::BeyondPerl::ToSQL::Pg
    Acme::BeyondPerl::ToSQL::SQLite
    Acme::BeyondPerl::ToSQL::mysql

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Acme/
%dir %{perl_vendorlib}/Acme/BeyondPerl/
%{perl_vendorlib}/Acme/BeyondPerl/ToSQL/
%{perl_vendorlib}/Acme/BeyondPerl/ToSQL.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
