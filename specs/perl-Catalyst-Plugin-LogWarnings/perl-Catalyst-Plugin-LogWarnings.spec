# $Id$
# Authority: dries
# Upstream: Jonathan Rockway <jrockway$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-LogWarnings

Summary: Log perl warnings to the Catalyst log
Name: perl-Catalyst-Plugin-LogWarnings
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-LogWarnings/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-LogWarnings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This plugin redirects perl's warn() warnings to a Catalyst log
($c->log->warn), allowing you to filter warnings, log warnings to a
database, Log4Perl, etc.

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
%{perl_vendorlib}/Catalyst/Plugin/LogWarnings.pm
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/

%changelog
* Sat Nov 19 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.03-1
- Updated to release 0.03.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
