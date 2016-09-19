# $Id$
# Authority: dag
# Upstream: Gregor Mosheh <stigmata$blackangel,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-CalendarMonthSimple

Summary: Perl module for Generating HTML Calendars
Name: perl-HTML-CalendarMonthSimple
Version: 1.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-CalendarMonthSimple/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-CalendarMonthSimple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-HTML-CalendarMonthSimple is a Perl module for Generating HTML Calendars.

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
%doc MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man3/HTML::CalendarMonthSimple.3pm*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/CalendarMonthSimple.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.25-1
- Initial package. (using DAR)
