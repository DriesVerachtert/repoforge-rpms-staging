# $Id$
# Authority: dag
# Upstream: David Glasser <glasser@bestpractical.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Server-Simple-Recorder

Summary: Mixin to record HTTP::Server::Simple's sockets
Name: perl-HTTP-Server-Simple-Recorder
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Server-Simple-Recorder/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Server-Simple-Recorder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Mixin to record HTTP::Server::Simple's sockets.

This package contains the following Perl module:

    HTTP::Server::Simple::Recorder

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Server::Simple::Recorder.3pm*
%dir %{perl_vendorlib}/HTTP/
%dir %{perl_vendorlib}/HTTP/Server/
%dir %{perl_vendorlib}/HTTP/Server/Simple/
#%{perl_vendorlib}/HTTP/Server/Simple/Recorder/
%{perl_vendorlib}/HTTP/Server/Simple/Recorder.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
