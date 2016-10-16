# $Id$
# Authority: cmr
# Upstream: David Robins <dbrobins$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Parser

Summary: Perl module named HTTP-Parser
Name: perl-HTTP-Parser
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Parser/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml requires
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(ExtUtils::MakeMaker)


%description
perl-HTTP-Parser is a Perl module.

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
%doc %{_mandir}/man3/HTTP::Parser.3pm*
%dir %{perl_vendorlib}/HTTP/
#%{perl_vendorlib}/HTTP/Parser/
%{perl_vendorlib}/HTTP/Parser.pm

%changelog
* Sun Oct 16 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.06-1
- Updated to release 0.06.

* Mon Sep 07 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Initial package. (using DAR)
