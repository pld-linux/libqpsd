#
# Conditional build:
%bcond_without	qt4	# Qt 4 version
%bcond_without	qt5	# Qt 5 version
#
Summary:	PSD (Photoshop Document) & PSB (Photoshop Big) library and plugin for Qt/C++
Summary(pl.UTF-8):	Biblioteka oraz wtyczka PSD (Photoshop Document) i PSB (Photoshop Big) dla Qt/C++
Name:		libqpsd
Version:	0
%define	snap	20151125
%define	gitref	3915ad553f020d438adc5636d99e256de905e1bb
Release:	0.%{snap}.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/Code-ReaQtor/libqpsd/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	fa7955b2bfa468ff99485e6859dabea5
Patch0:		%{name}-build.patch
URL:		https://github.com/Code-ReaQtor/libqpsd
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PSD (Photoshop Document) & PSB (Photoshop Big) library and plugin for
Qt/C++.

%description -l pl.UTF-8
Biblioteka oraz wtyczka PSD (Photoshop Document) i PSB (Photoshop Big)
dla Qt/C++.

%package qt4
Summary:	PSD (Photoshop Document) & PSB (Photoshop Big) library and plugin for Qt 4
Summary(pl.UTF-8):	Biblioteka oraz wtyczka PSD (Photoshop Document) i PSB (Photoshop Big) dla Qt 4
Group:		Libraries

%description qt4
PSD (Photoshop Document) & PSB (Photoshop Big) library and plugin for
Qt 4.

%description qt4 -l pl.UTF-8
Biblioteka oraz wtyczka PSD (Photoshop Document) i PSB (Photoshop Big)
dla Qt 4.

%package qt4-devel
Summary:	Header file for QPSD library (Qt 4 version)
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki QPSD (wersja dla Qt 4)
Group:		Development/Libraries
Requires:	%{name}-qt4 = %{version}-%{release}
Requires:	QtCore-devel >= 4
Requires:	QtGui-devel >= 4

%description qt4-devel
Header file for QPSD library (Qt 4 version).

%description qt4-devel -l pl.UTF-8
Plik nagłówkowy biblioteki QPSD (wersja dla Qt 4).

%package qt5
Summary:	PSD (Photoshop Document) & PSB (Photoshop Big) library and plugin for Qt 5
Summary(pl.UTF-8):	Biblioteka oraz wtyczka PSD (Photoshop Document) i PSB (Photoshop Big) dla Qt 5
Group:		Libraries

%description qt5
PSD (Photoshop Document) & PSB (Photoshop Big) library and plugin for
Qt 5.

%description qt5 -l pl.UTF-8
Biblioteka oraz wtyczka PSD (Photoshop Document) i PSB (Photoshop Big)
dla Qt 5.

%package qt5-devel
Summary:	Header file for QPSD library (Qt 5 version)
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki QPSD (wersja dla Qt 5)
Group:		Development/Libraries
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	Qt5Core-devel >= 5
Requires:	Qt5Gui-devel >= 5

%description qt5-devel
Header file for QPSD library (Qt 5 version).

%description qt5-devel -l pl.UTF-8
Plik nagłówkowy biblioteki QPSD (wersja dla Qt 5).

%prep
%setup -q -n %{name}-%{gitref}
%patch0 -p1

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
qmake-qt4 ../main.pro \
	BUILD_DIR=build-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
qmake-qt5 ../main.pro \
	BUILD_DIR=build-qt5 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# useless symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqpsd.so.1.0
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# useless symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqpsd5.so.1.0
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libqpsd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpsd.so.1
%attr(755,root,root) %{_libdir}/qt4/plugins/imageformats/libqpsd.so

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqpsd.so
%{_includedir}/qt4/qpsdhandler.h
%endif

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libqpsd5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqpsd5.so.1
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqpsd.so

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqpsd5.so
%{_includedir}/qt5/qpsdhandler.h
%endif
