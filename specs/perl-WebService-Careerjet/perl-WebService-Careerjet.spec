# $Id$
# Authority: dries
# Upstream: Jerome Eteve <jeromeAteteveDotnet>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Careerjet

Summary: Perl interface to Careerjet's public search API
Name: perl-WebService-Careerjet
Version: 3.1
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Careerjet/

Source: http://www.cpan.org/modules/by-module/WebService/WebService-Careerjet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp) >= 1.03
BuildRequires: perl(Class::AutoAccess) >= 0.02
BuildRequires: perl(Encode) >= 2.08
BuildRequires: perl(Getopt::Std) >= 1.05
BuildRequires: perl(HTTP::Request) >= 1.4
BuildRequires: perl(JSON) >= 2.07
BuildRequires: perl(LWP::UserAgent) >= 2.033
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Wrap) >= 2001.09292
BuildRequires: perl(URI::Escape) >= 3.28
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Carp) >= 1.03
Requires: perl(Class::AutoAccess) >= 0.02
Requires: perl(Encode) >= 2.08
Requires: perl(Getopt::Std) >= 1.05
Requires: perl(HTTP::Request) >= 1.4
Requires: perl(JSON) >= 2.07
Requires: perl(LWP::UserAgent) >= 2.033
Requires: perl(Test::More)
Requires: perl(Text::Wrap) >= 2001.09292
Requires: perl(URI::Escape) >= 3.28

%filter_from_requires /^perl*/d
%filter_setup


%description
Perl interface to Careerjet's public search API.

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
%doc %{_mandir}/man3/WebService::Careerjet.3pm*
%{_bindir}/jobsearch
%dir %{perl_vendorlib}/WebService/
#%{perl_vendorlib}/WebService/Careerjet/
%{perl_vendorlib}/WebService/Careerjet.pm

%changelog
* Mon Feb 13 2017 Dries Verachtert <dries.verachtert@dries.eu> - 3.1-2
- Updated to release 3.1.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
