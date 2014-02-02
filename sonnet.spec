%define major 5
%define libname %mklibname KF5ItemViews %{major}
%define devname %mklibname KF5ItemViews -d
%define debug_package %{nil}

Name: sonnet
Version: 4.95.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 spell checking library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5

%description
Sonnet provides spell-checking capabilities to applications.

Sonnet uses plugins for the actual spell-checking, and provides a
Qt-style abstraction on top of these. Available backends include
aspell, enchant, hspell and hunspell.

%package -n %{libname}
Summary: The KDE Frameworks 5 spell checking library
Group: System/Libraries

%description -n %{libname}
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

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%dir %{_libdir}/plugins
%dir %{_libdir}/plugins/kf5
%dir %{_libdir}/plugins/kf5/plugins
%dir %{_libdir}/plugins/kf5/plugins/sonnet_clients
%dir %{_libdir}/plugins/kf5/sonnet_clients

%files enchant
%{_libdir}/plugins/kf5/plugins/sonnet_clients/kspell_enchant.so

%files hunspell
%{_libdir}/plugins/kf5/plugins/sonnet_clients/kspell_hunspell.so

%files aspell
%{_libdir}/plugins/kf5/sonnet_clients/kspell_aspell.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Sonnet
