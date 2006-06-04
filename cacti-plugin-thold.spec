%define		namesrc	thold
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Thold
Summary(pl):	Wtyczka do Cacti - Thold
Name:		cacti-plugin-thold
Version:	0.3.0
Release:	1
License:	GPL v2.1
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	87c9b0bd79968bc3a39e071d9a0e4365
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - the Threshold Module (by Aurelio DeSimone) converted
to a plugin. Much easier to install and maintain. Requires that you
have the Plugin Architecture installed.

%description -l pl
Wtyczka do Cacti - modu³ Threshold (który napisa³ Aurelio DeSimone)
przekszta³cony do wtyczki, dziêki czemu jest du¿o ³atwiejszy do
instalacji i utrzymania. Wymaga zainstalowanej architektury wtyczek.
Umozliwia monitoring parametrów i alarmowanie w przypadku 
przekroczenia zadanych wartosci lub niekorzystnych zmian w przebiegu
monitorowanych parametrów

%prep
%setup -q -n %{namesrc}

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
