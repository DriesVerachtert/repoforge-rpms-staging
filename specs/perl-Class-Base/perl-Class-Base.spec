# $Id$
# Authority: dag
# Upstream: Andy Wardley <cpan$wardley,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Base

Summary: Perl module for deriving other modules
Name: perl-Class-Base
Version: 0.08
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Base/

Source: http://www.cpan.org/modules/by-module/Class/Class-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Class-Base is a Perl module for deriving other modules.

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
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man3/Class::Base.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Base.pm

%changelog
* Thu Aug 04 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.08-2
- Updated to release 0.08.

* Thu Aug 04 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.08-1
- Updated to release 0.08.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
