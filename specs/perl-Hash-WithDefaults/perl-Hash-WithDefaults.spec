# $Id$
# Authority: dag
# Upstream: Jan Krynicky <Jenda$Krynicky,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Hash-WithDefaults

Summary: Perl module that implements a class for hashes with key-casing requirements supporting defaults
Name: perl-Hash-WithDefaults
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Hash-WithDefaults/

Source: http://www.cpan.org/modules/by-module/Hash/Hash-WithDefaults-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Hash-WithDefaults is a Perl module that implements a class for hashes
with key-casing requirements supporting defaults.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Hash::WithDefaults.3pm*
%dir %{perl_vendorlib}/Hash/
%{perl_vendorlib}/Hash/WithDefaults.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
