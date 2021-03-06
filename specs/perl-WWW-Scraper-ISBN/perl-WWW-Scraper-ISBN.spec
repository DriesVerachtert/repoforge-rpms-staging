# $Id$
# Authority: cmr
# Upstream: Andrew Schamp <andy$schamp,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Scraper-ISBN

Summary: Perl module named WWW-Scraper-ISBN
Name: perl-WWW-Scraper-ISBN
Version: 0.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Scraper-ISBN/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Scraper-ISBN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml requires
BuildRequires: perl(Carp) >= 1
BuildRequires: perl(WWW::Scraper::ISBN::Record) >= 0.15


%description
perl-WWW-Scraper-ISBN is a Perl module.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/WWW::Scraper::ISBN.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Scraper/
#%{perl_vendorlib}/WWW/Scraper/ISBN/
%{perl_vendorlib}/WWW/Scraper/ISBN.pm

%changelog
* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.25-1
- Initial package. (using DAR)
