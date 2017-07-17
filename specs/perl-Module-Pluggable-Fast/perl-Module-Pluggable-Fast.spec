# $Id$
# Authority: dries
# Upstream: Sebastian Riedel <sri$oook,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Pluggable-Fast

Summary: Fast plugins with instantiation
Name: perl-Module-Pluggable-Fast
Version: 0.19
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Pluggable-Fast/

Source: http://www.cpan.org/modules/by-module/Module/Module-Pluggable-Fast-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Similar to "Module::Pluggable" but instantiates plugins as soon as
they're found, useful for code generators like "Class::DBI::Loader".

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Module/Pluggable/Fast.pm

%changelog
* Mon Jul 17 2017 Dries Verachtert <dries.verachtert@dries.eu> - 0.19-1
- Updated to release 0.19.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
