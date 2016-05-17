# $Id$
# Authority: dries
# Upstream: Austin Schutz <tex$habit,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Stty

Summary: Setting terminal parameters
Name: perl-IO-Stty
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Stty/

Source: http://www.cpan.org/modules/by-module/IO/IO-Stty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)

%description
The two perl items in this package are an stty shell script and a
module for setting terminal parameters.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e "s|/usr/local/perl/bin/perl|%{_bindir}/perl|g;" *.pl

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build
./Build test

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IO/Stty.pm
%{_bindir}/stty.pl

%changelog
* Tue May 17 2016 Dries Verachtert <dries.verachtert@dries.eu> 0.03-1
- Updated to release 0.03.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - .02-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - .02-1
- Initial package.
