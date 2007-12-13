%define		namesrc	thold
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Thold
Summary(pl.UTF-8):	Wtyczka do Cacti - Thold
Name:		cacti-plugin-thold
Version:	0.3.8
Release:	2
License:	GPL v2.1
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{namesrc}-%{version}.zip
# Source0-md5:	811b9e8283cd10bc47c319571e8bc512
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
Requires:	cacti-plugin-settings
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - the Threshold Module (by Aurelio DeSimone) converted
to a plugin. Much easier to install and maintain. Requires that you
have the Plugin Architecture installed.

%description -l pl.UTF-8
Wtyczka do Cacti - moduł Threshold (który napisał Aurelio DeSimone)
przekształcony do wtyczki, dzięki czemu jest dużo łatwiejszy do
instalacji i utrzymania. Wymaga zainstalowanej architektury wtyczek.
Umożliwia monitoring parametrów i alarmowanie w przypadku
przekroczenia zadanych wartości lub niekorzystnych zmian w przebiegu
monitorowanych parametrów.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
