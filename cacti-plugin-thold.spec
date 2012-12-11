%define		plugin	thold
%define		php_min_version 5.1.1
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - Thold
Summary(pl.UTF-8):	Wtyczka do Cacti - Thold
Name:		cacti-plugin-%{plugin}
Version:	0.4.9
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:thold-v%{version}-3.tgz
# Source0-md5:	18fa28a60cafa0d9821fb5d9a8cf7823
Patch0:		%{name}-undefined_variable_subject.patch
Patch1:		%{name}-division_by_zero.patch
URL:		http://docs.cacti.net/plugin:thold
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.9
Requires:	cacti-plugin-settings >= 0.71
Requires:	php(core) >= %{php_min_version}
Requires:	php(gd)
Requires:	php(pcre)
Requires:	php-date
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
%setup -qc
mv %{plugin}/{LICENSE,README} .

%{__rm} thold/includes/.settings.php.swp

%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
