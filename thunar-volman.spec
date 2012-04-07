%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A removable volume manager for Thunar
Name:		thunar-volman
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel >= 1.3.1
BuildRequires:	dbus-devel >= 0.34
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	exo-devel >= 0.7.2
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	xfconf-devel >= 4.7.0
BuildRequires:	libnotify-devel >= 0.4.0
Requires:	thunar >= 1.3.1
Requires:	dbus >= 0.34
Requires:	gvfs
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

# add onlyshowin=xfce in the .desktop file:
desktop-file-install --vendor="" \
		--remove-key="Encoding" \
		--add-only-show-in="XFCE" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/thunar-volman-settings.desktop


%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/applications/thunar-volman-settings.desktop
