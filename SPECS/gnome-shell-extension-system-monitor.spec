%global extension       system-monitor
%global developer       gnome-shell-extensions.gcampax.github.com
%global uuid            %{extension}@%{developer}

Name:           gnome-shell-extension-%{extension}
Version:        6
Release:        %autorelease
Summary:        GNOME Shell extension to monitor system from the top bar
License:        GPL-2.0-only
URL:            https://gitlab.gnome.org/GNOME/gnome-shell-extensions/-/tree/main/extensions/system-monitor
BuildArch:      noarch

Source:         https://extensions.gnome.org/extension-data/%{extension}%{developer}.v%{version}.shell-extension.zip

Patch0:         system-monitor.patch

Requires:       gnome-shell >= 45
Requires:       gnome-shell-extension-common >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
%{summary}.


%prep
%autosetup -c

# fix spurious-executable-perm and script-without-shebang rpmlint warnings/errors
find -type f -print -exec chmod 644 {} \;


%build
# fix gettext-domain in metadata
sed -i -E 's/"gettext-domain": ?"[^"]*"/"gettext-domain": "gnome-shell-extensions"/' metadata.json


%install
# install main extension files
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

for file in *.*; do
    cp -a $file %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
done
cp -a icons %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%files
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog
