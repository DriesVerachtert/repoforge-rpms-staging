# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-IMAP-Simple

Summary: Perl extension for simple IMAP account handling
Name: perl-Net-IMAP-Simple
Version: 1.2206
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IMAP-Simple/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JETTERO/Net-IMAP-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl >= 5.008
Requires: perl(IO::Select)
Requires: perl(IO::Socket)
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup

%description
This module is a simple way to access IMAP accounts.

%prep
%setup -n %{real_name}-%{version}

%build
echo y | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%dir %{perl_vendorlib}/Net/IMAP/
%{perl_vendorlib}/Net/IMAP/Simple.pm
%{perl_vendorlib}/Net/IMAP/Simple.pod
%{perl_vendorlib}/Net/IMAP/Simple/PipeSocket.pm
%{perl_vendorlib}/Net/IMAP/SimpleX.pm
%{perl_vendorlib}/Net/IMAP/SimpleX.pod

%changelog
* Thu Jan 14 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.2206-1
- Updated to release 1.2206.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.1910-1
- Updated to version 1.1910.

* Thu Jul 30 2009 Christoph Maser <cmr@financial.com> - 1.1907-1
- Updated to version 1.1907.

* Wed Jul 22 2009 Christoph Maser <cmr@financial.com> - 1.1905-1
- Updated to version 1.1905.

* Mon Jul 13 2009 Christoph Maser <cmr@financial.com> - 1.1900-1
- Updated to version 1.1900.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.1801-1
- Updated to version 1.1801.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.101-1
- Updated to release 0.101.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Initial package.
