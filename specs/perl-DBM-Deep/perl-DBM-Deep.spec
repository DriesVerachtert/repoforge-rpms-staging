# $Id$
# Authority: dag
# Upstream: Rob Kinyon <rob,kinyon$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBM-Deep

Summary: Pure perl multi-level hash/array DBM that supports transactions
Name: perl-DBM-Deep
Version: 2.0013
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBM-Deep/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKINYON/DBM-Deep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Digest::MD5) >= 1.00
BuildRequires: perl(Fcntl) >= 0.01
BuildRequires: perl(File::Path) >= 0.01
BuildRequires: perl(File::Temp) >= 0.01
BuildRequires: perl(IO::Scalar) >= 0.01
BuildRequires: perl(Pod::Usage) >= 1.3
BuildRequires: perl(Scalar::Util) >= 1.14
BuildRequires: perl(Test::Deep) >= 0.095
BuildRequires: perl(Test::Exception) >= 0.21
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn) >= 0.08
BuildRequires: perl >= 5.006_000
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Digest::MD5) >= 1.00
Requires: perl(Fcntl) >= 0.01
Requires: perl(Scalar::Util) >= 1.14
Requires: perl >= 5.006_000

%filter_from_requires /^perl*/d
%filter_setup

%description
DBM-Deep is a Perl module that implements a pure perl multi-level
hash/array DBM that supports transactions.

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
%doc %{_mandir}/man3/DBM::Deep.3pm*
%doc %{_mandir}/man3/DBM::Deep::*.3pm*
%dir %{perl_vendorlib}/DBM/
%{perl_vendorlib}/DBM/Deep/
%{perl_vendorlib}/DBM/Deep.pm
%{perl_vendorlib}/DBM/Deep.pod

%changelog
* Mon Jun 13 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.0013-1
- Updated to release 2.0013.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 1.0015-1
- Updated to version 1.0015.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.0014-1
- Updated to version 1.0014.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.0013-1
- Updated to release 1.0013.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.0009-1
- Updated to release 1.0009.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.0008-1
- Updated to release 1.0008.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.0007-1
- Updated to release 1.0007.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.0006-1
- Updated to release 1.0006.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.0001-1
- Initial package. (using DAR)
