# $Id$
# Authority: dag
# Upstream: Guillaume Rousse <grousse$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Youri-Media
%define real_version 0.002001

Summary: Perl module that implements the abstract media class
Name: perl-Youri-Media
Version: 0.2.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Youri-Media/

Source: http://www.cpan.org/authors/id/G/GR/GROUSSE/Youri-Media-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Youri-Media is a Perl module that implements the abstract media class.

This package contains the following Perl module:

    Youri::Media

%prep
%setup -n %{real_name}-v%{version}

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Youri::Media.3pm*
%doc %{_mandir}/man3/Youri::Media::URPM.3pm*
%dir %{perl_vendorlib}/Youri/
%{perl_vendorlib}/Youri/Media/
%{perl_vendorlib}/Youri/Media.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
