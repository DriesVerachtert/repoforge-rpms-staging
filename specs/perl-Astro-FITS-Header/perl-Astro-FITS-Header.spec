# $Id$
# Authority: cmr
# Upstream: Alasdair Allan <aa$astro,ex,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Astro-FITS-Header

Summary: Object Orientated interface to FITS HDUs
Name: perl-Astro-FITS-Header
Version: 3.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Astro-FITS-Header/

Source: http://www.cpan.org/modules/by-module/Astro/Astro-FITS-Header-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
AutoReq: no

%description
Object Orientated interface to FITS HDUs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Astro::FITS::Header*.3pm*
%dir %{perl_vendorlib}/Astro/
%dir %{perl_vendorlib}/Astro/FITS/
%{perl_vendorlib}/Astro/FITS/Header/
%{perl_vendorlib}/Astro/FITS/Header.pm

%changelog
* Mon Dec 07 2015 Dries Verachtert <dries.verachtert@dries.eu> - 3.07-1
- Updated to release 3.07.

* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 3.01-1
- Initial package. (using DAR)
