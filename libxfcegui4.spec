Summary:	Various gtk widgets for XFce
Summary(pl):	Ró¿ne widgety gtk dla XFce
Name:		libxfcegui4
Version:	4.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	2d8ae6735a06c0ba2ffc3572e0aca707
URL:		http://www.xfce.org/
BuildRequires:	gtk+2-devel >= 2.0.6
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
Requires:	%{name} = %{version}
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
Requires:	%{name}-devel = %{version}

%description static
Static libxfce4util library.

%description static -l pl
Statyczna biblioteka libxfce4util.

%prep
%setup -q

%build
%configure \
	--enable-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
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
