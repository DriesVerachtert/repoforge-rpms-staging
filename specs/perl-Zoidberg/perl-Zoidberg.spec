# $Id$
# Authority: dag
# Upstream: Jaap Karssenberg <pardus$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Zoidberg

Summary: Perl module implementing a modular perl shell
Name: perl-Zoidberg
Version: 0.98
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Zoidberg/

Source: http://search.cpan.org/CPAN/authors/id/J/JB/JBERGER/Zoidberg-%{version}.tar.gz
#Source: http://www.cpan.org/authors/id/P/PA/PARDUS/zoidberg/Zoidberg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Module::Build) >= 0.24
BuildRequires: perl(Pod::Text)
BuildRequires: perl(Test::More)

%description
perl-Zoidberg is a Perl module implementing a modular perl shell.

This package contains the following Perl modules:

    Bundle::Zoidberg
    Zoidberg
    Zoidberg::Contractor
    Zoidberg::DispatchTable
    Zoidberg::Fish
    Zoidberg::Fish::Commands
    Zoidberg::Fish::Intel
    Zoidberg::Fish::Log
    Zoidberg::Fish::ReadLine
    Zoidberg::PluginHash
    Zoidberg::Shell
    Zoidberg::StringParser
    Zoidberg::Utils
    Zoidberg::Utils::Error
    Zoidberg::Utils::FileSystem
    Zoidberg::Utils::GetOpt
    Zoidberg::Utils::Output

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

### Clean up docs
#find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic Changes MANIFEST META.yml README
%doc %{_mandir}/man1/zoid.1*
%doc %{_mandir}/man1/zoidbuiltins.1*
%doc %{_mandir}/man1/zoiddevel.1*
%doc %{_mandir}/man1/zoidfaq.1*
%doc %{_mandir}/man1/zoiduser.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/zoid
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/auto/share/
%{perl_vendorlib}/Bundle/Zoidberg.pm
%{perl_vendorlib}/Zoidberg/
%{perl_vendorlib}/Zoidberg.pm
%{perl_vendorlib}/auto/share/dist/Zoidberg/
   
%changelog
* Fri Sep 11 2015 Dries Verachtert <dries.verachtert@dries.eu> - 0.98-1
- Updated to release 0.98.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.96-1
- Updated to release 0.96.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.95-1
- Initial package. (using DAR)
