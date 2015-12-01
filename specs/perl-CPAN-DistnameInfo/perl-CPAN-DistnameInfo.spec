# $Id$
# Authority: dries
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CPAN-DistnameInfo

Summary: Extract distribution name and version from a distribution filename
Name: perl-CPAN-DistnameInfo
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CPAN-DistnameInfo/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/CPAN-DistnameInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
Many online services that are centered around CPAN attempt to associate
multiple uploads by extracting a distribution name from the filename of
the upload. For most distributions this is easy as they have used
ExtUtils::MakeMaker or Module::Build to create the distribution, which
results in a uniform name. But sadly not all uploads are created in this
way.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/CPAN::DistnameInfo.3pm*
%dir %{perl_vendorlib}/CPAN/
#%{perl_vendorlib}/CPAN/DistnameInfo/
%{perl_vendorlib}/CPAN/DistnameInfo.pm

%changelog
* Tue Dec 01 2015 Dries Verachtert <dries.verachtert@dries.eu> - 0.12-1
- Updated to release 0.12.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.09-1
- Updated to version 0.09.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
