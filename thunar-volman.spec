%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A removable volume manager for Thunar
Name:		thunar-volman
Version:	0.5.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel >= 1.1.2
BuildRequires:	dbus-devel >= 0.34
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	libusb-devel
BuildRequires:	libgudev-devel
BuildRequires:	exo-devel >= 0.5.4
BuildRequires:	libxfce4-util-devel >= 4.7.0
BuildRequires:	xfconf-devel >= 4.7.0
BuildRequires:	libnotify-devel >= 0.4.0
Requires:	thunar >= 1.1.2
Requires:	dbus >= 0.34
Requires:	hal >= 0.5.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std

# add onlyshowin=xfce in the .desktop file:
desktop-file-install --vendor="" \
		--remove-key="Encoding" \
		--add-only-show-in="XFCE" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/thunar-volman-settings.desktop


%find_lang %{name}

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/applications/thunar-volman-settings.desktop
