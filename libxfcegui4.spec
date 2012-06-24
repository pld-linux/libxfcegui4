Summary:	Various GTK+ widgets for Xfce
Summary(pl):	R�ne widgety GTK+ dla Xfce
Name:		libxfcegui4
Version:	4.1.99.3
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	802e5b50887f6a34ac82cc734d136366
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	dbh-devel >= 1.0
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libxml2-devel >= 2.4.0
Requires:	libxfce4util >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various GTK+ widgets for Xfce.

%description -l pl
R�ne widgety GTK+ dla Xfce.

%package devel
Summary:	Development files for libxfcegui4 library
Summary(pl):	Pliki nag��wkowe biblioteki libxfcegui4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 1:2.2.0
Requires:	gtk-doc-common
Requires:	libxfce4util-devel >= %{version}
Requires:	startup-notification-devel >= 0.5

%description devel
Development files for the libxfcegui4 library.

%description devel -l pl
Pliki nag��wkowe biblioteki libxfcegui4.

%package static
Summary:	Static libxfce4util library
Summary(pl):	Statyczna biblioteka libxfce4util
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfce4util library.

%description static -l pl
Statyczna biblioteka libxfce4util.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-xinerama \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# modules loaded through gmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/modules/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/xfce4
%dir %{_libdir}/xfce4/modules
# why -avoid-version only on Cygwin?
%attr(755,root,root) %{_libdir}/xfce4/modules/lib*.so*
%{_datadir}/xfce4/mime
%{_datadir}/xfce4/hicolor-index.theme
%{_datadir}/xfce4/xfce-svg-test.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xfce4/libxfcegui4
%{_includedir}/xfce4/xfce4-modules
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/libxfcegui4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
