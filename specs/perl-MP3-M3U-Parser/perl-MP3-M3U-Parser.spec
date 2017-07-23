# $Id$
# Authority: dries
# Upstream: Burak Gürsoy <burak$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MP3-M3U-Parser

Summary: MP3 playlist parser
Name: perl-MP3-M3U-Parser
Version: 2.32
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MP3-M3U-Parser/

Source: http://www.cpan.org/modules/by-module/MP3/MP3-M3U-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml build_requires
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(Cwd)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(Text::Template)


%description
Parses M3U mp3 playlists and if wanted, exports the parsed data to
formats like xml and html.

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
%doc %{_mandir}/man3/MP3::M3U::Parser.3pm*
%doc %{_mandir}/man3/MP3::M3U::Parser::Constants.3pm*
%doc %{_mandir}/man3/MP3::M3U::Parser::Dummy.3pm*
%doc %{_mandir}/man3/MP3::M3U::Parser::Export.3pm*
%dir %{perl_vendorlib}/MP3/
%dir %{perl_vendorlib}/MP3/M3U/
%{perl_vendorlib}/MP3/M3U/Parser.pm
%dir %{perl_vendorlib}/MP3/M3U/Parser/
%{perl_vendorlib}/MP3/M3U/Parser/Constants.pm
%{perl_vendorlib}/MP3/M3U/Parser/Dummy.pm
%{perl_vendorlib}/MP3/M3U/Parser/Export.pm

%changelog
* Sun Jul 23 2017 Dries Verachtert <dries.verachtert@dries.eu> - 2.32-1
- Updated to release 2.32.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 2.24-1
- Updated to version 2.24.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.23-1
- Updated to version 2.23.

* Sat Jun 16 2007 Who Knows ( aka Jim ) <quien-sabe@metaorg.com> - 2.20-1
- Updated to release 2.20.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Update to release 2.1.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
