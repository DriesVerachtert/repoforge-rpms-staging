# $Id: $
# Authority: ae
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Std

Summary: Generic config module
Name: perl-Config-Std
Version: 0.901
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Std/
Source: http://www.cpan.org/modules/by-module/Config/Config-Std-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements yet another damn configuration-file system.

The configuration language is deliberately simple and limited, and the
module works hard to preserve as much information (section order,
comments, etc.) as possible when a configuration file is updated.

See Chapter 19 of "Perl Best Practices" (O'Reilly, 2005) for the
rationale for this approach.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Config::Std*
%{perl_vendorlib}/Config/Std.pm

%changelog
* Tue Aug 09 2016 Dries Verachtert <dries.verachtert@dries.eu> 0.901-1
- Updated to release 0.901.

* Wed Dec 14 2011 Roderick A Anderson <raanders@cyber-office.net> - 0.900-1
- Brought up to version 0.900

* Fri Jun 29 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 0.0.4-1
- Initial package.
