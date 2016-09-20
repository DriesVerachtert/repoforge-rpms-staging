# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Querylet-Output-Text

Summary: Perl module to output querylet results to text tables
Name: perl-Querylet-Output-Text
Version: 0.112
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Querylet-Output-Text/

Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Querylet-Output-Text-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Querylet-Output-Text is a Perl module to output querylet results
to text tables.

This package contains the following Perl module:

    Querylet::Output::Text

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Querylet::Output::Text.3pm*
%dir %{perl_vendorlib}/Querylet/
%dir %{perl_vendorlib}/Querylet/Output/
%{perl_vendorlib}/Querylet/Output/Text.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.112-1
- Initial package. (using DAR)
