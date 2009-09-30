Name: twitter-glib
Summary: Twitter library
Group: Development/Libraries
Version: 0.9.8
License: LGPLv2.1
URL: http://live.gnome.org/TwitterGlib
Release: %mkrel 1
Source0: twitter-glib-%{version}git20090728.tar.gz
Patch0: twitter-glib-0.9.8git20090728-fix-asif.patch
Patch1: twitter-glib-0.9.8git20090728-timegm.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libglib2.0-devel
BuildRequires: moblin-json-glib-devel
BuildRequires: libsoup-2.4-devel
BuildRequires: libgdk_pixbuf2.0_0-devel
BuildRequires: gtk-doc

Requires: moblin-json-glib

%description
Twitter-GLib uses LibSoup to access the RESTful API exposed by Twitter, and JSON-GLib to parse the JSON data streams returned by Twitter. 

%package devel

Summary: Development libraries and headers for twitter-glib
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel
Requires: moblin-json-glib-devel
Requires: %{name} >= %{version}

%description devel
Development environment for twitter-glib

%package doc

Summary: Documentation for twitter-glib
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}
Requires: gtk-doc
Requires: %{name} >= %{version}

%description doc
Documentation for twitter-glib

%prep
%setup -q -n twitter-glib-0.9.8git20090728
%patch0 -p0
%patch1 -p0

%build
./autogen.sh --prefix=/usr --enable-gtk-doc
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
  if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
    mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
  fi
done

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%exclude %{_libdir}/*.la
%{_libdir}/libtwitter-glib-1.0.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libtwitter-glib-1.0.so
%{_libdir}/pkgconfig/twitter-glib-1.0.pc
%{_includedir}/twitter-glib-1.0/*
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/*

%files doc
%{_datadir}/gtk-doc/html/*
