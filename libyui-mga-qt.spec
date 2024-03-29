%define major 16
%define oldlibname %mklibname yui 15-mga-qt
%define libname %mklibname yui-mga-qt
%define develname %mklibname yui-mga-qt -d

Name:		libyui-mga-qt
Version:	1.2.0
Release:	3
Summary:	UI abstraction library - Qt plugin
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/manatools/libyui-mga-qt
Source0:	https://github.com/manatools/libyui-mga-qt/archive/%{name}-%{version}.tar.gz
Patch0:		fix-linking.patch

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui) >= 3.1.2
BuildRequires:	pkgconfig(libyui-mga)
BuildRequires:	pkgconfig(libyui-qt)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	boost-devel
BuildRequires:	doxygen
#BuildRequires:	texlive
BuildRequires:	graphviz
BuildRequires:	ghostscript
BuildRequires:	pkgconfig(fontconfig)
Requires:	libyui

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Requires:	%{_lib}qt5x11extras5
Provides:	%{name} = %{EVRD}
Provides:	libyui%{major}-mga-qt = %{EVRD}
%rename %{_lib}yui-mga8-qt
%rename %{oldlibname}

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-mga-qt.

%files -n %{libname}
%{_libdir}/yui/lib*.so.*

#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/KDE and Qt
Requires:	libyui-devel
Requires:	%{name} = %{EVRD}
Provides:	yui-mga-qt-devel = %{EVRD}

%description -n %{develname}
This package provides headers files for libyui-mga-qt development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/yui/lib*.so
#%{_libdir}/pkgconfig/libyui-mga-qt.pc
#%{_libdir}/cmake/libyui-mga-qt

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
#./bootstrap.sh
%cmake \
    -DYPREFIX=%{_prefix}  \
    -DDOC_DIR=%{_docdir} \
    -DLIB_DIR=%{_lib}    \
    -G Ninja

%ninja_build

%install
%ninja_install -C build
