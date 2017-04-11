# $Id$
# Authority: dries
# Upstream: Ted Pedersen <tpederse$d,umn,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-NSP

Summary: Extract collocations and Ngrams from text
Name: perl-Text-NSP
Version: 1.31
Release: 1%{?dist}
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-NSP/

Source: http://search.cpan.org/CPAN/authors/id/T/TP/TPEDERSE/Text-NSP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%filter_from_requires /^perl*/d
%filter_setup

%description
The Ngram Statistics Package (NSP) is a suite of programs that aids in 
analyzing Ngrams in text files. We define an Ngram as a sequence of 'n' 
tokens that occur within a window of at least 'n' tokens in the text; 
what constitutes a "token" can be defined by the user.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES FDL.txt GPL.txt INSTALL MANIFEST META.yml README TODO doc/
%doc %{_mandir}/man1/combig.pl.1*
%doc %{_mandir}/man1/count.pl.1*
%doc %{_mandir}/man1/count2huge.pl.1*
%doc %{_mandir}/man1/find-compounds.pl.1*
%doc %{_mandir}/man1/huge-count.pl.1*
%doc %{_mandir}/man1/huge-delete.pl.1*
%doc %{_mandir}/man1/huge-merge.pl.1*
%doc %{_mandir}/man1/huge-sort.pl.1*
%doc %{_mandir}/man1/huge-split.pl.1*
%doc %{_mandir}/man1/kocos.pl.1*
%doc %{_mandir}/man1/rank.pl.1*
%doc %{_mandir}/man1/statistic.pl.1*
%doc %{_mandir}/man3/Text::NSP.3pm*
%doc %{_mandir}/man3/Text::NSP::*.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/NSP/
%{_bindir}/combig-script.sh
%{_bindir}/combig.pl
%{_bindir}/count.pl
%{_bindir}/count2huge.pl
%{_bindir}/find-compounds.pl
%{_bindir}/huge-count.pl
%{_bindir}/huge-delete.pl
%{_bindir}/huge-merge.pl
%{_bindir}/huge-sort.pl
%{_bindir}/huge-split.pl
%{_bindir}/kocos-script.sh
%{_bindir}/kocos.pl
%{_bindir}/rank-script.sh
%{_bindir}/rank.pl
%{_bindir}/statistic.pl
%{perl_vendorlib}/Text/NSP/
%{perl_vendorlib}/Text/NSP.pm

%changelog
* Tue Apr 11 2017 Dries Verachtert <dries.verachtert@dries.eu> - 1.31-1
- Updated to release 1.31.

* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.21-1
- Updated to version 1.21.

* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Thu Mar 11 2010 Christoph Maser <cmr@financial.com> - 1.13-1
- Updated to version 1.13.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.11-1
- Updated to version 1.11.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
