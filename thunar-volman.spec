%define __libtoolize /bin/true 

Summary:     An archive plugin for the Thunar File Manager
Name: 		thunar-volman
Version: 	0.1.2
Release: 	%mkrel 1
License:	GPL
URL: 		http://xfce4-goodies.berlios.de
Source0: 	%{name}-%{version}.tar.bz2
Group: 		Graphical desktop/Xfce
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Requires:       thunar >= 0.2.2
Requires:       dbus >= 0.34
Requires:       hal >= 0.5.0
#optional requires..at least 1 is needed
#Requires:     file-roller
#Requires:     kdeutils-ark
BuildRequires:	thunar-devel >= 0.2.2
BuildRequires:	dbus-devel >= 0.34
BuildRequires:	hal-devel >= 0.5.0

%description
The Thunar Volume Manager is an extension for the Thunar 
file manager, which enables automatic management of removable 
drives and media. For example, if thunar-volman is installed 
and configured properly, and you plug in your digital camera, 
it will automatically launch your preferred photo application 
and import the new pictures from the camera into your photo collection.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS
%{_bindir}/thunar-volman
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
 


