# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-cant
%define real_version 0.000001

Summary: Perl module to see if an object or package can't do something
Name: perl-UNIVERSAL-cant
Version: 0.0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-cant/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-cant-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-UNIVERSAL-cant is a Perl module to see if an object or package
can't do something.

This package contains the following Perl module:

    UNIVERSAL::cant

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/UNIVERSAL::cant.3pm*
%dir %{perl_vendorlib}/UNIVERSAL/
#%{perl_vendorlib}/UNIVERSAL/cant/
%{perl_vendorlib}/UNIVERSAL/cant.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.0.1-1
- Initial package. (using DAR)
