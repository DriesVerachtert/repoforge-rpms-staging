# $Id$
# Authority: rudolf
# Upstream: <physfs$icculus,org>

Summary: Library to provide abstract access to various archives
Name: physfs
Version: 2.0.3
Release: 1%{?dist}
License: zlib License
Group: System Environment/Libraries
URL: http://www.icculus.org/physfs/

Source: http://www.icculus.org/physfs/downloads/physfs-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, readline-devel, zlib-devel, cmake, doxygen, gcc-c++

%description
A library to provide abstract access to various archives.
It is intended for use in video games.
The programmer defines a "write directory" on the physical filesystem.
No file writing done through the PhysicsFS API can leave that write directory.

%package devel
Summary: Headers for developing programs that will use physfs
Group: Development/Libraries
Requires: %{name} = %{version}, zlib-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use physfs

%prep
%setup

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPREFIX=%{_prefix} .
%{__make}

%install
%{__rm} -rf %{buildroot}
# fix lib path on x86_64
%{__perl} -pi.orig -e 's|\${CMAKE_INSTALL_PREFIX}/lib|%{_libdir}|g' cmake_install.cmake
%{__make} install \
	DESTDIR="%{buildroot}" \
	LIB_SUFFIX="%{?lib_suffix}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG.txt CREDITS.txt INSTALL.txt LICENSE.txt TODO.txt
%{_libdir}/libphysfs*.so.*

%files -n %{name}-devel
%defattr(-, root, root, 0755)
%{_bindir}/test_physfs
%{_includedir}/physfs.h
%{_libdir}/libphysfs.a
%{_libdir}/libphysfs.so

%changelog
* Wed Nov  6 2013 Dries Verachtert <dries.verachtert@dries.eu> - 2.0.3-1
- Updated to release 2.0.3.

* Wed Dec 29 2004 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Added x86_64 fix.

* Sun Oct 12 2003 Che
- initial rpm release
