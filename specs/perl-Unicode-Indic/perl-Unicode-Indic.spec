# $Id$
# Authority: dag
# Upstream: Syamala Tadigadapa <syamalarao$hotmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Indic

Summary: Perl module to transliterate Indic language
Name: perl-Unicode-Indic
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Indic/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Indic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Unicode-Indic is a Perl module to transliterate Indic language.

This package contains the following Perl module:

    Unicode::Indic::Bengali

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
%doc Changes MANIFEST readme.first
%doc %{_mandir}/man3/Unicode::Indic::*.3pm*
%dir %{perl_vendorlib}/Unicode/
%{perl_vendorlib}/Unicode/Indic/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
