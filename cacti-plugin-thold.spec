%define		plugin	thold
%define		php_min_version 5.1.1
Summary:	Plugin for Cacti - Thold
Summary(pl.UTF-8):	Wtyczka do Cacti - Thold
Name:		cacti-plugin-%{plugin}
Version:	1.8.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/Cacti/plugin_thold/archive/refs/tags/v%{version}.tar.gz?/plugin_thold-%{version}.tar.gz
# Source0-md5:	013ce9d41c9b21c0c04fb175698ecce0
URL:		https://github.com/Cacti/plugin_thold
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 3.1
Requires:	cacti-plugin-settings >= 0.71
Requires:	php(core) >= %{php_min_version}
Requires:	php(gd)
Requires:	php(pcre)
Requires:	php(date)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This plugin is for the alerting of data found within any graph within
Cacti.

Thold is Cacti's premier Alerting modules that integrates seamlessly
with Cacti's Graphing engine.

%description -l pl.UTF-8
Wtyczka do Cacti - moduł Threshold (który napisał Aurelio DeSimone)
przekształcony do wtyczki, dzięki czemu jest dużo łatwiejszy do
instalacji i utrzymania. Wymaga zainstalowanej architektury wtyczek.
Umożliwia monitoring parametrów i alarmowanie w przypadku
przekroczenia zadanych wartości lub niekorzystnych zmian w przebiegu
monitorowanych parametrów.

%prep
%setup -q -n plugin_thold-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/LICENSE $RPM_BUILD_ROOT%{plugindir}/README.md

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{plugindir}
