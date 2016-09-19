# $Id$
# Authority: dag
# Upstream: Casey West <casey$geeknest,com>

### EL6 ships with perl-Net-SMTP-SSL-1.01-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SMTP-SSL

Summary: SSL support for Net::SMTP
Name: perl-Net-SMTP-SSL
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SMTP-SSL/

Source: http://www.cpan.org/modules/by-module/Net/Net-SMTP-SSL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
SSL support for Net::SMTP.

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
%doc %{_mandir}/man3/Net::SMTP::SSL.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/SMTP/
#%{perl_vendorlib}/Net/SMTP/SSL/
%{perl_vendorlib}/Net/SMTP/SSL.pm

%changelog
* Tue Mar 24 2009 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
