Summary:	An ASCII art GFX library
Summary(fr):	Bibliothèque AA (Ascii Art)
Summary(pl):	Biblioteka graficzna ASCII Art
Name:		aalib
Version:	1.4rc5
Release:	2
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/aa-project/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://aa-project.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	libtool
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device.
In fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!

%description -l fr
La bibliothèque AA est nécessaire pour GIMP. Elle offre la possibilité
de travailler dans des contextes graphiques sans affichage.

%description -l pl
AA-lib jest niskopoziomow± bibliotek± graficzn± podobnie jak wiele
innych bibliotek. G³ówna ró¿nica pomiêdzy nimi jest taka, ¿e AA-lib
nie wymaga trybu graficznego. W³a¶ciwie nie ma mo¿liwo¶ci wy¶wietlenia
czego¶ w trybie graficznym. AA-lib zastêpuje te staromodne metody
wysoko wydajnym narzêdziem do renderowania ascii-art. Teraz mój Linux
startuje z ³adnym logo pingwina na drugim monitorze. AA-lib API jest
zaprojektowane tak by byæ podobnym do innych graficznych bibliotek.
Nauka nowego API bêdzie bu³k± z mas³em!

%package devel
Summary:	Header files libraries for aalib
Summary(pl):	Pliki nag³ówkowe dla aalib
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
The header files for development of programs using the AAlib.

%description -l pl devel
Pliki nag³ówkowe do pisania programów u¿ywaj±cych AAlib.

%package static
Summary:	Static aalib library
Summary(pl):	Statyczna biblioteka aalib
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static aalib library.

%description -l pl static
Statyczna biblioteka aalib.

%package progs
Summary:	AA-lib tools
Summary(pl):	Narzêdzia AA-lib
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Requires:	%{name} = %{version}

%description progs
AA-lib tools.

%description -l pl progs
Narzêdzia AA-lib.

%prep
%setup -q -n %{name}-1.4.0
%patch0 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS AUTHORS ANNOUNCE ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/aalib-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h
%{_infodir}/*.info*
%{_mandir}/man3/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aafire
%attr(755,root,root) %{_bindir}/aainfo
%attr(755,root,root) %{_bindir}/aasavefont
%attr(755,root,root) %{_bindir}/aatest
%{_mandir}/man1/*
