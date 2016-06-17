# $Id$
# Authority: cmr
# Upstream: Leon Brocard <acme$astray,com>,

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Stomp

Summary: A Streaming Text Orientated Messaging Protocol Client
Name: perl-Net-Stomp
Version: 0.57
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Stomp/

Source: http://www.cpan.org/modules/by-module/Net/Net-Stomp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A Streaming Text Orientated Messaging Protocol Client.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/Net::Stomp.3pm*
%doc %{_mandir}/man3/Net::Stomp::Frame.3pm*
%doc %{_mandir}/man3/Net::Stomp::StupidLogger.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Stomp/Frame.pm
%{perl_vendorlib}/Net/Stomp.pm
%{perl_vendorlib}/Net/Stomp/StupidLogger.pm

%changelog
* Fri Jun 17 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.57-1
- Updated to release 0.57.

* Tue Jan 06 2009 Christoph Maser <cmr@financial.com> - 0.34-1
- Initial package. (using DAR)
