# $Id$
# Authority: dries
# Upstream: David Muir Sharnoff <muir$idiom,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Flock

Summary: File locking with flock
Name: perl-File-Flock
Version: 2014.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Flock/

Source: http://www.cpan.org/modules/by-module/File/File-Flock-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
File::Flock is a wrapper around the flock() call.  The only thing it
does that is special is that it creates the lock file if the lock file
does not already exist.

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
%doc Changes MANIFEST META.* README
%doc %{_mandir}/man3/File::Flock.3pm*
%doc %{_mandir}/man3/File::Flock::Forking.3pm.gz
%doc %{_mandir}/man3/File::Flock::Subprocess.3pm.gz
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Flock/
%{perl_vendorlib}/File/Flock.pm
%{perl_vendorlib}/File/Flock/Forking.pm
%{perl_vendorlib}/File/Flock/Subprocess.pm

%changelog
* Mon Aug 07 2017 Dries Verachtert <dries.verachtert@dries.eu> - 2014.01-1
- Updated to release 2014.01.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2008.01-1
- Updated to version 2008.01.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 104.111901-1
- Initial package.
