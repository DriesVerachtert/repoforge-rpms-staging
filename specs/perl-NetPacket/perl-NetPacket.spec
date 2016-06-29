# $Id$
# Authority: dag
# Upstream: Yanick Champoux <yanick$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name NetPacket

Summary: Assemble and dissassemble network packets
Name: perl-NetPacket
Version: 1.6.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NetPacket/

Source: http://search.cpan.org/CPAN/authors/id/Y/YA/YANICK/NetPacket-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(Carp)
BuildRequires: perl(Module::Build) >= 0.3601
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.94
Requires: perl >= 0:5.004

%description
These modules do basic disassembly of network packets of various Internet
protocols.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README README.mkdn SIGNATURE
%doc %{_mandir}/man3/NetPacket.3pm*
%doc %{_mandir}/man3/NetPacket::*.3pm*
%{perl_vendorlib}/NetPacket/
%{perl_vendorlib}/NetPacket.pm

%changelog
* Wed Jun 29 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.6.0-1
- Updated to release 1.6.0.

* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.43.2-1
- Updated to release 0.43.2.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.41.1-1
- Updated to version 0.41.1.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
