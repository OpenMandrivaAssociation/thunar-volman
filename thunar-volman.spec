%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	A removable volume manager for Thunar
Name:		thunar-volman
Version:	4.20.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	https://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(thunarx-3)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.20.0
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gudev-1.0)

Requires:	thunar >= 1.3.1
Requires:	dbus >= 0.34
Requires:	gvfs
Suggests:	gvfs-archive
Suggests:	gvfs-fuse
Suggests:	gvfs-gphoto2
Suggests:	gvfs-iphone
Suggests:	gvfs-obexftp
Suggests:	gvfs-smb
Suggests:	gvfs-mtp
Obsoletes:	xfce4-volstatus-icon <= 0.1.0

%description
The Thunar Volume Manager is an extension for the Thunar
file manager, which enables automatic management of removable
drives and media. For example, if thunar-volman is installed
and configured properly, and you plug in your digital camera,
it will automatically launch your preferred photo application
and import the new pictures from the camera into your photo collection.

%prep
%autosetup -p1

%build
%configure \
	--enable-notifications

%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README* THANKS
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/applications/thunar-volman-settings.desktop
