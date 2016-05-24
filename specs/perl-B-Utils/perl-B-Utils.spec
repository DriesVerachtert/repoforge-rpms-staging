# $Id$
# Authority: shuff
# Upstream: Joshua ben Jore <jjore$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Utils

Summary: Helper functions for op tree manipulation
Name: perl-%{real_name}
Version: 0.27
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Utils/

Source: http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/B-Utils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.006
Requires: perl(Exporter)
Requires: perl(ExtUtils::CBuilder)
Requires: perl(Scalar::Util)
Requires: perl(Task::Weaken)
Requires: perl(Test::More)
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup

%description
Perl module B::Utils.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
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
%doc Changes MANIFEST META.yml README 
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/B/
%{perl_vendorarch}/B/Utils.pm
%{perl_vendorarch}/B/Utils/OP.pm
%{perl_vendorarch}/auto/B/Utils/Utils.bs
%{perl_vendorarch}/auto/B/Utils/Utils.so
%{perl_vendorarch}/B/Utils/Install/BUtils.h
%{perl_vendorarch}/B/Utils/Install/Files.pm
%{perl_vendorarch}/B/Utils/Install/typemap

%changelog
* Tue May 24 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.27-1
- Updated to release 0.27.

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Sat Oct 03 2009 Steve Huff <shuff@vecna.org> - 0.08-1
- Initial package.
