# $Id$
# Authority: dag
# Upstream: Mark Overmeer

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Report

Summary: Report a problem, pluggable handlers and language support
Name: perl-Log-Report
Version: 1.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Report/

Source: http://www.cpan.org/modules/by-module/Log/Log-Report-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Report a problem, pluggable handlers and language support.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Log::Report.3pm*
%doc %{_mandir}/man3/Log::Report::*.3pm*
%doc %{_mandir}/man3/Dancer2::Logger::LogReport.3pm*
%doc %{_mandir}/man3/Dancer2::Plugin::LogReport.3pm*
%doc %{_mandir}/man3/Dancer2::Plugin::LogReport::Message.3pm*
%doc %{_mandir}/man3/Dancer::Logger::LogReport.3pm*
%doc %{_mandir}/man3/MojoX::Log::Report.3pm*

#{_bindir}/xgettext-perl
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/Report/
%{perl_vendorlib}/Dancer/Logger/
%{perl_vendorlib}/Dancer2/Logger/
%{perl_vendorlib}/Dancer2/Plugin/
%{perl_vendorlib}/Dancer2/Plugin/LogReport.p*
%{perl_vendorlib}/Dancer2/Plugin/LogReport/
%{perl_vendorlib}/Log/Report.pm
%{perl_vendorlib}/Log/Report.pod
%{perl_vendorlib}/MojoX/Log/Report.p*
#exclude %{perl_vendorlib}/Log/Report/Win32Locale.pm
#exclude %{perl_vendorlib}/Log/Report/Win32Locale.pod

%changelog
* Sat Jul 09 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.16-1
- Updated to release 1.16.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.25-1
- Updated to version 0.25.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.24-1
- Updated to version 0.24.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.14-2
- Exclude Win32 specific modules.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
