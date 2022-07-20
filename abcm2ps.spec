Name:		abcm2ps
Version:	8.14.13
Release:	1
Summary:	Converts ABC format music sheets into Postscript
License:	GPLv2+
URL:		https://github.com/leesavide/abcm2ps
Group:		Publishing
Source0:	https://github.com/leesavide/abcm2ps/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch0:		abcm2ps_makefile.patch
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(pangocairo)

%description
abcm2ps is a package which converts music tunes from ABC format
to PostScript. Based on abc2ps version 1.2.5, it was developed
mainly to print polyphonic music, i.e. music with multiple voices
per staff. abcm2ps uses an extension to the ABC language that make
it suitable for classical music. This extended format is documented
under http://abcplus.sourceforge.net/.

%prep
%autosetup -p1
%configure --enable-a4 --enable-deco-is-roll

%build
%make_build

%install
%make_install 

%files
%doc README.md *.abc sample3.eps
%{_datadir}/doc/abcm2ps/examples/*
%{_bindir}/*
%{_datadir}/abcm2ps
%{_mandir}/man1/abcm2ps.1.*
