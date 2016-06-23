# $Id$
# Authority: dries
# Upstream: Richard Foley <richard,foley$rfi,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Data

Summary: Interface to file data
Name: perl-File-Data
Version: 1.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Data/

Source: http://search.cpan.org/CPAN/authors/id/R/RF/RFOLEY/File-Data-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Interface to file data.

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
%{perl_vendorlib}/File/File/Data.pm

%changelog
* Thu Jun 23 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.20-1
- Updated to release 1.20.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
