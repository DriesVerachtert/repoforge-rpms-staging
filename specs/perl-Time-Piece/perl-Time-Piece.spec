# $Id$
# Authority: dries
# Upstream: MSERGEANT <msergeant@cpan.org>

### EL6 ships with perl-Time-Piece-1.15-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Piece

Summary: Object Oriented time objects
Name: perl-Time-Piece
Version: 1.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Piece/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Time-Piece-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains Object Oriented time objects.

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
%doc Changes MANIFEST MANIFEST META.* README
%doc %{_mandir}/man3/Time::Piece.3pm*
%doc %{_mandir}/man3/Time::Seconds.3pm*
%dir %{perl_vendorarch}/auto/Time/
%{perl_vendorarch}/auto/Time/Piece/
%dir %{perl_vendorarch}/Time/
#%{perl_vendorarch}/Time/Piece/
%{perl_vendorarch}/Time/Piece.pm
%{perl_vendorarch}/Time/Seconds.pm

%changelog
* Tue Apr 25 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.30-1
- Updated to release 1.30.

* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Mon Mar  8 2010 Christoph Maser <cmr@financial.com> - 1.19-1
- Updated to version 1.19.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 1.17-1
- Updated to version 1.17.

* Tue Jan 12 2010 Christoph Maser <cmr@financial.com> - 1.16-1
- Updated to version 1.16.

* Mon Jun 29 2009 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 1.14-1
- Updated to version 1.14.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Thu Nov 22 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Tue Aug 22 2006 Dag Wieers <dag@wieers.com> - 1:1.09-1
- Revert back to non-developer release 1.09. (Aaron Scamehorn)

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.00_01-1
- Updated to release 2.00_01.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
