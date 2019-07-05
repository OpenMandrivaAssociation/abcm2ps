Name:		abcm2ps
Version:  8.14.4
Release:	1
Summary:	Converts ABC format music sheets into Postscript
License:	GPLv2+
URL:		http://abcplus.sourceforge.net/
Group:		Publishing
Source0:	http://moinejf.free.fr/%{name}-%{version}.tar.gz
#Patch0:		abcm2ps_makefile.patch

%description
abcm2ps is a package which converts music tunes from ABC format
to PostScript. Based on abc2ps version 1.2.5, it was developed
mainly to print polyphonic music, i.e. music with multiple voices
per staff. abcm2ps uses an extension to the ABC language that make
it suitable for classical music. This extended format is documented
under http://abcplus.sourceforge.net/.

%prep
%setup -q
#patch0 -p0

%build
%configure2_5x --enable-a4 --enable-deco-is-roll
%make_build

%install
%make_install 

%files
%doc README.md *.abc sample3.eps
%{_datadir}/doc/abcm2ps/examples/*
%{_bindir}/*
%{_datadir}/abcm2ps
%{_mandir}/man1/abcm2ps.1.xz





