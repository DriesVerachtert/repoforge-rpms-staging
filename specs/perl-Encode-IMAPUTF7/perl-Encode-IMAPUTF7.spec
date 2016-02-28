# $Id$
# Authority: cmr
# Upstream: Peter Makholm <peter$makholm,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Encode-IMAPUTF7

Summary: modification of UTF-7 encoding for IMAP
Name: perl-Encode-IMAPUTF7
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Encode-IMAPUTF7/

Source: http://www.cpan.org/modules/by-module/Encode/Encode-IMAPUTF7-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
modification of UTF-7 encoding for IMAP.

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Encode::IMAPUTF7.3pm*
%dir %{perl_vendorlib}/Encode/
#%{perl_vendorlib}/Encode/IMAPUTF7/
%{perl_vendorlib}/Encode/IMAPUTF7.pm

%changelog
* Sun Feb 28 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.05-1
- Updated to release 1.05.

* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 1.04-1
- Initial package. (using DAR)
