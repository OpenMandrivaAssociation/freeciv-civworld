%define civname	freeciv
%define name	%{civname}-civworld
%define version	1.14.0
%define release %mkrel 5

Name:		%{name}
Summary:	Editor for FREE CIVilization clone
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.freeciv.org/freeciv/stable/%{civname}-%{version}.tar.bz2
Source1:	%{name}
Source10:	%{name}.16.png
Source11:	%{name}.32.png
Source12:	%{name}.48.png
Patch0:		ftp://ftp.freeciv.org/freeciv/contrib/utils/civworld/civworld-%{version}.diff-against-freeciv
Patch1:		%{name}-fix_typo.patch
License:	GPL
Group:		Games/Strategy
Requires:	freeciv-data = %{version}
BuildRequires:	imlib-devel
BuildRequires:	libSDL_mixer-devel
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://www.freeciv.org

%description
Freeciv is a multiplayer strategy game, released under the GNU General
Public License. It is generally comparable with Civilization II(r),
published by Microprose(r).

This package contains CivWorld, the editor for saved games and scenarios. 
CivWorld is considered unstable, but works reasonably well nonetheless.

%prep
%setup -q -n%{civname}-%{version}
%patch -p1
%patch1 -p1

%build
#./autogen.sh
autoconf
automake
%configure --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m755 civworld/civworld -D $RPM_BUILD_ROOT%{_gamesbindir}/civworld

# menu
install -m644 %{SOURCE1} -D $RPM_BUILD_ROOT%{_menudir}/%{name}

# icons
install -m644 %{SOURCE10} -D $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -fr %buildroot

%files
%defattr(-, root, root, 0755)
%doc civworld/ChangeLog civworld/README.civworld civworld/TODO.civworld
%defattr(-, root, games, 0755)
%{_gamesbindir}/civworld
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

