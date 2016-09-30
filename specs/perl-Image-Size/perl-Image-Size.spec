# $Id$
# Authority: dries
# Upstream: Randy J. Ray <rjray$blackperl,com>

### EL6 ships with perl-Image-Size-3.2-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Size

Summary: Library to extract height/width from images
Name: perl-Image-Size
Version: 3.300
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Size/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJRAY/Image-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(Module::Build) >= 0.28
#BuildRequires: perl(Test::More) >= 0.80
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.006
Requires: perl(File::Spec) >= 0.8
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup

%description
A library to extract height/width from images.

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Image::Size.3pm*
%doc %{_mandir}/man1/imgsize.1*
%dir %{perl_vendorlib}/Image/
#%{perl_vendorlib}/Image/Size/
%{perl_vendorlib}/Image/Size.pm
#%dir %{perl_vendorlib}/auto/Image/
#%{perl_vendorlib}/auto/Image/Size/
%{_bindir}/imgsize

%changelog
* Fri Sep 30 2016 Dries Verachtert <dries.verachtert@dries.eu> - 3.300-1
- Updated to release 3.300.

* Wed Dec 23 2009 Christoph Maser <cmr@financial.com> - 3.220-1
- Updated to version 3.220.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 3.2-1
- Updated to version 3.2.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Updated to release 3.1.1.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 3.1-1
- Updated to release 3.1.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.992
- Initial package.
