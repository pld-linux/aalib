Summary:	An ASCII art GFX library
Summary(pl):	Biblioteka GFX sztuki w ASCII
Name:		aalib
Version:	1.2
Release:	9
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.ta.jcu.cz/pub/aa/%{name}-%{version}.tar.gz
Patch0:		aalib-xref.patch
Patch1:		aalib-info.patch
Patch2:		aalib-autoconf.patch
URL:		http://horac.ta.jcu.cz/aa/aalib/
BuildPrereq:	gpm-devel
BuildPrereq:	slang-devel
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!

%description -l pl
AA-lib jest niskopoziomow± bibliotek± gfx podobnie jak wiele innych bibliotek.
G³ówna ró¿nica pomiêdzy nimi jest taka, ¿e AA-lib nie wymaga trybu graficznego.
W³a¶ciwie nie ma mo¿liwo¶ci wy¶wietlenia czego¶ w trybie graficznym. AA-lib
zastêpuje te staromodne metody wysoko wydajnym narzêdziem do renderowania
ascii-art. Teraz mój linux startuje z ³adnym logo pingwina na drugim monitorze.
AA-lib API jest zaprojektowane tak by byæ podobnym do innych graficznych
bibliotek. Nauka nowego API bêdzie bu³k± z mas³em!

%package devel
Summary:	Header files libraries for aalib
Summary(pl):	Pliki nag³ówkowe dla aalib
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}
Prereq:		/sbin/install-info

%description devel
The header files for development of programs using the AAlib.

%description -l pl devel
Pliki nag³ówkowe do pisania programów u¿ywaj±cych AAlib.

%package static
Summary:	Static aalib library
Summary(pl):	Statyczna biblioteka aalib
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static aalib library.

%description -l pl static
Statyczna biblioteka aalib.

%package progs
Summary:     AA-lib tools
Summary(pl): Narzêdzia AA-lib
Group:       Utilities/Terminal
Group(pl):   Narzêdzia/Terminal
Requires:    %{name} = %{version}

%description progs
AA-lib tools.

%description -l pl progs
Narzêdzia AA-lib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
LDFLAGS="-s"; export LDFLAGS
automake
autoconf
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info \
	README NEWS AUTHORS ANNOUNCE ChangeLog

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/aalib.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/aalib.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {README,NEWS,AUTHORS,ANNOUNCE,ChangeLog}.gz
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_infodir}/*.info.gz

%files static
%attr(644,root,root) %{_libdir}/lib*.a

%files progs
%attr(755,root,root) %{_bindir}/*

%changelog
* Wed Jun 30 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-9]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
