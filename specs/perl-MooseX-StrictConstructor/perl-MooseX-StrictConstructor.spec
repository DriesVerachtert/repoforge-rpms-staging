# $Id$
# Authority: shuff
# Upstream: Dave Rolsky <autarch$urth,org>
# ExcludeDist: el2 el3 el4 el5
# Rationale: conflicts with older perl-Moose

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-StrictConstructor

Summary: Make your object constructors blow up on unknown attributes
Name: perl-%{real_name}
Version: 0.19
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-StrictConstructor/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/MooseX-StrictConstructor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose) >= 0.94
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Moose) >= 0.74


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Simply loading this module makes your constructors "strict". If your
constructor is called with an attribute init argument that your class does not
declare, then it calls "Carp::confess()". This is a great way to catch small
typos.

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
%doc Changes INSTALL MANIFEST META.json README SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/*

%changelog
* Thu Nov 26 2015 Dries Verachtert <dries.verachtert@dries.eu> - 0.19-1
- Updated to release 0.19.

* Tue Aug 23 2011 Steve Huff <shuff@vecna.org> - 0.16-1
- Updated to version 0.16 (el6-only).
- Split out perl-MooseX-StrictConstructor-0.08 as its own spec.

* Fri Dec 18 2009 Steve Huff <shuff@vecna.org> - 0.08-1
- Initial package.
