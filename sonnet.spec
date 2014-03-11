%define major 5
%define libname %mklibname KF5ItemViews %{major}
%define devname %mklibname KF5ItemViews -d
%define debug_package %{nil}

Name: sonnet
Version: 4.97.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
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
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

%files
%{_datadir}/sonnet/trigrams.map
%dir %{_libdir}/plugins
%dir %{_libdir}/plugins/kf5
%dir %{_libdir}/plugins/kf5/sonnet_clients

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

# Enchant isn't supported in 4.96.0, but will likely come back
#files enchant
#{_libdir}/plugins/kf5/sonnet_clients/sonnet_enchant.so

%files hunspell
%{_libdir}/plugins/kf5/sonnet_clients/sonnet_hunspell.so

%files aspell
%{_libdir}/plugins/kf5/sonnet_clients/sonnet_aspell.so

%files hspell
%{_libdir}/plugins/kf5/sonnet_clients/sonnet_hspell.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Sonnet
%{_libdir}/qt5/mkspecs/modules/*
