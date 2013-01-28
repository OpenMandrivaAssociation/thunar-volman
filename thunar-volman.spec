%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A removable volume manager for Thunar
Name:		thunar-volman
Version:	0.8.0
Release:	2
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

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/applications/thunar-volman-settings.desktop


%changelog
* Tue May 01 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-1
+ Revision: 794654
- update to new version 0.8.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.1-1
+ Revision: 791050
- update to new version 0.7.1

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.0-1
+ Revision: 789668
- drop desktop-file-install script
- update to new version 0.7.0
- spec file clean

* Thu Apr 05 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-2
+ Revision: 789477
- update buildrequires
- drop old stuff from spec file

* Sat Mar 31 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-1
+ Revision: 788526
- use pkgconfig(gudev-1.0) as a buildrequire
- update to new version 0.6.1

* Fri Apr 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-3
+ Revision: 660731
- obsolete xfce4-volstatus-icon

* Tue Apr 19 2011 Funda Wang <fwang@mandriva.org> 0.6.0-2
+ Revision: 656033
- rebuild for libnotify 0.7

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1
+ Revision: 632766
- update to new version 0.6.0

* Wed Dec 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.3-1mdv2011.0
+ Revision: 616410
- update to new version 0.5.3

* Mon Nov 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-2mdv2011.0
+ Revision: 595119
- drop buildrequires and requires on hal
- gvfs is needed as a runtime dependency, without this auto mount does not work

* Sun Nov 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.2-1mdv2011.0
+ Revision: 594764
- update to new version 0.5.2

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.1-1mdv2011.0
+ Revision: 579585
- update to new version 0.5.1
- drop patch0
- adjust buildrequires
- fix file list

* Thu Jun 17 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.80-6mdv2010.1
+ Revision: 548214
- only show .desktop file in XFCE

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.80-5mdv2010.1
+ Revision: 543286
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.3.80-4mdv2010.0
+ Revision: 445425
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.80-3mdv2009.1
+ Revision: 349271
- Patch0: fix compiling with -Werror=format-strings

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.80-2mdv2009.1
+ Revision: 294880
- drop patch 3

* Thu Sep 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.80-1mdv2009.1
+ Revision: 285641
- update to new version 0.3.80
- drop patches 1 and 2, as they were merged upstream
- Patch3: lower exo version requirements (for LUKS support)

* Wed Aug 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-6mdv2009.0
+ Revision: 274172
- Patch2: add support for LUKS encrypted volumes (upstream bug #3349)

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-5mdv2009.0
+ Revision: 261535
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.2.0-4mdv2009.0
+ Revision: 254538
- rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - revert, it is pointless to backport this patch, too much effort
    - Patch4: add support for LUKS encrypted volumes (upstream bug #3349)
    - run scriplets only for mdv older than 2009

* Wed Mar 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-2mdv2008.1
+ Revision: 189004
- fix summary
- add missing buildrequires on libusb-devel
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 Jérôme Soyer <saispo@mandriva.org> 0.2.0-1mdv2008.1
+ Revision: 115271
- New release 0.2.0

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new license policy
    - do not package COPYING and INSTALL files

* Tue Sep 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-3mdv2008.0
+ Revision: 79380
- provide patch 0 (properlly detect DVD disks)
  provide patch 1 (run audio player only for ipod medias alike)

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-2mdv2008.0
+ Revision: 33283
- drop __libtoolize
- spec file clean
- add macros to %%post and %%postun


* Tue Apr 03 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.2-1mdv2007.1
+ Revision: 150344
- Import thunar-volman

