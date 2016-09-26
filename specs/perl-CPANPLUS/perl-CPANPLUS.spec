# $Id$
# Authority: dries
# Upstream: Chris Williams <chris@bingosnet.co.uk>

### This package is dangerous, we don't want it to be available as-is
# Tag: rft

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CPANPLUS

Summary: Command-line access to the CPAN interface
Name: perl-CPANPLUS
Version: 0.9160
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CPANPLUS/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/CPANPLUS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Data::Dumper)
Requires: perl >= 2:5.8.1

%description
The "CPANPLUS" library is an API to the "CPAN" mirrors and a collection
of interactive shells, commandline programs, daemons, etc, that use
this API.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} -pi -e 's|^ *\@ARGV = grep \{.*||g;' Makefile.PL
%{__perl} -pi -e 's|use Your::Module::Here|your use statements here|g;' lib/CPANPLUS/Internals/Constants/Report.pm
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" AUTOINSTALL=1 SETUP=0 JFDI=1
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
%{__rm} -rf  %{buildroot}%{_mandir}/man3/CPANPLUS*Win32* \
  %{buildroot}%{_mandir}/man?/CPANPLUS::inc* \
  %{buildroot}%{perl_vendorlib}/CPANPLUS/inc/*/*/*Win32*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man1/cpan2dist.1*
%doc %{_mandir}/man1/cpanp.1*
%doc %{_mandir}/man3/CPANPLUS.3pm*
%doc %{_mandir}/man3/CPANPLUS::*.3pm*
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%{perl_vendorlib}/CPANPLUS/
%{perl_vendorlib}/CPANPLUS.pm

%changelog
* Mon Sep 26 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.9160-1
- Updated to release 0.9160.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.9001-1
- Updated to version 0.9001.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.88-1
- Updated to version 0.88.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.074-1
- Updated to release 0.074.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.061-1
- Updated to release 0.061.

* Thu Nov 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.055-3
- Rebuild.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.055-1
- Updated to release 0.055.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.053-2
- Don't install all the included modules.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.053-1
- Updated to release 0.053.

* Mon Jan 17 2005 Dries Verachtert <dries@ulyssis.org> - 0.051-1
- Initial package.
