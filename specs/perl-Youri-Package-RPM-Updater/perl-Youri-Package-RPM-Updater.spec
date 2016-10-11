# $Id$
# Authority: dag
# Upstream: Youri project <youri$zarb,org>

# rpm on el4 is to old
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Youri-Package-RPM-Updater

Summary: Perl module to update RPM packages automatically
Name: perl-Youri-Package-RPM-Updater
Version: 0.6.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Youri-Package-RPM-Updater/

Source: http://www.cpan.org/authors/id/G/GR/GROUSSE/Youri-Package-RPM-Updater-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Youri-Package-RPM-Updater is a Perl module to update RPM packages
automatically.

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
%doc %{_mandir}/man3/Youri::Package::RPM::Updater.3pm*
%dir %{perl_vendorlib}/Youri/
%dir %{perl_vendorlib}/Youri/Package/
%dir %{perl_vendorlib}/Youri/Package/RPM/
#%{perl_vendorlib}/Youri/Package/RPM/Updater/
%{perl_vendorlib}/Youri/Package/RPM/Updater.pm

%changelog
* Tue Oct 11 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.6.0-1
- Updated to release 0.6.0.

* Mon Jul 20 2009 Christoph Maser <cmr@financial.com> - 0.4.7-1
- Updated to version 0.4.7.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Initial package. (using DAR)
