# $Id$
# Authority: dries
# Upstream: Abigail <$cpan$$abigail,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Common

Summary: Provide commonly requested regular expressions
Name: perl-Regexp-Common
Version: 2017040401
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Common/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABIGAIL/Regexp-Common-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl >= 5.4.730
BuildRequires: perl(strict)
BuildRequires: perl(vars)
Requires: perl >= 5.4.730
Requires: perl(strict)
Requires: perl(vars)

%filter_from_requires /^perl*/d
%filter_setup


%description
Provide commonly requested regular expressions.

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
%doc COPYRIGHT COPYRIGHT.AL COPYRIGHT.AL2 COPYRIGHT.BSD COPYRIGHT.MIT MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Regexp::Common.3pm*
%doc %{_mandir}/man3/Regexp::Common::*.3pm*
%dir %{perl_vendorlib}/Regexp/
%{perl_vendorlib}/Regexp/Common/
%{perl_vendorlib}/Regexp/Common.pm

%changelog
* Tue May 30 2017 Dries Verachtert <dries.verachtert@dries.eu> - 2017040401-1
- Updated to release 2017040401.

* Mon Oct 31 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2016060801-1
- Updated to release 2016060801.

* Fri Jun 18 2010 Christoph Maser <cmr@financial.com> - 2010010201-2
- Changed perl dependency from 5.00473 to 5.4.730.

* Mon Jan  4 2010 Christoph Maser <cmr@financial.com> - 2010010201-1
- Updated to version 2010010201.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 2009123002-1
- Updated to version 2009123002.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 2009123001-1
- Updated to version 2009123001.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 2.122-1
- Updated to release 2.122.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.120-1
- Initial package.
