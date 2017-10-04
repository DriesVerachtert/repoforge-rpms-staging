# $Id$
# Authority: dries
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-Attachment-Stripper

Summary: Strip the attachments from a mail
Name: perl-Email-MIME-Attachment-Stripper
Version: 1.317
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-Attachment-Stripper/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-Attachment-Stripper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this perl module, you can strip attachments from a mail.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::MIME::Attachment::Stripper.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/MIME/
%dir %{perl_vendorlib}/Email/MIME/Attachment/
#%{perl_vendorlib}/Email/MIME/Attachment/Stripper/
%{perl_vendorlib}/Email/MIME/Attachment/Stripper.pm

%changelog
* Wed Oct 04 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.317-1
- Updated to release 1.317.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.316-1
- Updated to version 1.316.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.315-1
- Updated to release 1.315.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.314-1
- Updated to release 1.314.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.31-1
- Updated to release 1.31.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
