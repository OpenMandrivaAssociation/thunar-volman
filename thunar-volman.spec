%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A removable volume manager for Thunar
Name:		thunar-volman
Version:	0.8.0
Release:	7
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(thunarx-2)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(exo-1)
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.11
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(libnotify)
Requires:	thunar >= 1.3.1
Requires:	dbus >= 0.34
Requires:	gvfs
%if %mdvver >= 201300
Suggests:	gvfs-archive
Suggests:	gvfs-fuse
Suggests:	gvfs-gphoto2
Suggests:	gvfs-iphone
Suggests:	gvfs-obexftp
Suggests:	gvfs-smb
Suggests:	gvfs-mtp
%endif
Obsoletes:	xfce4-volstatus-icon <= 0.1.0

%description
The Thunar Volume Manager is an extension for the Thunar
file manager, which enables automatic management of removable
drives and media. For example, if thunar-volman is installed
and configured properly, and you plug in your digital camera,
it will automatically launch your preferred photo application
and import the new pictures from the camera into your photo collection.

%prep
%setup -q

%build
%configure2_5x \
	--enable-notifications

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/applications/thunar-volman-settings.desktop

