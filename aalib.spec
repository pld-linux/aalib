Summary:     An ASCII art GFX library
Summary(pl): Biblioteka GFX sztuki w ASCII
Name:        aalib
Version:     1.2
Release:     6
Copyright:   LGPL
Group:       Libraries
Source:      ftp://ftp.ta.jcu.cz/pub/aa/%{name}-%{version}.tar.gz
URL:         http://horac.ta.jcu.cz/aa/aalib/
Buildroot:   /tmp/%{name}-%{version}-root

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
G³ówna ró¿nica pomiêdzi nimi jest taka, ¿e AA-lib nie wymaga trybu graficznego.
W³a¶ciwie nie ma mo¿liwo¶ci wy¶wietlenia czego¶ w trybie graficznym. AA-lib
zastêpuje te staromodne metody wysoko wydajnym narzêdziem do renderowania
asci-art. Teraz mój linux startuje z ³adnym logo pingwina na drugim monitorze.
AA-lib API jest zaprojektowane tak by byæ podobnym do innych graficznych
bibliotek. Nauka nowego API bêdzie bu³k± z mas³em!

%package devel
Summary:     Header files libraries for aalib
Summary(pl): Pliki nag³ówkowe dla aalib
Group:       Libraries
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
Requires:    %{name}-devel = %{version}

%description static
Static aalib library.

%description -l pl static
Statyczna biblioteka aalib

%package progs
Summary:     AA-lib tools
Summary(pl): Narzêdzia AA-lib
Requires:    %{name} = %{version}
Group:       Utilities/Terminal

%description progs
AA-lib tools.

%description -l pl progs
Narzêdzia AA-lib.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
gzip -9fn $RPM_BUILD_ROOT/usr/info/*.info

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info --info-dir=/usr/info /usr/info/aalib.info.gz

%preun devel
/sbin/install-info --delete --info-dir=/usr/info /usr/info/aalib.info.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc README NEWS AUTHORS ANNOUNCE
/usr/include/*.h
/usr/lib/lib*.so
/usr/info/*.info.gz

%files static
%attr(644, root, root) /usr/lib/lib*.a

%files progs
%attr(755, root, root) /usr/bin/*

%changelog
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
