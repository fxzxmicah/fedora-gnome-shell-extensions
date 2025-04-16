%global extension       blur-my-shell
%global developer       aunetx
%global uuid            %{extension}@%{developer}

Name:           gnome-shell-extension-%{extension}
Version:        68
Release:        %autorelease
Summary:        GNOME Shell extension to add a blur look to different parts of the GNOME Shell
License:        GPL-3.0-only
URL:            https://github.com/aunetx/blur-my-shell
BuildArch:      noarch

Source:         https://extensions.gnome.org/extension-data/%{extension}%{developer}.v%{version}.shell-extension.zip

Requires:       gnome-shell >= 48
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
%{summary}.


%prep
%autosetup -c

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
cp -a components %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -a conveniences %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -a dbus %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -a effects %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -a preferences %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp -a ui %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

cp -a icons %{buildroot}%{_datadir}/

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
%{_datadir}/icons/*/*/*/*
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
