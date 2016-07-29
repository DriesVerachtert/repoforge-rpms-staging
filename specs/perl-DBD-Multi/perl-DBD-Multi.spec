# $Id$
# Authority: dag
# Upstream: Dan Wright <dwright@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Multi

Summary: Failover and Load Balancing of DBI Handles
Name: perl-DBD-Multi
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Multi/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Multi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(DBD::SQLite) >= 1.09
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod) >= 1.14
BuildRequires: perl(Test::Pod::Coverage) >= 1.04
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
Failover and Load Balancing of DBI Handles.

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/DBD::Multi.3pm*
%dir %{perl_vendorlib}/DBD/
#%{perl_vendorlib}/DBD/Multi/
%{perl_vendorlib}/DBD/Multi.pm

%changelog
* Fri Jul 29 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.18-1
- Updated to release 0.18.

* Sun Feb 24 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
