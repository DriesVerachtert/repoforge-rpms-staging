# $Id$
# Authority: dries
# Upstream: Shlomi Fish <shlomif$iglu,org,il>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-LineTrace

Summary: Apply traces to individual lines
Name: perl-Devel-LineTrace
Version: 0.1.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-LineTrace/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-LineTrace-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Apply traces to individual lines.

%prep
%setup -n %{real_name}-v%{version}

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
%doc %{_mandir}/man3/Devel::LineTrace*
%{perl_vendorlib}/Devel/LineTrace.pm

%changelog
* Wed Jan 13 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.1.9-1
- Updated to release 0.1.9.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.1.6-1
- Initial package.
