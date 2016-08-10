# $Id$
# Authority: dag
# Upstream: Shawn Sorichetti <ssoriche$coloredblocks,net>

### EL6 ships with perl-Test-Output-0.12-3.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Output

Summary: Utilities to test STDOUT and STDERR messages
Name: perl-Test-Output
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Output/

Source: http://www.cpan.org/modules/by-module/Test/Test-Output-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Utilities to test STDOUT and STDERR messages.

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
%doc %{_mandir}/man3/Test::Output.3pm*
#%doc %{_mandir}/man3/Test::Output::Tie.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Output/
%{perl_vendorlib}/Test/Output.pm

%changelog
* Wed Aug 10 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.03-1
- Updated to release 1.03.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
