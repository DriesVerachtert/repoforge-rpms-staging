# $Id$
# Authority: dag
# Upstream: Lincoln A Baxter <lab$lincolnbaxter,com,MAKE,ME,VALID>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-SigAction

Summary: Perl module for consistent signal handling
Name: perl-Sys-SigAction
Version: 0.21
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-SigAction/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-SigAction-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Sys-SigAction is a Perl module for consistent signal handling.

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
%doc %{_mandir}/man3/Sys::SigAction.3pm*
%dir %{perl_vendorlib}/Sys/
%dir %{perl_vendorlib}/Sys/SigAction/
%{perl_vendorlib}/Sys/SigAction.pm
%{perl_vendorlib}/Sys/SigAction/Alarm.pm

%changelog
* Thu Mar 17 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.21-2
- Updated to release 0.21.

* Thu Mar 17 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.21-1
- Updated to release 0.21.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
