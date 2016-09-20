# $Id$
# Authority: dag
# Upstream: Agent Zhang <agentzh@gmail.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UML-Class-Simple

Summary: Render simple UML class diagrams, by loading the code
Name: perl-UML-Class-Simple
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UML-Class-Simple/

Source: http://www.cpan.org/modules/by-module/UML/UML-Class-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(Test::More)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(YAML::Syck)
BuildRequires: perl(PPI)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Template)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: graphviz
Requires: perl >= 0:5.004
Requires: perl(Test::More)
Requires: perl(File::Slurp)
Requires: perl(YAML::Syck)
Requires: perl(PPI)
Requires: perl(IPC::Run3)
Requires: perl(List::MoreUtils)
Requires: perl(Template)
Requires: perl(Class::Inspector)
Requires: perl(XML::LibXML)
Requires: graphviz


%description
Render simple UML class diagrams, by loading the code.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README samples/
%doc %{_mandir}/man1/umlclass.pl.1*
%doc %{_mandir}/man3/UML::Class::Simple.3pm*
%{_bindir}/umlclass.pl
%dir %{perl_vendorlib}/UML/
%dir %{perl_vendorlib}/UML/Class/
%{perl_vendorlib}/UML/Class/Simple.pm

%changelog
* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
