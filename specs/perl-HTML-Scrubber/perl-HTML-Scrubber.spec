# $Id$
# Authority: dries
# Upstream: D. H. <crazyinsomniac$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Scrubber

Summary: Scrub or sanitize html
Name: perl-HTML-Scrubber
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Scrubber/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Scrubber-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Module::Build)

%description
Perl extension for scrubbing/sanitizing html.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/Scrubber.pm

%changelog
* Fri Oct 21 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.15-1
- Updated to release 0.15.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
