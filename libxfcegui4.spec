Summary: 	Various gtk widgets for xfce
Name: 		libxfcegui4
Version: 	3.90.0
Release: 	0.1
License:	LGPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	c20b716bddf559792360a3c4107218f7
Group: 		Development/Libraries
Requires:	gtk+2 >= 2.0.6
Requires:	libxfce4util >= 3.90.0
BuildRequires: 	gtk+2-devel >= 2.0.6
BuildRequires:	libxfce4util-devel >= 3.90.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various gtk widgets for xfce.

%package devel
Summary:	Developpment tools for libxfcegui4 library
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for the libxfcegui4 library.

%package static
Summary:	Static libraries for libxfce4util
Group:		Development/Libriaries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for libxfce4util.


%prep
%setup -q

%build
%configure \
	--enable-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/libxfcegui4

%files static
%defattr(644,root,root,755)
%{_libdir}/*a
