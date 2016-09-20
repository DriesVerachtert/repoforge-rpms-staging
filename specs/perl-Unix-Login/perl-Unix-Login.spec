# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Login

Summary: Perl module for customizable Unix login prompt and validation 
Name: perl-Unix-Login
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Login/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-Login-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Unix-Login is a Perl module for customizable Unix login prompt
and validation.

This package contains the following Perl module:

    Unix::Login

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Unix::Login.3pm*
%dir %{perl_vendorlib}/Unix/
#%{perl_vendorlib}/Unix/Login/
%{perl_vendorlib}/Unix/Login.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Initial package. (using DAR)
