%define		extname		mylauncher
Summary:	Customizable menu for gnome shell/panel
Name:		gnome-shell-extension-%{extname}
Version:	20121027
Release:	0.1
Group:		X11/Applications
License:	GPLv2
# $ git clone git://github.com/mbokil/mylauncher-extension.git
# $ cd mylauncher-extension/
# $ git archive --format=tar --prefix=%{extname}-%{version}/ master | xz > ../%{extname}-%{version}.tar.xz
Source0:	%{extname}-%{version}.tar.xz
# Source0-md5:	2b1e69daf0d39d1a4b478fd6eaa9e83b
URL:		http://markbokil.com/downloads/extensions/
Requires:	gnome-shell >= 3.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyLauncher is a customizable menu which can launch links, shell
scripts, apps, and open folders. Right-click the menu after
installation to edit the launcher. See help on the right-click for
listing of all options. MyLauncher also supports alias commands such
as [RG] for restart shell, [TD] for toggle desktop, etc.

%prep
%setup -q -n %{extname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas \
	$RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/mylauncher@markbokil.com

install schemas/org.gnome.shell.extensions.mylauncher.gschema.xml $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/
install *.js* $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/mylauncher@markbokil.com/
install *.css $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/mylauncher@markbokil.com/
install *.svg $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/mylauncher@markbokil.com/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.mylauncher.gschema.xml
%{_datadir}/gnome-shell/extensions/mylauncher*
