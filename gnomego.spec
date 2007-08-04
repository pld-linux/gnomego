#
Summary:	Go board game frontend for Gnome
Name:		gnomego
Version:	0.5.1
Release:	1
License:	GPLv2
Group:		Applications
Source0:	http://dl.sourceforge.net/gnomego/%{name}-%{version}.tar.gz
# Source0-md5:	5a318f5cd17f758c4307fc33c57fc0ad
URL:		http://gnomego.sourceforge.net/
BuildArch: noarch
Requires:	python-gnome-gconf
Requires:	python-pyparsing
Requires: gnugo > 3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Go is an ancient east asian board game nowadays played all over the
world. GnomeGo aims to bring all software a go player can think of to
the gnome desktop.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%find_lang gnomego --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS  TODO README
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
%{py_sitescriptdir}/gnomego-0.5.1-py2.5.egg-info
%dir %{py_sitescriptdir}/gnomego
%{py_sitescriptdir}/gnomego/*.py[co]
