# $Id$
# Authority: dag
# Upstream: Maxim Kashliak <maxico$softhome,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ZM-SSI

Summary: Perl module that implements an SSI parser for CGI
Name: perl-ZM-SSI
Version: 0.0.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ZM-SSI/

Source: http://www.cpan.org/authors/id/M/MA/MAXICO/ZM-SSI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-ZM-SSI is a Perl module that implements an SSI parser for CGI.

This package contains the following Perl module:

    ZM::SSI

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
%doc MANIFEST README
%doc %{_mandir}/man3/ZM::SSI.3pm*
%dir %{perl_vendorlib}/ZM/
%{perl_vendorlib}/ZM/SSI.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.0.5-1
- Initial package. (using DAR)
