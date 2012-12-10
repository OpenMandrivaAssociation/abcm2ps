Name:		abcm2ps
Version:	7.0.13
Release:	1
Summary:	Converts ABC format music sheets into Postscript
License:	GPLv2+
URL:		http://abcplus.sourceforge.net/
Group:		Publishing
Source0:	http://moinejf.free.fr/%{name}-%{version}.tar.gz
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
%patch0 -p0

%build
%configure2_5x --enable-a4 --enable-deco-is-roll
%make

%install
%makeinstall 

%files
%doc Changes INSTALL License README *.abc *.txt sample3.eps
%{_bindir}/*
%{_datadir}/abcm2ps




%changelog
* Thu Jul 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 7.0.13-1
+ Revision: 809008
- version update 7.0.13

* Tue Mar 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 7.0.3-1
+ Revision: 782368
- version update  7.0.3

* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 7.0.2-1
+ Revision: 781000
- version update 7.0.2

* Wed Feb 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 7.0.1-1
+ Revision: 774377
- version update 7.0.1

* Tue Feb 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.6.5-1
+ Revision: 771608
- version update 6.6.4

* Sun Feb 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.6.4-1
+ Revision: 771297
- version update 6.6.4

* Wed Jan 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.6.3-1
+ Revision: 762093
- version update 6.6.3

* Tue Dec 06 2011 Alexander Khrukin <akhrukin@mandriva.org> 6.5.15-1
+ Revision: 738233
- version update 6.5.15

* Fri Nov 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 6.5.12-1
+ Revision: 731607
- version update

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 6.0.4-2mdv2011.0
+ Revision: 609901
- rebuild

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 6.0.4-1mdv2010.1
+ Revision: 503394
- update to 6.0.4

* Thu Jan 28 2010 Frederik Himpe <fhimpe@mandriva.org> 6.0.1-1mdv2010.1
+ Revision: 497674
- update to new version 6.0.1

* Fri Jan 22 2010 Frederik Himpe <fhimpe@mandriva.org> 6.0.0-1mdv2010.1
+ Revision: 495043
- update to new version 6.0.0

* Sat Dec 26 2009 Jérôme Brenier <incubusss@mandriva.org> 5.9.7-1mdv2010.1
+ Revision: 482332
- new version 5.9.7

* Fri Nov 06 2009 Jérôme Brenier <incubusss@mandriva.org> 5.9.6-1mdv2010.1
+ Revision: 462010
- update to new version 5.9.6
- changes for specfile policy
- source url completed

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Mon Sep 01 2008 Emmanuel Andry <eandry@mandriva.org> 4.12.30-1mdv2009.0
+ Revision: 278529
- New version
- fix license
- fix URL

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 4.12.28-1mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

