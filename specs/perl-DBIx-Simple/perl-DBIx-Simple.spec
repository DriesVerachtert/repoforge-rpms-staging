# $Id$
# Authority: cmr
# Upstream: Juerd Waalboer <spamcollector_cpan$juerd,nl>

### EL6 ships with perl-DBIx-Simple-1.32-3.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Simple

Summary: Perl module named DBIx-Simple
Name: perl-DBIx-Simple
Version: 1.35
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Simple/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-DBIx-Simple is a Perl module.

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
%doc %{_mandir}/man3/DBIx::Simple.3pm*
%doc %{_mandir}/man3/DBIx::Simple::Comparison.3pm.gz
%doc %{_mandir}/man3/DBIx::Simple::Examples.3pm.gz
%doc %{_mandir}/man3/DBIx::Simple::Result::RowObject.3pm.gz
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/Simple/Comparison.pod
%{perl_vendorlib}/DBIx/Simple/Examples.pod
%{perl_vendorlib}/DBIx/Simple.pm
%{perl_vendorlib}/DBIx/Simple/Result/RowObject.pm

%changelog
* Sat Oct 31 2015 Dries Verachtert <dries.verachtert@dries.eu> - 1.35-1
- Updated to release 1.35.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 1.32-1
- Initial package. (using DAR)
