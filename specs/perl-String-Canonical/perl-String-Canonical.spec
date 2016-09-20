# $Id$
# Authority: dag
# Upstream: Erick Calder <ecalder$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Canonical

Summary: Perl module to creates canonical strings
Name: perl-String-Canonical
Version: 1.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Canonical/

Source: http://www.cpan.org/modules/by-module/String/String-Canonical-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-String-Canonical is a Perl module to creates canonical strings.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/String::Canonical.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/String/
#%{perl_vendorlib}/String/Canonical/
%{perl_vendorlib}/String/Canonical.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
