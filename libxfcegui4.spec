#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Various GTK+ widgets for Xfce
Summary(pl.UTF-8):	Różne widgety GTK+ dla Xfce
Name:		libxfcegui4
Version:	4.6.0
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8627ae4fad26289f55f0afbebe238bf5
URL:		http://www.xfce.org/projects/libraries/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgladeui-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various GTK+ widgets for Xfce.

%description -l pl.UTF-8
Różne widgety GTK+ dla Xfce.

%package apidocs
Summary:	libxfcegui4 API documentation
Summary(pl.UTF-8):	Dokumentacja API libxfcegui4
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libxfcegui4 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxfcegui4.

%package devel
Summary:	Development files for libxfcegui4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxfcegui4
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.6
Requires:	libxfce4util-devel >= %{version}
Requires:	startup-notification-devel >= 0.8
Requires:	xfconf-devel >= %{version}
Requires:	xorg-lib-libSM-devel

%description devel
Development files for the libxfcegui4 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxfcegui4.

%package static
Summary:	Static libxfcegui4 library
Summary(pl.UTF-8):	Statyczna biblioteka libxfcegui4
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxfcegui4 library.

%description static -l pl.UTF-8
Statyczna biblioteka libxfcegui4.

%package -n glade3-libxfcegui4
Summary:	libxfcegui4 support for Glade 3
Summary(pl.UTF-8):	Wsparcie dla libxfcegui4 w Glade 3
Group:		Development/Building
Requires:	glade3

%description -n glade3-libxfcegui4
libxfcegui4 support for Glade 3.

%description -n glade3-libxfcegui4 -l pl.UTF-8
Wsparcie dla libxfcegui4 w Glade 3.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# assume bn==bn_IN as no translation for bn_BD appeared till now
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/bn{_IN,}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade3/modules/libgladexfce4.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/libxfce4.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxfce4kbd-private.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfce4kbd-private.so.5
%attr(755,root,root) %{_libdir}/libxfcegui4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfcegui4.so.4
%attr(755,root,root) %{_libdir}/libglade/2.0/libxfce4.so
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfce4kbd-private.so
%attr(755,root,root) %{_libdir}/libxfcegui4.so
%{_libdir}/libxfce4kbd-private.la
%{_libdir}/libxfcegui4.la
%{_includedir}/xfce4/libxfce4kbd-private
%{_includedir}/xfce4/libxfcegui4
%{_pkgconfigdir}/libxfce4kbd-private-1.0.pc
%{_pkgconfigdir}/libxfcegui4-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfce4kbd-private.a
%{_libdir}/libxfcegui4.a
%endif

%files -n glade3-libxfcegui4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade3/modules/libgladexfce4.so
%{_datadir}/glade3/catalogs/xfce4.xml
%{_datadir}/glade3/catalogs/xfce4.xml.in
%{_datadir}/glade3/pixmaps/*/*/*/*.png
