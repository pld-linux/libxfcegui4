# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Various GTK+ widgets for Xfce
Summary(pl):	R�ne widgety GTK+ dla Xfce
Name:		libxfcegui4
Version:	4.2.3
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	5d2bae78c5ef66e914ae7a930bbdeb57
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbh-devel >= 1.0
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc-automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	xfce4-dev-tools
Requires:	gtk+2 >= 2:2.6.0
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
Requires:	gtk+2-devel >= 2:2.6.0
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
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-xinerama \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# modules loaded through gmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/modules/*.{la,a}

# assume bn==bn_IN as no translation for bn_BD appeared till now
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/bn{_IN,}

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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
