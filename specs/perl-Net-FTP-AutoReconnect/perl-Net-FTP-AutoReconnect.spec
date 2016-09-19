# $Id$
# Authority: dag
# Upstream: Scott Gifford <sgifford$suspectclass,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-FTP-AutoReconnect

Summary: FTP client class with automatic reconnect on failure
Name: perl-Net-FTP-AutoReconnect
Version: 0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-FTP-AutoReconnect/

Source: http://www.cpan.org/modules/by-module/Net/Net-FTP-AutoReconnect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml requires
BuildRequires: perl(Fcntl)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(Net::FTP)
BuildRequires: perl(ExtUtils::MakeMaker)


%description
FTP client class with automatic reconnect on failure.

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
%doc MANIFEST MANIFEST.SKIP META.yml
%doc %{_mandir}/man3/Net::FTP::AutoReconnect.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/FTP/
#%{perl_vendorlib}/Net/FTP/AutoReconnect/
%{perl_vendorlib}/Net/FTP/AutoReconnect.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.3-1
- Updated to version 0.3.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
