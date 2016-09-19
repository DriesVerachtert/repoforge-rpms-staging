# $Id$
# Authority: dag
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-IMAP-Simple-SSL

Summary: Perl module that implements SSL support for Net::IMAP::Simple
Name: perl-Net-IMAP-Simple-SSL
Version: 1.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-IMAP-Simple-SSL/

Source: http://www.cpan.org/modules/by-module/Net/Net-IMAP-Simple-SSL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Net-IMAP-Simple-SSL is a Perl module that implements SSL support for
Net::IMAP::Simple.

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
%doc %{_mandir}/man3/Net::IMAP::Simple::SSL.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/IMAP/
%dir %{perl_vendorlib}/Net/IMAP/Simple/
#%{perl_vendorlib}/Net/IMAP/Simple/SSL/
%{perl_vendorlib}/Net/IMAP/Simple/SSL.pm

%changelog
* Fri Sep 28 2007 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
