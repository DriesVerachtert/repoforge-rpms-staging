# $Id$
# Authority: dries

Summary: Fast artificial neural network library
Name: fann
Version: 2.2.0
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://leenissen.dk/fann/wp/

Source: http://sourceforge.net/projects/fann/files/fann/%{version}/FANN-%{version}-Source.zip/download
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++, cmake

%description
Fann is a fast artificial neural network library. More information and a lot
of documentation is available at http://fann.sourceforge.net/

%prep
%setup -n FANN-%{version}-Source

%build
#cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_SUFFIX=64 .
%{__perl} -pi.orig -e "s|SET\(PKGCONFIG_INSTALL_DIR .*|SET (PKGCONFIG_INSTALL_DIR /%{_lib}/pkgconfig)|" CMakeLists.txt
%{__cmake} -DCMAKE_INSTALL_PREFIX=%{_prefix} %{_cmake_lib_suffix64} -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig .
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%package devel
Summary: fann devel
Group: Development/Libraries
Requires: fann = %{version}-%{release}

%description devel
Development headers of fann: fast artificial neural network library

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING.txt README.txt
%{_libdir}/libfloatfann.so.*
%{_libdir}/libdoublefann.so.*
%{_libdir}/libfixedfann.so.*
%{_libdir}/libfann.so.*
%{_libdir}/pkgconfig/fann.pc


%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libfloatfann.so
%{_libdir}/libdoublefann.so
%{_libdir}/libfixedfann.so
%{_libdir}/libfann.so
#%{_libdir}/libfann.a
#%{_libdir}/libfann.la
%{_includedir}/compat_time.h
%{_includedir}/doublefann.h
%{_includedir}/fann*.h
%{_includedir}/fixedfann.h
%{_includedir}/floatfann.h
#%{_libdir}/libdoublefann.a
#%{_libdir}/libdoublefann.la
#%{_libdir}/libfixedfann.a
#%{_libdir}/libfixedfann.la
#%{_libdir}/libfloatfann.a
#%{_libdir}/libfloatfann.la

%changelog
* Sun Sep 25 2016 Dries Verachtert <dries.verachtert@dries.eu> - 2.2.0-1
- Updated to release 2.2.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-1
- Updated to release 2.0.0.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 1.2.0-1
- Update to 1.2.0

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 1.1.0-1
- update to 1.1.0

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.0.5-1
- cleanup of spec file
- update from 1.0.4 to 1.0.5

* Sat Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 1.0.4-2
- first packaging for Fedora Core 1
