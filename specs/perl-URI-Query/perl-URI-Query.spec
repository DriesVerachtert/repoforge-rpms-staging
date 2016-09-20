# $Id$
# Authority: dag
# Upstream: Gavin Carr <gavin$openfusion,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-Query

Summary: Perl module that provides URI query string manipulation
Name: perl-URI-Query
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-Query/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAVINC/URI-Query-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-URI-Query is a Perl module that provides URI query string manipulation.

This package contains the following Perl module:

    URI::Query

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
%doc MANIFEST README
%doc %{_mandir}/man3/URI::Query.3pm*
%dir %{perl_vendorlib}/URI/
#%{perl_vendorlib}/URI/Query/
%{perl_vendorlib}/URI/Query.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.08-1
- Updated to version 0.08.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
