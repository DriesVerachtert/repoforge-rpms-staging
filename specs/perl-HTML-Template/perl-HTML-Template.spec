# $Id$
# Authority: dries
# Upstream: Sam Tregar <sam$tregar,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Template

Summary: HTML Templates for CGI scripts
Name: perl-HTML-Template
Version: 2.97
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Template/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Template-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can use HTML templates in CGI scripts.

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
%doc LICENSE MANIFEST META.* Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/HTML/
%dir %{perl_vendorlib}/HTML/Template/
%{perl_vendorlib}/HTML/Template.pm
%{perl_vendorlib}/HTML/Template/FAQ.pm

%changelog
* Wed Aug 30 2017 Dries Verachtert <dries.verachtert@dries.eu> - 2.97-1
- Updated to release 2.97.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.9-1
- Updated to release 2.9.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Updated to release 2.8.

* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Initial package.
