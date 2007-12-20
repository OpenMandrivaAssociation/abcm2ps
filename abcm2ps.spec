%define version 4.12.28
%define release %mkrel 1

Name:		abcm2ps
Version:	%{version}
Release:	%{release}
Summary:	Converts ABC format music sheets into Postscript
License:	GPL
URL:		http://moinejf.free.fr
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://moinejf.free.fr/%{name}-%{version}.tar.bz2
Patch0:		abcm2ps_makefile.patch

%description
abcm2ps is a package which converts music tunes from ABC format
to PostScript. Based on abc2ps version 1.2.5, it was developed
mainly to print polyphonic music, i.e. music with multiple voices
per staff. abcm2ps uses an extension to the ABC language that make
it suitable for classical music. This extended format is documented
under http://abcplus.sourceforge.net/.

%prep
%setup -q

%patch0 -p 1

%build
%configure2_5x --enable-a4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes INSTALL License README *.abc *.txt sample3.eps
%{_bindir}/*
%{_datadir}/abcm2ps


