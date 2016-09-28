# $Id$
# Authority: dag
# Upstream: Ilya Martynov <ilya$martynov,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Dumper

Summary: Perl module that implements stringified perl data structures
Name: perl-Data-Dumper
Version: 2.161
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Dumper/

Source: http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/Data-Dumper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-Data-Dumper is a Perl module that implements stringified perl data
structures, suitable for both printing and eval.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST Todo
%dir %{perl_vendorarch}/Data/
%{perl_vendorarch}/Data/Dumper.pm
%dir %{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/auto/Data/Dumper/

%changelog
* Wed Sep 28 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.161-1
- Updated to release 2.161.

* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 2.125-1
- Updated to version 2.125.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 2.124-1
- Updated to version 2.124.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 2.121-1
- Initial package. (using DAR)
