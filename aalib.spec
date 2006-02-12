Summary:	An ASCII art GFX library
Summary(fr):	BibliothХque AA (Ascii Art)
Summary(es):	Biblioteca ASCII art
Summary(pl):	Biblioteka graficzna ASCII Art
Summary(pt_BR):	Uma biblioteca para ASCII art
Summary(ru):	Библиотека консольной графики (ASCII Art)
Summary(uk):	Б╕бл╕отека консольно╖ граф╕ки (ASCII Art)
Name:		aalib
Version:	1.4rc5
Release:	11
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}.tar.gz
# Source0-md5:	9801095c42bba12edebd1902bcf0a990
Source1:	%{name}-config.1
Patch0:		%{name}-info.patch
Patch1:		%{name}-debian_man.patch
Patch2:		%{name}-am18.patch
URL:		http://aa-project.sourceforge.net/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	libtool
BuildRequires:	slang-devel >= 2.0.0
BuildRequires:	texinfo
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
La bibliothХque AA est nИcessaire pour GIMP. Elle offre la possibilitИ
de travailler dans des contextes graphiques sans affichage.

%description -l pl
AA-lib jest niskopoziomow╠ bibliotek╠ graficzn╠ podobnie jak wiele
innych bibliotek. GЁСwna rС©nica pomiЙdzy nimi jest taka, ©e AA-lib
nie wymaga trybu graficznego. WЁa╤ciwie nie ma mo©liwo╤ci wy╤wietlenia
czego╤ w trybie graficznym. AA-lib zastЙpuje te staromodne metody
wysoko wydajnym narzЙdziem do renderowania ascii-art. Teraz mСj Linux
startuje z Ёadnym logo pingwina na drugim monitorze. AA-lib API jest
zaprojektowane tak by byФ podobnym do innych graficznych bibliotek.
Nauka nowego API bЙdzie buЁk╠ z masЁem!

%description -l pt_BR
Uma biblioteca para trabalhar com ASCII art.

%description -l ru
AA-lib - это низкоуровневая графическая библиотека. Ее основное
отличие от других графических библиотек в том, что AA-lib не требует
графического устройства. На самом деле, графический (в обычном смысле
этого слова) вывод и невозможен. AA-lib переводит графику в так
называемый ASCII-Art.

%description -l uk
AA-lib - це низькор╕внева граф╕чна б╕бл╕отека. Головна в╕дм╕нн╕сть ╖╖
в╕д ╕нших граф╕чних б╕бл╕отек в тому, о AA-lib не потребу╓ граф╕чного
пристрою. Насправд╕, граф╕чний (в звичному розум╕нн╕ цього слова)
вив╕д ╕ неможливий. AA-lib перетворю╓ граф╕ку в так званий ASCII-Art.

%package devel
Summary:	Header files and libraries for aalib
Summary(pl):	Pliki nagЁСwkowe dla aalib
Summary(ru):	Хедеры для построения программ с AAlib
Summary(uk):	Хедери для побудови програм з AAlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	gpm-devel
Requires:	slang-devel

%description devel
The header files for development of programs using the AAlib.

%description devel -l pl
Pliki nagЁСwkowe do pisania programСw u©ywaj╠cych AAlib.

%description devel -l ru
Хедеры для построения программ с AAlib.

%description devel -l uk
Хедери для побудови програм з AAlib.

%package static
Summary:	Static aalib library
Summary(pl):	Statyczna biblioteka aalib
Summary(ru):	Статическая библиотека для построения программ с aalib
Summary(uk):	Статична б╕бл╕отека для побудови програм з aalib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static aalib library.

%description static -l pl
Statyczna biblioteka aalib.

%description static -l ru
Статическая библиотека для программирования с aalib.

%description static -l uk
Статична б╕бл╕отека для програмування з aalib.

%package progs
Summary:	AA-lib tools
Summary(pl):	NarzЙdzia AA-lib
Summary(ru):	Утилиты для AA-lib
Summary(uk):	Утил╕ти для AA-lib
Group:		Applications/Terminal
Requires:	%{name} = %{version}-%{release}

%description progs
AA-lib tools.

%description progs -l pl
NarzЙdzia AA-lib.

%description progs -l ru
Утилиты для AA-lib.

%description progs -l uk
Утил╕ти для AA-lib.

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
%configure
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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aafire
%attr(755,root,root) %{_bindir}/aainfo
%attr(755,root,root) %{_bindir}/aasavefont
%attr(755,root,root) %{_bindir}/aatest
%{_mandir}/man1/aafire.1*
