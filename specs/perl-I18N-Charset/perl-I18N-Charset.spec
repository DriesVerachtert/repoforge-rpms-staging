# $Id$
# Authority: dag
# Upstream: Martin Thurn <mthurn$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name I18N-Charset

Summary: IANA Character Set Registry names and Unicode::MapUTF8
Name: perl-I18N-Charset
Version: 1.415
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/I18N-Charset/

Source: http://www.cpan.org/modules/by-module/I18N/I18N-Charset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(IO::Capture::Stderr)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Env)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.004

%description
IANA Character Set Registry names and Unicode::MapUTF8 (et al.)
conversion scheme names .

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
%doc %{_mandir}/man3/I18N::Charset.3pm*
#%doc %{_mandir}/man3/I18N::Charset::*.3pm*
%dir %{perl_vendorlib}/I18N/
#%{perl_vendorlib}/I18N/Charset/
%{perl_vendorlib}/I18N/Charset.pm

%changelog
* Sat Nov 05 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.415-1
- Updated to release 1.415.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 1.394-1
- Updated to release 1.394.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.389-1
- Updated to release 1.389.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 1.388-1
- Updated to release 1.388.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 1.387-1
- Updated to release 1.387.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.385-1
- Updated to release 1.385.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.382-1
- Updated to release 1.382.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 1.379-1
- Updated to release 1.379.

* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 1.375-1
- Initial package. (using DAR)
