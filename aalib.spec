Summary:	An ASCII art GFX library
Summary(fr):	Bibliothèque AA (Ascii Art)
Summary(es):	Biblioteca ASCII art
Summary(pl):	Biblioteka graficzna ASCII Art
Summary(pt_BR):	Uma biblioteca para ASCII art
Summary(ru):	âÉÂÌÉÏÔÅËÁ ËÏÎÓÏÌØÎÏÊ ÇÒÁÆÉËÉ (ASCII Art)
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ ËÏÎÓÏÌØÎÏ§ ÇÒÁÆ¦ËÉ (ASCII Art)
Name:		aalib
Version:	1.4rc5
Release:	5
License:	LGPL
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Aðgerðasöfn
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sl):	Knji¾nice
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
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

%description -l es
Biblioteca ASCII art.

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

%description -l pt_BR
Uma biblioteca para trabalhar com ASCII art.

%description -l ru
AA-lib - ÜÔÏ ÎÉÚËÏÕÒÏ×ÎÅ×ÁÑ ÇÒÁÆÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ. åÅ ÏÓÎÏ×ÎÏÅ
ÏÔÌÉÞÉÅ ÏÔ ÄÒÕÇÉÈ ÇÒÁÆÉÞÅÓËÉÈ ÂÉÂÌÉÏÔÅË × ÔÏÍ, ÞÔÏ AA-lib ÎÅ ÔÒÅÂÕÅÔ
ÇÒÁÆÉÞÅÓËÏÇÏ ÕÓÔÒÏÊÓÔ×Á. îÁ ÓÁÍÏÍ ÄÅÌÅ, ÇÒÁÆÉÞÅÓËÉÊ (× ÏÂÙÞÎÏÍ ÓÍÙÓÌÅ
ÜÔÏÇÏ ÓÌÏ×Á) ×Ù×ÏÄ É ÎÅ×ÏÚÍÏÖÅÎ. AA-lib ÐÅÒÅ×ÏÄÉÔ ÇÒÁÆÉËÕ × ÔÁË
ÎÁÚÙ×ÁÅÍÙÊ ASCII-Art.

%description -l uk
AA-lib - ÃÅ ÎÉÚØËÏÒ¦×ÎÅ×Á ÇÒÁÆ¦ÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ. çÏÌÏ×ÎÁ ×¦ÄÍ¦ÎÎ¦ÓÔØ §§
×¦Ä ¦ÎÛÉÈ ÇÒÁÆ¦ÞÎÉÈ Â¦ÂÌ¦ÏÔÅË × ÔÏÍÕ, Ï AA-lib ÎÅ ÐÏÔÒÅÂÕ¤ ÇÒÁÆ¦ÞÎÏÇÏ
ÐÒÉÓÔÒÏÀ. îÁÓÐÒÁ×Ä¦, ÇÒÁÆ¦ÞÎÉÊ (× Ú×ÉÞÎÏÍÕ ÒÏÚÕÍ¦ÎÎ¦ ÃØÏÇÏ ÓÌÏ×Á)
×É×¦Ä ¦ ÎÅÍÏÖÌÉ×ÉÊ. AA-lib ÐÅÒÅÔ×ÏÒÀ¤ ÇÒÁÆ¦ËÕ × ÔÁË Ú×ÁÎÉÊ ASCII-Art.


%package devel
Summary:	Header files and libraries for aalib
Summary(pl):	Pliki nag³ówkowe dla aalib
Summary(ru):	èÅÄÅÒÙ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÒÏÇÒÁÍÍ Ó AAlib
Summary(uk):	èÅÄÅÒÉ ÄÌÑ ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ Ú AAlib
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Aðgerðasöfn
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sl):	Knji¾nice
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	slang-devel
Requires:	gpm-devel
Requires:	XFree86-devel

%description devel
The header files for development of programs using the AAlib.

%description devel -l pl
Pliki nag³ówkowe do pisania programów u¿ywaj±cych AAlib.

%description devel -l ru
èÅÄÅÒÙ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÒÏÇÒÁÍÍ Ó AAlib.

%description devel -l uk
èÅÄÅÒÉ ÄÌÑ ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ Ú AAlib.

%package static
Summary:	Static aalib library
Summary(pl):	Statyczna biblioteka aalib
Summary(ru):	óÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ ÐÒÏÇÒÁÍÍ Ó aalib
Summary(uk):	óÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ Ú aalib
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Aðgerðasöfn
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sl):	Knji¾nice
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static aalib library.

%description static -l pl
Statyczna biblioteka aalib.

%description static -l ru
óÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó aalib.

%description static -l uk
óÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú aalib.

%package progs
Summary:	AA-lib tools
Summary(pl):	Narzêdzia AA-lib
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ AA-lib
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ AA-lib
Group:		Applications/Terminal
Group(cs):	Aplikace/Terminál
Group(da):	Programmer/Terminal
Group(de):	Applikationen/Terminal
Group(es):	Aplicaciones/Terminal
Group(fr):	Applications/Terminal
Group(is):	Forrit/Textaskilum
Group(it):	Applicazioni/Terminale
Group(no):	Applikasjoner/Terminal
Group(pl):	Aplikacje/Terminal
Group(pt):	Aplicações/Terminal
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/ôÅÒÍÉÎÁÌ
Group(sl):	Programi/Terminal
Group(sv):	Tillämpningar/Terminal
Group(uk):	ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ/ôÅÒÍ¦ÎÁÌÉ
Requires:	%{name} = %{version}

%description progs
AA-lib tools.

%description progs -l pl
Narzêdzia AA-lib.

%description progs -l ru
õÔÉÌÉÔÙ ÄÌÑ AA-lib.

%description progs -l uk
õÔÉÌ¦ÔÉ ÄÌÑ AA-lib.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
