Summary:	Go board game frontend for GNOME
Summary(pl.UTF-8):	Interfejs GNOME do gry planszowej go
Name:		gnomego
Version:	0.5.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gnomego/%{name}-%{version}.tar.gz
# Source0-md5:	5a318f5cd17f758c4307fc33c57fc0ad
URL:		http://gnomego.sourceforge.net/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	gnugo > 3.6
Requires:	python-gnome-gconf
Requires:	python-pyparsing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Go is an ancient East Asian board game nowadays played all over the
world. GnomeGo aims to bring all software a Go player can think of to
the GNOME desktop.

%description -l pl.UTF-8
Go to stara wschodnioazjatycka gra planszowa obecnie rozgrywana na
całym świecie. Celem GnomeGo jest przeniesienie całego oprogramowania
dla graczy w go do środowiska GNOME.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/gnomego
%attr(755,root,root) %{_bindir}/sgf-info
%attr(755,root,root) %{_bindir}/sgf-thumbnailer
%attr(755,root,root) %{_libdir}/gnome-screensaver/sgf-screensaver
%{_desktopdir}/gnomego.desktop
%{_desktopdir}/screensavers/sgf-screensaver.desktop
#%{_datadir}/gconf/schemas/sgf-thumbnailer.schemas
%dir %{_datadir}/gnomego
%{_datadir}/gnomego/*.svg
%{_datadir}/gnomego/*.png
%{_datadir}/gnomego/*.glade
%dir %{_datadir}/gnomego/sgfs
%{_datadir}/gnomego/sgfs/games.zip
%{_datadir}/mime/packages/gnomego.xml
%{_pixmapsdir}/gnomego_64x64.png
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/gnomego-*.egg-info
%endif
%dir %{py_sitescriptdir}/gnomego
%{py_sitescriptdir}/gnomego/*.py[co]
