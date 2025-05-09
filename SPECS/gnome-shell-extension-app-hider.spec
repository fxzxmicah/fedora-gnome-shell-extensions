%global extension       app-hider
%global developer       lynith.dev
%global uuid            %{extension}@%{developer}

Name:           gnome-shell-extension-%{extension}
Version:        23
Release:        %autorelease
Summary:        GNOME Shell extension to hide apps in GNOME's app menu
License:        GPL-2.0-only
URL:            https://github.com/LynithDev/gnome-app-hider
BuildArch:      noarch

Source:         https://extensions.gnome.org/extension-data/%{extension}%{developer}.v%{version}.shell-extension.zip

Source1:        %{url}/raw/refs/heads/master/LICENSE#/LICENSE.%{extension}

Requires:       gnome-shell >= 48
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
%{summary}.


%prep
%autosetup -c

cp %{SOURCE1} LICENSE

# fix spurious-executable-perm and script-without-shebang rpmlint warnings/errors
find -type f -print -exec chmod 644 {} \;


%build
# Nothing to build


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

for file in *.*; do
    cp -a $file %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
done
cp -a patches %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install locale files
cp -a locale %{buildroot}%{_datadir}/
%find_lang %{uuid}


%files -f %{uuid}.lang
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
