Summary:	An ASCII art GFX library
Summary(fr):	Biblioth�que AA (Ascii Art)
Summary(es):	Biblioteca ASCII art
Summary(pl):	Biblioteka graficzna ASCII Art
Summary(pt_BR):	Uma biblioteca para ASCII art
Summary(ru):	���������� ���������� ������� (ASCII Art)
Summary(uk):	��̦����� ��������ϧ ���Ʀ�� (ASCII Art)
Name:		aalib
Version:	1.4rc5
Release:	5
License:	LGPL
Group:		Libraries
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
La biblioth�que AA est n�cessaire pour GIMP. Elle offre la possibilit�
de travailler dans des contextes graphiques sans affichage.

%description -l pl
AA-lib jest niskopoziomow� bibliotek� graficzn� podobnie jak wiele
innych bibliotek. G��wna r�nica pomi�dzy nimi jest taka, �e AA-lib
nie wymaga trybu graficznego. W�a�ciwie nie ma mo�liwo�ci wy�wietlenia
czego� w trybie graficznym. AA-lib zast�puje te staromodne metody
wysoko wydajnym narz�dziem do renderowania ascii-art. Teraz m�j Linux
startuje z �adnym logo pingwina na drugim monitorze. AA-lib API jest
zaprojektowane tak by by� podobnym do innych graficznych bibliotek.
Nauka nowego API b�dzie bu�k� z mas�em!

%description -l pt_BR
Uma biblioteca para trabalhar com ASCII art.

%description -l ru
AA-lib - ��� �������������� ����������� ����������. �� ��������
������� �� ������ ����������� ��������� � ���, ��� AA-lib �� �������
������������ ����������. �� ����� ����, ����������� (� ������� ������
����� �����) ����� � ����������. AA-lib ��������� ������� � ���
���������� ASCII-Art.

%description -l uk
AA-lib - �� ������Ҧ����� ���Ʀ��� ¦�̦�����. ������� צ�ͦ�Φ��� ��
צ� ����� ���Ʀ���� ¦�̦���� � ����, � AA-lib �� ������դ ���Ʀ�����
��������. �������Ħ, ���Ʀ���� (� �������� ����ͦ�Φ ����� �����)
��צ� � ����������. AA-lib ���������� ���Ʀ�� � ��� ������ ASCII-Art.


%package devel
Summary:	Header files and libraries for aalib
Summary(pl):	Pliki nag��wkowe dla aalib
Summary(ru):	������ ��� ���������� �������� � AAlib
Summary(uk):	������ ��� �������� ������� � AAlib
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	slang-devel
Requires:	gpm-devel
Requires:	XFree86-devel

%description devel
The header files for development of programs using the AAlib.

%description devel -l pl
Pliki nag��wkowe do pisania program�w u�ywaj�cych AAlib.

%description devel -l ru
������ ��� ���������� �������� � AAlib.

%description devel -l uk
������ ��� �������� ������� � AAlib.

%package static
Summary:	Static aalib library
Summary(pl):	Statyczna biblioteka aalib
Summary(ru):	����������� ���������� ��� ���������� �������� � aalib
Summary(uk):	�������� ¦�̦����� ��� �������� ������� � aalib
Group:		Libraries
Requires:	%{name}-devel = %{version}

%description static
Static aalib library.

%description static -l pl
Statyczna biblioteka aalib.

%description static -l ru
����������� ���������� ��� ���������������� � aalib.

%description static -l uk
�������� ¦�̦����� ��� ������������� � aalib.

%package progs
Summary:	AA-lib tools
Summary(pl):	Narz�dzia AA-lib
Summary(ru):	������� ��� AA-lib
Summary(uk):	���̦�� ��� AA-lib
Group:		Applications/Terminal
Requires:	%{name} = %{version}

%description progs
AA-lib tools.

%description progs -l pl
Narz�dzia AA-lib.

%description progs -l ru
������� ��� AA-lib.

%description progs -l uk
���̦�� ��� AA-lib.

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
