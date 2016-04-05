# $Id$
# Authority: dries
# Upstream: Mattia Barbon <mbarbon$users,sourceforge,net>

### EL6 ships with perl-Module-Info-0.31-7.el6
%{?el6:# Tag: rfx}
# ExclusiveDist: el2 el3 el4 el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Info

Summary: Information about Perl modules
Name: perl-Module-Info
Version: 0.37
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Info/

Source: http://www.cpan.org/modules/by-module/Module/Module-Info-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Information about Perl modules.

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
%doc Changes
%doc %{_mandir}/man?/*
%{_bindir}/module_info
%{_bindir}/pfunc
%{perl_vendorlib}/Module/Info.pm
%{perl_vendorlib}/B

%changelog
* Tue Apr 05 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.37-1
- Updated to release 0.37.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Updated to release 0.28.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Initial package.
