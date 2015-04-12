%define major 5
%define libname %mklibname KF5SonnetCore %{major}
%define devname %mklibname KF5SonnetCore -d
%define uilibname %mklibname KF5SonnetUi %{major}
%define uidevname %mklibname KF5SonnetUi -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: sonnet
Version: 5.9.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 spell checking library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
Requires: %{libname} = %{EVRD}

%description
Sonnet provides spell-checking capabilities to applications.

Sonnet uses plugins for the actual spell-checking, and provides a
Qt-style abstraction on top of these. Available backends include
aspell, enchant, hspell and hunspell.

%package -n %{libname}
Summary: The KDE Frameworks 5 spell checking library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Sonnet provides spell-checking capabilities to applications.

Sonnet uses plugins for the actual spell-checking, and provides a
Qt-style abstraction on top of these. Available backends include
aspell, enchant, hspell and hunspell.

%package -n %{uilibname}
Summary: The KDE Frameworks 5 spell checking UI library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{uilibname}
Sonnet provides spell-checking capabilities to applications.

Sonnet uses plugins for the actual spell-checking, and provides a
Qt-style abstraction on top of these. Available backends include
aspell, enchant, hspell and hunspell.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Sonnet provides spell-checking capabilities to applications.

Sonnet uses plugins for the actual spell-checking, and provides a
Qt-style abstraction on top of these. Available backends include
aspell, enchant, hspell and hunspell.

%package -n %{uidevname}
Summary: UI Development files for %{name}
Group: Development/KDE and Qt
Requires: %{uilibname} = %{EVRD}
Requires: %{devname} = %{EVRD}

%description -n %{uidevname}
UI Development files (Headers etc.) for %{name}.

Sonnet provides spell-checking capabilities to applications.

Sonnet uses plugins for the actual spell-checking, and provides a
Qt-style abstraction on top of these. Available backends include
aspell, enchant, hspell and hunspell.

%package enchant
Summary: Enchant backend for the Sonnet spell checking library
Requires: %{libname} = %{EVRD}
Group: System/Libraries
Provides: sonnet-backend = %{EVRD}
BuildRequires: pkgconfig(enchant)

%description enchant
Enchant backend for the Sonnet spell checking library

%package hunspell
Summary: Hunspell backend for the Sonnet spell checking library
Requires: %{libname} = %{EVRD}
Group: System/Libraries
Provides: sonnet-backend = %{EVRD}
BuildRequires: pkgconfig(hunspell)

%description hunspell
Hunspell backend for the Sonnet spell checking library

%package aspell
Summary: Aspell backend for the Sonnet spell checking library
Requires: %{libname} = %{EVRD}
Group: System/Libraries
Provides: sonnet-backend = %{EVRD}
BuildRequires: aspell aspell-devel

%description aspell
Aspell backend for the Sonnet spell checking library

%package hspell
Summary: Hspell backend for the Sonnet spell checking library
Requires: %{libname} = %{EVRD}
Group: System/Libraries
Provides: sonnet-backend = %{EVRD}
BuildRequires: hspell-devel

%description hspell
Hspell backend for the Sonnet spell checking library

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%dir %{_datadir}/kf5/sonnet
%{_datadir}/kf5/sonnet/trigrams.map
%dir %{_libdir}/qt5/plugins/kf5
%dir %{_libdir}/qt5/plugins/kf5/sonnet

%files -n %{libname}
%{_libdir}/*Core.so.%{major}
%{_libdir}/*Core.so.%{version}

%files -n %{uilibname}
%{_libdir}/*Ui.so.%{major}
%{_libdir}/*Ui.so.%{version}

# Enchant isn't supported in 4.96.0, but will likely come back
#files enchant
#{_libdir}/qt5/plugins/sonnet_clients/sonnet_enchant.so

%files hunspell
%{_libdir}/qt5/plugins/kf5/sonnet/hunspell.so

%files aspell
%{_libdir}/qt5/plugins/kf5/sonnet/aspell.so

%files hspell
%{_libdir}/qt5/plugins/kf5/sonnet/hspell.so

%files -n %{devname}
%{_includedir}/KF5/sonnet_version.h
%{_includedir}/KF5/SonnetCore
%{_libdir}/*Core.so
%{_libdir}/cmake/KF5Sonnet
%{_libdir}/qt5/mkspecs/modules/*Core*

%files -n %{uidevname}
%{_includedir}/KF5/SonnetUi
%{_libdir}/*Ui.so
%{_libdir}/qt5/mkspecs/modules/*Ui*
