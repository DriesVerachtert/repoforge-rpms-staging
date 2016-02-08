# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Return-Value
%define real_version 1.666005

Summary: Polymorphic return values
Name: perl-Return-Value
Version: 1.666.005
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Return-Value/

Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Return-Value-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package provides polymorphic return values.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Return::Value.3pm*
%dir %{perl_vendorlib}/Return/
#%{perl_vendorlib}/Return/Value/
%{perl_vendorlib}/Return/Value.pm

%changelog
* Mon Feb 08 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.666.005-1
- Updated to release 1.666.005.

* Wed Jul 22 2009 Christoph Maser <cmr@finanial.com> - 1.666.001-1
- Updated to version 1.666.001.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.302-1
- Initial package.
