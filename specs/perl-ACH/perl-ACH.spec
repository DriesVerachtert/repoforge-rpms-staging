# $Id$
# Authority: dag
# Upstream: Christopher Kois <cpkois$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ACH

Summary: Perl module that implements a ACH perl object
Name: perl-ACH
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ACH/

Source: http://www.cpan.org/authors/id/C/CP/CPKOIS/ACH/ACH-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-ACH is a Perl module that implements a ACH perl object.

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
%doc %{_mandir}/man3/ACH.3pm*
%{perl_vendorlib}/ACH.pm

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
