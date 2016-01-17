# $Id$
# Authority: dag
# Upstream: Jerry D. Hedden <jdhedden$cpan,org>
# ExcludeDist: el4 [ because Requires: perl(Scalar::Util) >= 1.21 ]

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-InsideOut

Summary: Comprehensive inside-out object support module
Name: perl-Object-InsideOut
Version: 4.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-InsideOut/

Source: http://search.cpan.org/CPAN/authors/id/J/JD/JDHEDDEN/Object-InsideOut-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(B)
BuildRequires: perl(Config)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Exception::Class) >= 1.29
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util) >= 1.21
BuildRequires: perl(Test::More) >= 0.5
BuildRequires: perl(attributes)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
Requires: perl(B)
Requires: perl(Config)
Requires: perl(Data::Dumper)
Requires: perl(Exception::Class) >= 1.29
Requires: perl(Scalar::Util) >= 1.21
Requires: perl(Test::More) >= 0.5
Requires: perl(attributes)
Requires: perl(overload)
Requires: perl(strict)
Requires: perl(warnings)

%filter_from_requires /^perl*/d
%filter_setup

%description
perl-Object-InsideOut is a Perl module with comprehensive inside-out
object support module.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Bundle::Object::InsideOut.3pm*
%doc %{_mandir}/man3/Object::InsideOut.3pm*
%doc %{_mandir}/man3/Object::InsideOut::*.3pm*
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/Bundle/Object/
%{perl_vendorlib}/Bundle/Object/InsideOut.pm
%dir %{perl_vendorlib}/Object/
%{perl_vendorlib}/Object/InsideOut/
%{perl_vendorlib}/Object/InsideOut.pm
%{perl_vendorlib}/Object/InsideOut.pod

%changelog
* Sun Jan 17 2016 Dries Verachtert <dries.verachtert@dries.eu> - 4.02-1
- Updated to release 4.02.

* Mon Dec 28 2009 Christoph Maser <cmr@financial.com> - 3.58-1
- Updated to version 3.58.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 3.57-1
- Updated to version 3.57.

* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 3.56-1
- Updated to version 3.56.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 3.55-1
- Updated to version 3.55.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 3.52-1
- Updated to release 3.52.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 3.47-1
- Updated to release 3.47.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 3.46-1
- Updated to release 3.46.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 3.42-1
- Updated to release 3.42.

* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 3.39-1
- Updated to release 3.39.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 3.38-1
- Updated to release 3.38.

* Fri Feb 22 2008 Dag Wieers <dag@wieers.com> - 3.37-1
- Updated to release 3.37.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 3.36-1
- Updated to release 3.36.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 3.35-1
- Updated to release 3.35.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 3.34-1
- Updated to release 3.34.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 3.33-1
- Updated to release 3.33.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 3.27-1
- Updated to release 3.27.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 3.14-1
- Initial package. (using DAR)
