Summary:   An ASCII art GFX library
Name:      aalib
Version:   1.2
Release:   5
Copyright: LGPL
Group:     Libraries
Source:    ftp://ftp.ta.jcu.cz/pub/aa/%{name}-%{version}.tar.gz
URL:       http://horac.ta.jcu.cz/aa/aalib/
Buildroot: /tmp/%{name}-%{version}-root

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!

%package   devel
Summary:   header files libraries for aalib
Group:     Libraries
Requires:  aalib = %{version}
Prereq:    /sbin/install-info

%description devel
The header files for development of programs using the AAlib.

%package   static
Summary:   Static aalib library
Group:     Libraries
Requires:  aalib = %{version}
Prereq:    /sbin/install-info

%description static
Static aalib library.

%package   progs
Summary:   AA-lib tools
Requires:  aalib = %{version}
Group:     Utilities/Terminal

%description progs
AA-lib tools

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
* Thu Jun 18 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-5]
- recompiled on system without ncurses (only slang).
- added static subpackage,
- all %doc moved to devel.

* Mon Jun  1 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-4]
- added -q %setup parameter,
- built against ncurses 4.2 (for RH 5.1).

* Wed May  6 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-3]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added using %%{name} macro in Buildroot and Source field,
- added -q %setup parameter.

* Thu Apr 21 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [1.2-2]
- spec file rewrited for using Buildroot,
- info pages moved to devel,
- added "Requires: aalib = %%{PACKAGE_VERSION}" for devel header,
- added %clean section,
- added URL,
- added striping programs and AA shared library,
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
