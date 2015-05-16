%define debug_package %{nil}

Summary:	Faba icon theme
Name:		faba-icon-theme
Version:	4.0
Release:	1
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

%files
%doc AUTHORS
%{_iconsdir}/Faba
