# $Id$
# Upstream: Allen Day <allenday@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Math-Combinatorics

Summary: unknown
Name: perl-Math-Combinatorics
Version: 0.09
Release: 1%{?dist}
License: unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Combinatorics/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALLENDAY/Math-Combinatorics-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Math::Combinatorics.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Math/Combinatorics.pm
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.09-1
- initial package
