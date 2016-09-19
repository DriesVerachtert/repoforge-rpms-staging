# $Id$
# Authority: dag
# Upstream: D. Hageman <dhageman$dracken,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exporter-Cluster

Summary: Perl module for easy multiple module imports
Name: perl-Exporter-Cluster
Version: 0.31
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Exporter-Cluster/

Source: http://www.cpan.org/modules/by-module/Exporter/Exporter-Cluster-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Exporter-Cluster is a Perl module for easy multiple module imports.

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
%doc %{_mandir}/man3/Exporter::Cluster.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Exporter/
#%{perl_vendorlib}/Exporter/Cluster/
%{perl_vendorlib}/Exporter/Cluster.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Initial package. (using DAR)
