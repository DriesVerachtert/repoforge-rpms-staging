# $Id$
# Authority: dries
# Upstream: mdehoon <mdehoon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Cluster

Summary: Perl interface to the C Clustering Library
Name: perl-Algorithm-Cluster
Version: 1.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Cluster/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Cluster-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl interface to the C Clustering Library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL MANIFEST META.yml README doc/
%doc %{_mandir}/man3/Algorithm::Cluster.3pm*
%dir %{perl_vendorarch}/auto/Algorithm/
%{perl_vendorarch}/auto/Algorithm/Cluster/
%dir %{perl_vendorarch}/Algorithm/
%{perl_vendorarch}/Algorithm/Cluster/
%{perl_vendorarch}/Algorithm/Cluster.pm

%changelog
* Wed Dec 09 2015 Dries Verachtert <dries.verachtert@dries.eu> - 1.52-1
- Updated to release 1.52.

* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 1.47-1
- Updated to version 1.47.

* Mon Oct 06 2008 Dag Wieers <dag@wieers.com> - 1.43-1
- Updated to release 1.43.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 1.39-1
- Updated to release 1.39.

* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.37-1
- Updated to release 1.37.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.33-1
- Initial package.
