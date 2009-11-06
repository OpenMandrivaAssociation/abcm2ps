%define version 5.9.6
%define release %mkrel 1

Name:		abcm2ps
Version:	%{version}
Release:	%{release}
Summary:	Converts ABC format music sheets into Postscript
License:	GPLv2+
URL:		http://abcplus.sourceforge.net/
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://moinejf.free.fr/%{name}-%{version}.tar.gz
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
rm -rf %{buildroot}
%makeinstall 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes INSTALL License README *.abc *.txt sample3.eps
%{_bindir}/*
%{_datadir}/abcm2ps


