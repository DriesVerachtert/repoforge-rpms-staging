# $Id$
# Authority: dag
# Upstream: Tim Keefer <tkeefer$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ACH-Builder

Summary: Tools for building ACH (Automated Clearing House) files
Name: perl-ACH-Builder
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ACH-Builder/

Source: http://www.cpan.org/authors/id/T/TK/TKEEFER/ACH-Builder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-ACH-Builder contains tools for building ACH (Automated Clearing House) files.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/ACH::Builder.3pm*
%dir %{perl_vendorlib}/ACH/
%{perl_vendorlib}/ACH/Builder.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
