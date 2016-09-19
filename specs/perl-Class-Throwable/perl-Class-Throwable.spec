# $Id$
# Authority: dag
# Upstream: Stevan Little <stevan,little$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Throwable

Summary: Minimal lightweight exception class
Name: perl-Class-Throwable
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Throwable/

Source: http://www.cpan.org/modules/by-module/Class/Class-Throwable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Minimal lightweight exception class.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Class::Throwable.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Throwable/
%{perl_vendorlib}/Class/Throwable.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
