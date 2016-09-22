# $Id$
# Authority: dag
# Upstream: Alex Vandiver <alexmv+pause$mit,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-Hours

Summary: Perl module to calculate business hours in a time period
Name: perl-Business-Hours
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-Hours/

Source: http://www.cpan.org/modules/by-module/Business/Business-Hours-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Set::IntSpan) >= 1.12
Requires: perl(Set::IntSpan) >= 1.12

%filter_from_requires /^perl*/d
%filter_setup


%description
Business-Hours is a perl module to calculate business hours in a time period.

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
%doc Changes LICENSE MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Business::Hours.3pm*
%dir %{perl_vendorlib}/Business/
%{perl_vendorlib}/Business/Hours.pm

%changelog
* Thu Sep 22 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.12-1
- Updated to release 0.12.

* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 0.09-1
- Updated to version 0.09.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
