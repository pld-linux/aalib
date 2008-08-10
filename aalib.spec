#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	An ASCII art GFX library
Summary(fr.UTF-8):	Bibliothèque AA (Ascii Art)
Summary(es.UTF-8):	Biblioteca ASCII art
Summary(pl.UTF-8):	Biblioteka graficzna ASCII Art
Summary(pt_BR.UTF-8):	Uma biblioteca para ASCII art
Summary(ru.UTF-8):	Библиотека консольной графики (ASCII Art)
Summary(uk.UTF-8):	Бібліотека консольної графіки (ASCII Art)
Name:		aalib
%define         _rc     rc5
%define         _rel    13
Version:	1.4
Release:	0.%{_rc}.%{_rel}
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	9801095c42bba12edebd1902bcf0a990
Source1:	%{name}-config.1
Patch0:		%{name}-info.patch
Patch1:		%{name}-debian_man.patch
Patch2:		%{name}-am18.patch
URL:		http://aa-project.sourceforge.net/aalib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	libtool
BuildRequires:	slang-devel >= 2.0.0
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device.
In fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!

%description -l fr.UTF-8
La bibliothèque AA est nécessaire pour GIMP. Elle offre la possibilité
de travailler dans des contextes graphiques sans affichage.

%description -l pl.UTF-8
AA-lib jest niskopoziomową biblioteką graficzną podobnie jak wiele
innych bibliotek. Główna różnica pomiędzy nimi jest taka, że AA-lib
nie wymaga trybu graficznego. Właściwie nie ma możliwości wyświetlenia
czegoś w trybie graficznym. AA-lib zastępuje te staromodne metody
wysoko wydajnym narzędziem do renderowania ascii-art. Teraz mój Linux
startuje z ładnym logo pingwina na drugim monitorze. AA-lib API jest
zaprojektowane tak by być podobnym do innych graficznych bibliotek.
Nauka nowego API będzie bułką z masłem!

%description -l pt_BR.UTF-8
Uma biblioteca para trabalhar com ASCII art.

%description -l ru.UTF-8
AA-lib - это низкоуровневая графическая библиотека. Ее основное
отличие от других графических библиотек в том, что AA-lib не требует
графического устройства. На самом деле, графический (в обычном смысле
этого слова) вывод и невозможен. AA-lib переводит графику в так
называемый ASCII-Art.

%description -l uk.UTF-8
AA-lib - це низькорівнева графічна бібліотека. Головна відмінність її
від інших графічних бібліотек в тому, о AA-lib не потребує графічного
пристрою. Насправді, графічний (в звичному розумінні цього слова)
вивід і неможливий. AA-lib перетворює графіку в так званий ASCII-Art.

%package devel
Summary:	Header files and libraries for aalib
Summary(pl.UTF-8):	Pliki nagłówkowe dla aalib
Summary(ru.UTF-8):	Хедеры для построения программ с AAlib
Summary(uk.UTF-8):	Хедери для побудови програм з AAlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gpm-devel
Requires:	slang-devel
Requires:	xorg-lib-libX11-devel

%description devel
The header files for development of programs using the AAlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe do pisania programów używających AAlib.

%description devel -l ru.UTF-8
Хедеры для построения программ с AAlib.

%description devel -l uk.UTF-8
Хедери для побудови програм з AAlib.

%package static
Summary:	Static aalib library
Summary(pl.UTF-8):	Statyczna biblioteka aalib
Summary(ru.UTF-8):	Статическая библиотека для построения программ с aalib
Summary(uk.UTF-8):	Статична бібліотека для побудови програм з aalib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static aalib library.

%description static -l pl.UTF-8
Statyczna biblioteka aalib.

%description static -l ru.UTF-8
Статическая библиотека для программирования с aalib.

%description static -l uk.UTF-8
Статична бібліотека для програмування з aalib.

%package progs
Summary:	AA-lib tools
Summary(pl.UTF-8):	Narzędzia AA-lib
Summary(ru.UTF-8):	Утилиты для AA-lib
Summary(uk.UTF-8):	Утиліти для AA-lib
Group:		Applications/Terminal
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
AA-lib tools.

%description progs -l pl.UTF-8
Narzędzia AA-lib.

%description progs -l ru.UTF-8
Утилиты для AA-lib.

%description progs -l uk.UTF-8
Утиліти для AA-lib.

%prep
%setup -q -n %{name}-1.4.0
%patch0 -p1
%patch1 -p1
%patch2 -p1

# don't include aclocal.m4 from configure.in
tail -n +2 configure.in > c.tmp
mv -f c.tmp configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/aalib-config.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ANNOUNCE ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aalib-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_infodir}/*.info*
%{_mandir}/man1/aalib-config.1*
%{_mandir}/man3/*
%{_aclocaldir}/*.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aafire
%attr(755,root,root) %{_bindir}/aainfo
%attr(755,root,root) %{_bindir}/aasavefont
%attr(755,root,root) %{_bindir}/aatest
%{_mandir}/man1/aafire.1*
