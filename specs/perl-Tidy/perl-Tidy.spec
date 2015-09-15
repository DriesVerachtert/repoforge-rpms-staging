# $Id$
# Authority: dries
# Upstream: Steve Hancock <shancock7078$bigfoot,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl-Tidy

Summary: Perl module that parses and beautifies perl source
Name: perl-Tidy
Version: 20150815
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl-Tidy/

Source: http://www.cpan.org/modules/by-module/Perl/Perl-Tidy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Perltidy is a tool to indent and reformat perl scripts. It can also
write scripts in html format.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COPYING MANIFEST META.yml README TODO
%doc %{_mandir}/man1/perltidy.1*
%doc %{_mandir}/man3/Perl::Tidy.3pm*
%{_bindir}/perltidy
%dir %{perl_vendorlib}/Perl/
%{perl_vendorlib}/Perl/Tidy.pm
%{perl_vendorlib}/Perl/Tidy.pod

%changelog
* Tue Sep 15 2015 Dries Verachtert <dries.verachtert@dries.eu> - 20150815-1
- Updated to release 20150815.

* Sun Dec 23 2007 Dries Verachtert <dries@ulyssis.org> - 20071205-1
- Updated to release 20071205.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 20070424-1
- Initial package. (using DAR)
