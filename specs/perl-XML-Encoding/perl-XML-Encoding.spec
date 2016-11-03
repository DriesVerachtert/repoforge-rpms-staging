# $Id$
# Authority: dag
# Upstream: Clark Cooper <coopercc$netheaven,com>
# Upstream: Steve Hay <shay$cpan,org>

### EL4 ships with perl-XML-Encoding-1.01-26
%{?el4:# Tag: rfx}
### EL3 ships with perl-XML-Encoding-1.01-23
%{?el3:# Tag: rfx}
### EL2 ships with perl-XML-Encoding-1.01-2
%{?el2:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Encoding

Summary: Perl module for parsing XML encoding maps
Name: perl-XML-Encoding
Version: 2.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Encoding/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHAY/XML-Encoding-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(XML::Parser) >= 2.18
Requires: perl(XML::Parser) >= 2.18

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-XML-Encoding is a Perl module for parsing XML encoding maps.

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
%doc %{_mandir}/man3/XML::Encoding.3pm*
%doc %{_mandir}/man1/compile_encoding.1.gz
%doc %{_mandir}/man1/make_encmap.1.gz
%{_bindir}/compile_encoding
%{_bindir}/make_encmap
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Encoding.pm

%changelog
* Thu Nov 03 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.09-1
- Updated to release 2.09.

* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 2.08-1
- Updated to version 2.08.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 2.07-1
- Updated to version 2.07.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.01.

* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
