Summary:	A removable volume manager for Thunar
Name:		thunar-volman
Version:	0.2.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://foo-projects.org/~benny/projects/thunar-volman/index.html
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.bz2
Patch1:		%{name}-0.1.2-audio-player.patch
Requires:	thunar >= 0.8.0
Requires:	dbus >= 0.34
Requires:	hal >= 0.5.0
BuildRequires:	thunar-devel >= 0.8.0
BuildRequires:	dbus-devel >= 0.34
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	libusb-devel
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
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

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
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_libdir}/thunar-volman-settings
%{_datadir}/applications/thunar-volman-settings.desktop
