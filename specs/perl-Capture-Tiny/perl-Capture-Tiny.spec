# $Id$
# Authority: dag
# Upstream: David Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Capture-Tiny

Summary: Capture STDOUT and STDERR from Perl, XS or external programs
Name: perl-Capture-Tiny
Version: 0.44
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Capture-Tiny/

#Source: http://www.cpan.org/modules/by-module/Capture/Capture-Tiny-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
#BuildRequires: perl(File::Temp) >= 0.14
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Handle)
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl >= 5.006
Requires: perl(Exporter)
Requires: perl(File::Spec)
#Requires: perl(File::Temp) >= 0.14
Requires: perl(File::Temp)
Requires: perl(IO::Handle)
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup


%description
Capture STDOUT and STDERR from Perl, XS or external programs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes LICENSE MANIFEST META.yml README Todo examples/
%doc %{_mandir}/man3/Capture::Tiny.3pm*
%dir %{perl_vendorlib}/Capture/
#%{perl_vendorlib}/Capture/Tiny/
%{perl_vendorlib}/Capture/Tiny.pm
#%{perl_vendorlib}/Capture/Tiny.pod

%changelog
* Fri Sep 23 2016 Dries Verachtert <dries.verachtert@dries.eu> - 0.44-1
- Updated to release 0.44.

* Mon Jan 24 2011 Steve Huff <shuff@vecna.org> - 0.08-1
- Updated to version 0.08.

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.06-2
- Remove version number for Test::More requirement

* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
