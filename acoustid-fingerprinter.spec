Summary:	Acoustid Fingerprinter
Summary(pl.UTF-8):	Narzędzie do tworzenia odcisków Acoustid
Name:		acoustid-fingerprinter
Version:	0.6
Release:	1
License:	LGPL v2.1+
Group:		Applications/Sound
Source0:	https://github.com/downloads/lalinsky/acoustid-fingerprinter/%{name}-%{version}.tar.gz
# Source0-md5:	14e2e797ea09474a8862d200234f5e6b
URL:		http://acoustid.org/fingerprinter
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	QtNetwork-devel >= 4
BuildRequires:	cmake >= 2.6
BuildRequires:	ffmpeg-devel
BuildRequires:	libchromaprint-devel
BuildRequires:	qt4-build >= 4
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acoustid fingerprinter is a cross-platform GUI application that uses
Chromaprint to submit audio fingerprints from your music collection to
the Acoustid database. Only tagged audio files are submitted. Files
tagged by MusicBrainz applications such as Picard or Jaikoz are
preferred, but it will submit fingerprints for any files that have
tags such as track title, artist name, album name, etc.

%description -l pl.UTF-8
Acoustid finterprinter to wieloplatformowa aplikacja z graficznym
interfejsem użytkownika, wykorzystująca Chromaprint do wysyłania
dźwiękowych "odcisków palca" z kolekcji muzyki do bazy danych
Acoustid. Przesyłane są tylko oznaczone pliki dźwiękowe. Preferowane
są pliki oznaczone przez aplikacje MusicBrainz, takie jak Picard czy
Jaikoz, ale można przesłać także odciski dla dowolnych plików,
mających znaczniki takie jak tytuł utworu, nazwę wykonawcy, nazwę
albumu itp.

%prep
%setup -q

%build
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm  -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_bindir}/acoustid-fingerprinter
%{_desktopdir}/acoustid-fingerprinter.desktop
