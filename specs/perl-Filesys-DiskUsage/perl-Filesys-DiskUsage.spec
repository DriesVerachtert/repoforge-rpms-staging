# $Id$
# Authority: dag
# Upstream: José Alves de Castro <cog$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filesys-DiskUsage

Summary: Estimate file space usage (similar to `du`)
Name: perl-Filesys-DiskUsage
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filesys-DiskUsage/

Source: http://www.cpan.org/modules/by-module/Filesys/Filesys-DiskUsage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Estimate file space usage (similar to `du`).

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Filesys::DiskUsage.3pm*
%doc %{_mandir}/man1/fdu.1*
%dir %{perl_vendorlib}/Filesys/
#%{perl_vendorlib}/Filesys/DiskUsage/
%{perl_vendorlib}/Filesys/DiskUsage.pm
%{_bindir}/fdu

%changelog
* Mon Jan 25 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.08-1
- Updated to release 0.08.

* Thu Jan 24 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
