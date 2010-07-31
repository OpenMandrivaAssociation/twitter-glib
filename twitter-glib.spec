%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name: twitter-glib
Summary: Twitter library
Group: System/Libraries
Version: 0.9.8
License: LGPLv2.1
URL: http://live.gnome.org/TwitterGlib
Release: %mkrel 5
Source0: twitter-glib-%{version}git20090728.tar.gz
Patch0: twitter-glib-0.9.8git20090728-fix-asif.patch
Patch1: twitter-glib-0.9.8git20090728-timegm.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libglib2.0-devel
BuildRequires: libjson-glib-devel
BuildRequires: libsoup-2.4-devel
BuildRequires: libgdk_pixbuf2.0-devel
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel

%description
Twitter-GLib uses LibSoup to access the RESTful API exposed by
Twitter, and JSON-GLib to parse the JSON data streams returned by
Twitter.

%package -n %{libname}
Summary: Twitter libraries
Group: System/Libraries

%description -n %{libname}
Twitter-GLib uses LibSoup to access the RESTful API exposed by
Twitter, and JSON-GLib to parse the JSON data streams returned by
Twitter.

%package -n %{develname}
Summary: Development libraries and headers for twitter-glib
Group: Development/C

Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel

%description -n %{develname}
Development environment for twitter-glib

%package doc

Summary: Documentation for twitter-glib
Group: Development/Other

Requires: %{libname} = %{version}-%{release}
Requires: gtk-doc

%description doc
Documentation for twitter-glib

%prep
%setup -q -n twitter-glib-0.9.8git20090728
%patch0 -p0
%patch1 -p0
perl -pi -e 's,^./configure.*,,' ./autogen.sh

%build
./autogen.sh
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
  if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
    mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
  fi
done

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%exclude %{_libdir}/*.la
%{_libdir}/libtwitter-glib-1.0.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/libtwitter-glib-1.0.so
%{_libdir}/pkgconfig/twitter-glib-1.0.pc
%{_includedir}/twitter-glib-1.0/*
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/*

%files doc
%{_datadir}/gtk-doc/html/*
