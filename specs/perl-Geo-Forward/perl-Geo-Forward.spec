# $Id$
# Authority: dag
# Upstream: Michael R. Davis <account=>perl,tld=>com,domain=>michaelrdavis>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Forward

Summary: Perl module to calculate geographic location from lat, lon, distance, and heading
Name: perl-Geo-Forward
Version: 0.14
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Forward/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Forward-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Geo-Forward is a Perl module to calculate geographic location
from lat, lon, distance, and heading.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Geo::Forward.3pm*
%dir %{perl_vendorlib}/Geo/
%{perl_vendorlib}/Geo/Forward.pm

%changelog
* Mon Apr 11 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.14-1
- Updated to release 0.14.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
