%define debug_package %{nil}

Summary:	Faba icon theme
Name:		faba-icon-theme
Version:	4.0
Release:	2
License:	GPLv3
Group:		Graphical desktop/Other
URL:		http://mokaproject.com/faba-icon-theme/
Source0:	https://github.com/moka-project/faba-icon-theme/raw/master/%{name}-%{version}.tar.gz
Requires:	hicolor-icon-theme

%description
Faba icon theme.

%prep
%setup -q

%build

%install
install -d -m 755 %{buildroot}%{_iconsdir}/Faba
cp -afR Faba %{buildroot}%{_iconsdir}/Faba

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-faba.filter << EOF
^./usr/share/icons/Faba/
EOF

cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-faba.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/Faba/
fi
EOF
chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-faba.script

%files
%doc AUTHORS
%{_iconsdir}/Faba
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-faba.*
