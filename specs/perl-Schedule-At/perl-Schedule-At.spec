# $Id$
# Authority: dries
# Upstream: Jose A. Rodriguez <Jose,Rodriguez+cpan$ac,upc,es>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Schedule-At

Summary: OS independent interface to the Unix 'at' command
Name: perl-Schedule-At
Version: 1.15
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Schedule-At/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JOSERODR/Schedule-At-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module privides an OS independent interface to the Unix 'at' command
 and it will map the calls to real (and OS dependent) commands.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Schedule/At.pm

%changelog
* Sun Feb 19 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.15-2
- Updated to release 1.15.

* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 1.09-1
- Updated to version 1.09.

* Fri Jun 19 2009 Christoph Maser <cmr@financial.com> - 1.08-1
- Updated to version 1.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
