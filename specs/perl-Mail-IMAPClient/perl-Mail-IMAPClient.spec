# $Id$
# Authority: dries
# Upstream: Phil Pearl (Lobbes) <phil @ perkpartners.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-IMAPClient

Summary: IMAP4 client library
Name: perl-Mail-IMAPClient
Version: 3.39
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-IMAPClient/

Source: http://search.cpan.org/CPAN/authors/id/P/PL/PLOBBES/Mail-IMAPClient-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Errno)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(IO::Socket::INET) >= 1.26
BuildRequires: perl(List::Util)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Parse::RecDescent) >= 1.94
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl(Carp)
Requires: perl(Errno)
Requires: perl(Fcntl)
Requires: perl(File::Temp)
Requires: perl(IO::File)
Requires: perl(IO::Select)
Requires: perl(IO::Socket)
Requires: perl(IO::Socket::INET) >= 1.26
Requires: perl(List::Util)
Requires: perl(MIME::Base64)
Requires: perl(Parse::RecDescent) >= 1.94
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
This module provides perl routines that simplify a sockets connection
to and an IMAP conversation with an IMAP server.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README test_template.txt examples/
%doc %{_mandir}/man3/Mail::IMAPClient.3pm*
%doc %{_mandir}/man3/Mail::IMAPClient::*.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/IMAPClient/
%{perl_vendorlib}/Mail/IMAPClient.pm
%{perl_vendorlib}/Mail/IMAPClient.pod

%changelog
* Sun Jun 25 2017 Dries Verachtert <dries.verachtert@dries.eu> - 3.39-1
- Updated to release 3.39.

* Tue Feb 23 2016 Dries Verachtert <dries.verachtert@dries.eu> - 3.38-1
- Updated to release 3.38.

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 3.23-1
- Updated to version 3.23.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 3.22-1
- Updated to version 3.22.

* Tue Dec 15 2009 Christoph Maser <cmr@financial.com> - 3.21-1
- Updated to version 3.21.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 3.20-1
- Updated to version 3.20.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 3.19-1
- Updated to version 3.19.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 3.11-1
- Updated to release 3.11.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 3.08-1
- Updated to release 3.08.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 3.07-1
- Updated to release 3.07.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 3.05-1
- Updated to release 3.05.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 3.04-1
- Updated to release 3.04.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 3.03-1
- Updated to release 3.03.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 3.02-1
- Updated to release 3.02.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 3.00-1
- Updated to release 3.00.

* Sun Jul 31 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.9-1
- Initial package.
