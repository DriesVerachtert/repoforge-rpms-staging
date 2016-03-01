# $Id$
# Authority: dries
# Upstream: JT Smith <jt$plainblack,com>
# Needs new List::Util
# ExcludeDist: el4
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-JSON

Summary: JSON based config file system
Name: perl-Config-JSON
Version: 1.5202
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-JSON/

Source: http://search.cpan.org/CPAN/authors/id/R/RI/RIZEN/Config-JSON-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(File::Temp) >= 0.18
BuildRequires: perl(File::Temp)
BuildRequires: perl(JSON) >= 2.16
BuildRequires: perl(List::Util) >= 1.19
BuildRequires: perl(Moose) >= 0.93
BuildRequires: perl(Test::Deep) >= 0.095
BuildRequires: perl(Test::More) >= 0.7
#Requires: perl(File::Temp) >= 0.18
Requires: perl(File::Temp)
Requires: perl(JSON) >= 2.16
Requires: perl(List::Util) >= 1.19
Requires: perl(Moose) >= 0.93
Requires: perl(Test::Deep) >= 0.095
Requires: perl(Test::More) >= 0.7

%filter_from_requires /^perl*/d
%filter_setup

%description
A JSON based config file system.

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
%doc %{_mandir}/man3/Config::JSON.3pm*
%dir %{perl_vendorlib}/Config/
#%{perl_vendorlib}/Config/JSON/
%{perl_vendorlib}/Config/JSON.pm

%changelog
* Tue Mar 01 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.5202-1
- Updated to release 1.5202.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.5000-1
- Updated to version 1.5000.

* Sat Aug 22 2009 Chsrioph Maser <cmr@financial.com> - 1.3.1-1
- Updated to release 1.3.1.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Initial package.
