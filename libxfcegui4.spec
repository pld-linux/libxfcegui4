Summary:	Various gtk widgets for XFce
Summary(pl):	Ró¿ne widgety gtk dla XFce
Name:		libxfcegui4
Version:	4.1.26
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://lo1sanok.eu.org/~troll/PLD/xfce4/%{name}-%{version}.tar.bz2
# Source0-md5:	42401e82800f06695d7e99653383b4b7
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= 4.1.11
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	startup-notification-devel >= 0.5
Requires:	gtk+2 >= 2.0.6
Requires:	libxfce4util >= 4.1.11
Requires:	startup-notification >= 0.5
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
Requires:	libxfce4util-devel >= 4.1.11
Requires:	startup-notification-devel >= 0.5

%description devel
Development files for the libxfcegui4 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libxfcegui4.

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
# Workaround for nonexistant xfce4-modules which is going to appear (sometime)
mkdir -p xfce4-modules/{mime{,-icons,-applications},headers,combo}
for i in xfce4-modules/{,mime{,-icons,-applications},headers,combo}/Makefile.in
do
    cat << EOF > $i
all:
install:
EOF
done

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
