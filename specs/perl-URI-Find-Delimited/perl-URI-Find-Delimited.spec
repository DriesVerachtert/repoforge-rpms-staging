# $Id$
# Authority: dag
# Upstream: Kake L Pugh <kake$earth,li>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Find-Delimited

Summary: Perl module to find URIs which may be wrapped in enclosing delimiters
Name: perl-URI-Find-Delimited
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Find-Delimited/

Source: http://www.cpan.org/modules/by-module/URI/URI-Find-Delimited-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-URI-Find-Delimited is a Perl module to find URIs which may be wrapped
in enclosing delimiters.

This package contains the following Perl module:

    URI::Find::Delimited

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
%doc %{_mandir}/man3/URI::Find::Delimited.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/Find/
#%{perl_vendorlib}/URI/Find/Delimited/
%{perl_vendorlib}/URI/Find/Delimited.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
