# $Id$
# Authority: dag
# Upstream: Paul Johnson <pjcj$cpan,org>

### EL6 ships with perl-Devel-Cover-0.65-1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Cover

Summary: Code coverage metrics for Perl
Name: perl-Devel-Cover
Version: 1.22
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Cover/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Cover-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Storable)


%description
Devel-Cover module for perl.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes Contributors docs LICENCE MANIFEST META.yml README
%doc %{_mandir}/man1/cover.1*
%doc %{_mandir}/man1/cpancover.1*
%doc %{_mandir}/man1/gcov2perl.1*
%doc %{_mandir}/man3/Devel::Cover.3pm*
%doc %{_mandir}/man3/Devel::Cover::*.3pm*
%{_bindir}/cover
%{_bindir}/cpancover
%{_bindir}/gcov2perl
%dir %{perl_vendorarch}/Devel/
%{perl_vendorarch}/Devel/Cover/
%{perl_vendorarch}/Devel/Cover.pm
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/Cover/

%changelog
* Sun Apr 17 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.22-1
- Updated to release 1.22.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.65-1
- Updated to version 0.65.

* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 0.64-1
- Updated to release 0.64.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.63-1
- Updated to release 0.63.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.61-1
- Initial package. (using DAR)
