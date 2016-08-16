# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

# el5 has 2.12 in perl-5.8.8
%{?el5:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Encode

Summary: Perl module that implements character encodings
Name: perl-Encode
Version: 2.86
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Encode/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/Encode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.7.3
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 1:5.7.3

%description
perl-Encode is a Perl module that implements character encodings.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changes MANIFEST META.yml README
%doc %{_mandir}/man1/enc2xs.1*
%doc %{_mandir}/man1/piconv.1*
%doc %{_mandir}/man3/Encode.3pm*
%doc %{_mandir}/man3/Encode::*.3pm*
%doc %{_mandir}/man3/encoding.3pm*
%doc %{_mandir}/man1/encguess.1*
%{_bindir}/enc2xs
%{_bindir}/piconv
%{_bindir}/encguess
%{perl_vendorarch}/auto/Encode/
%{perl_vendorarch}/Encode/
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm

%changelog
* Tue Aug 16 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.86-1
- Updated to release 2.86.

* Mon Dec 13 2010 Steve Huff <shuff@vecna.org> - 2.39-2
- Tagged rfx for el5.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 2.39-1
- Updated to version 2.39.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 2.37-1
- Updated to version 2.37.

* Wed Jul 15 2009 Christoph Maser <cmr@financial.com> - 2.35-1
- Updated to version 2.35.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 2.34-1
- Updated to version 2.34.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 2.33-1
- Updated to version 2.33.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.26-1
- Updated to release 2.26.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.25-1
- Updated to release 2.25.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 2.24-1
- Updated to release 2.24.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.23-1
- Updated to release 2.23.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 2.20-1
- Initial package. (using DAR)
