# $Id$
# Authority: dag
# Upstream: Chia-liang Kao <clkao@clkao.org>
# EclusiveDist: el5

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name App-CLI

Summary: Dispatcher module for command line interface programs
Name: perl-App-CLI
Version: 0.313
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/App-CLI/

Source: http://www.cpan.org/modules/by-module/App/App-CLI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Getopt::Long) >= 2.35
BuildRequires: perl(Pod::Simple::Text)
BuildRequires: perl(Test::More)

%description
Dispatcher module for command line interface programs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST
%doc %{_mandir}/man3/App::CLI.3pm*
%doc %{_mandir}/man3/App::CLI::Command.3pm*
%doc %{_mandir}/man3/App::CLI::Command::Help.3pm*
%doc %{_mandir}/man3/App::CLI::Helper.3pm*
%dir %{perl_vendorlib}/App/
%{perl_vendorlib}/App/CLI/
%{perl_vendorlib}/App/CLI.pm

%changelog
* Wed May 25 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.313-1
- Updated to release 0.313.

* Wed Feb 03 2010 Christoph Maser <cmr@financial.com> - 0.08-2
- add skipdeps to Makefile.PL call

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
