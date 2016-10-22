# $Id$
# Authority: dag
# Upstream: SADAHIRO Tomoyuki <SADAHIRO$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Normalize

Summary: Perl module that implements Unicode Normalization Forms
Name: perl-Unicode-Normalize
Version: 1.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Normalize/

Source: http://search.cpan.org/CPAN/authors/id/K/KH/KHW/Unicode-Normalize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test)
BuildRequires: perl(bytes)
BuildRequires: perl(constant)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Carp)
Requires: perl(DynaLoader)
Requires: perl(Exporter)
Requires: perl(File::Copy)
Requires: perl(File::Spec)
Requires: perl(Test)
Requires: perl(bytes)
Requires: perl(constant)
Requires: perl(strict)
Requires: perl(warnings)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Unicode-Normalize is a Perl module that implements Unicode
Normalization Forms.

This package contains the following Perl module:

    Unicode::Normalize

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.N META.yml README
%doc %{_mandir}/man3/Unicode::Normalize.3pm*
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/Normalize.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/Normalize/

%changelog
* Sat Oct 22 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.25-1
- Updated to release 1.25.

* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.10-1
- Updated to version 1.10.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
