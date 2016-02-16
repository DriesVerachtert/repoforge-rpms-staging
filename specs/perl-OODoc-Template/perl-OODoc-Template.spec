# $Id$
# Authority: dag
# Upstream: Mark Overmeer

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name OODoc-Template

Summary: Simple template system
Name: perl-OODoc-Template
Version: 0.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OODoc-Template/

Source: http://www.cpan.org/modules/by-module/OODoc/OODoc-Template-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Simple template system.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/OODoc::Template.3pm*
%dir %{perl_vendorlib}/OODoc/
#%{perl_vendorlib}/OODoc/Template/
%{perl_vendorlib}/OODoc/Template.pm
%{perl_vendorlib}/OODoc/Template.pod

%changelog
* Tue Feb 16 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.16-1
- Updated to release 0.16.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.14-1
- Updated to version 0.14.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
