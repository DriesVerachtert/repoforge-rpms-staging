# $Id$
# Authority: dag
# Upstream: David Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-InsideOut

Summary: Perl module that implements a safe, simple inside-out object construction kit
Name: perl-Class-InsideOut
Version: 1.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-InsideOut/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Class-InsideOut-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Config)
BuildRequires: perl(Exporter)
BuildRequires: perl(Scalar::Util) >= 1.09
BuildRequires: perl(Test::More) >= 0.45
BuildRequires: perl(base)
BuildRequires: perl >= 5.005
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Class::ISA)
Requires: perl(Config)
Requires: perl(Exporter)
Requires: perl(Scalar::Util) >= 1.09
Requires: perl(Test::More) >= 0.45
Requires: perl(base)
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup

%description
Class-InsideOut is a Perl module that implements a safe, simple inside-out
object construction kit.

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
%doc Changes LICENSE MANIFEST META.yml README Todo examples/
%doc %{_mandir}/man3/Class::InsideOut.3pm*
%doc %{_mandir}/man3/Class::InsideOut::*.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/InsideOut/
%{perl_vendorlib}/Class/InsideOut.pm
#%{perl_vendorlib}/Class/InsideOut.pod

%changelog
* Thu Jan 07 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.13-1
- Updated to release 1.13.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.10-1
- Updated to version 1.10.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
