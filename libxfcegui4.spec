#
%define		snap 20040616
#
Summary:	Various gtk widgets for XFce
Summary(pl):	Ró¿ne widgety gtk dla XFce
Name:		libxfcegui4
Version:	4.1.0
Release:	0.%{snap}.1
License:	LGPL
Group:		Libraries
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	e4f17ff2dbf17f905f5a0e998156d80c
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
Requires:	gtk+2 >= 2.0.6
Requires:	libxfce4util >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various gtk widgets for XFce.

%description -l pl
Ró¿ne widgety gtk dla XFce.

%package devel
Summary:	Development files for libxfcegui4 library
Summary(pl):	Pliki nag³ówkowe biblioteki libxfcegui4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0.6
Requires:	libxfce4util-devel >= %{version}

%description devel
Development files for the libxfcegui4 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libxfcegui4.

%package static
Summary:	Static libxfce4util library
Summary(pl):	Statyczna biblioteka libxfce4util
Group:		Development/Libriaries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4util library.

%description static -l pl
Statyczna biblioteka libxfce4util.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xfce4/libxfcegui4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
