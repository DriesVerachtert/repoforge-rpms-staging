# $Id$
# Authority: dag
# Upstream: Greg McCarroll <greg$mccarroll,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jabber-SimpleSend

Summary: Perl module to send a Jabber message
Name: perl-Jabber-SimpleSend
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jabber-SimpleSend/

Source: http://www.cpan.org/modules/by-module/Jabber/Jabber-SimpleSend-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Jabber-SimpleSend is a Perl module to send a Jabber message.

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
%doc %{_mandir}/man3/Jabber::SimpleSend.3pm*
%dir %{perl_vendorlib}/Jabber/
#%{perl_vendorlib}/Jabber/SimpleSend/
%{perl_vendorlib}/Jabber/SimpleSend.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
