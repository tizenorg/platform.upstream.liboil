Name:           liboil
BuildRequires:  glib2-devel
Version:        0.3.17
Release:        1
Url:            http://liboil.freedesktop.org/wiki/
Group:          System/Libraries
License:        BSD-2-Clause
Summary:        Library of Optimized Inner Loops
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf

%description
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to floating-point
numbers or multiplying and summing an array of N numbers. Such
functions are candidates for significant optimization using various
techniques, especially by using extended instructions provided by
modern CPUs (Altivec, MMX, SSE, etc.).

Many multimedia applications and libraries already do similar things
internally. The goal of this project is to consolidate some of the code
used by various multimedia projects and also make optimizations easier
to use by a broader range of applications.

%package devel
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Summary:        Library of Optimized Inner Loops
Requires:       %{name} = %{version} glibc-devel

%description devel
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to floating-point
numbers or multiplying and summing an array of N numbers. Such
functions are candidates for significant optimization using various
techniques, especially by using extended instructions provided by
modern CPUs (Altivec, MMX, SSE, etc.).

Many multimedia applications and libraries already do similar things
internally. The goal of this project is to consolidate some of the code
used by various multimedia projects, and also make optimizations easier
to use by a broader range of applications.


%prep
%setup -q

%build
%configure --disable-static --with-pic
%__make %{?jobs:-j%jobs}
# Do NOT! disable running the testsuite or make failures
# non-fatal for the build!

%check
%__make check

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr (-, root, root)
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root)
%{_bindir}/oil-bugreport
%{_includedir}/liboil-*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
