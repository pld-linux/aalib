Summary:     An ASCII art GFX library
Summary(pl): Biblioteka GFX sztuki w ASCII
Name:        aalib
Version:     1.2
Release:     7
Copyright:   LGPL
Group:       Libraries
Group(pl):   Biblioteki
Source:      ftp://ftp.ta.jcu.cz/pub/aa/%{name}-%{version}.tar.gz
Patch0:      aalib-xref.patch
Patch1:      aalib-info.patch
URL:         http://horac.ta.jcu.cz/aa/aalib/
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
Summary:     Header files libraries for aalib
Summary(pl): Pliki nag³ówkowe dla aalib
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name} = %{version}
Prereq:      /sbin/install-info

%description devel
The header files for development of programs using the AAlib.

%description -l pl devel
Pliki nag³ówkowe do pisania programów u¿ywaj±cych AAlib.

%package static
Summary:     Static aalib library
Summary(pl): Statyczna biblioteka aalib
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name}-devel = %{version}

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

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=/usr 
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*}

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
* Mon Apr  5 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.2-7]
- added Group(pl),
- fixed info entry (aalib-info.patch), 
- fixed @xref definitions in aalib.texinfo (aalib-xref.patch),
- standarized {un}registering info pages,
- added gzipping documentation,
- added ChangeLog to %doc,
- cosmetic changes for common l&f.

* Sat Sep 26 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.2-6]
- added pl translation.

* Fri Aug 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-5]
- corected dependences in static "Requires: %%{name}-devel = %%{version}",
- removed "Prereq: /sbin/install-info" from static,
- aalib is now builded against libslang.so.1.

* Thu Jun 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-5]
- recompiled on system without ncurses (only slang).
- added static subpackage,
- all %doc moved to devel.

* Mon Jun  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-4]
- added -q %setup parameter,
- built against ncurses 4.2 (for RH 5.1).

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-3]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added using %%{name} macro in Buildroot and Source field,
- added -q %setup parameter.

* Thu Apr 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-2]
- spec file rewrited for using Buildroot,
- info pages moved to devel,
- added "Requires: aalib = %%{PACKAGE_VERSION}" for devel header,
- added %clean section,
- added URL,
- added stripping programs and AA shared library,
- added usung $RPM_OPT_FLAGS in CFLAGS during compiling, 
- Copyright satment changed to LGPL,
- removed COPYING from %doc (Copyright satment is in header),
- addec "Prereq: /sbin/install-info" for devel subpackage",
- added %%{version} to Source url,
- added %defattr and %attr macros in %files (allows building package from
  non-root account); %defattr requires rpm >= 2.4.99.

* Sun Mar  8 1998 ??? <root@pentium.home.cz>
  [1.2-1]
- first release in rpm packages.
