Summary: 	Powerful program for manipulating GIF images and animations
Name: 		ungifsicle
Version: 	1.58
Release:	5
Group: 		Graphics
License: 	GPLv2
URL: 		https://www.lcdf.org/gifsicle
Source0: 	http://www.lcdf.org/gifsicle/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(x11)

%description
Gifsicle manipulates GIF image files on the command line. It supports merging
several GIFs into a GIF animation; exploding an animation into its component
frames; changing individual frames in an animation; turning interlacing on and
off; adding transparency; adding delays, disposals, and looping to animations;
adding or removing comments; optimizing animations for space; and changing
images' colormaps, among other things.

The gifsicle package contains two other programs: gifview, a lightweight GIF
viewer for X, can show animations as slideshows or in real time, and gifdiff
compares two GIFs for identical visual appearance.

Those programs don't use LZW compression to avoid patent problems

%prep

%setup -q
touch `find . -type f`

%build
%configure2_5x --enable-ungif
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc NEWS README
%attr (0755,root,root) %_bindir/*
%attr (0644,root,root) %_mandir/man1/*


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.58-3mdv2011.0
+ Revision: 635351
- tighten BR

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.58-2mdv2011.0
+ Revision: 615356
- the mass rebuild of 2010.1 packages

* Sun Jan 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.58-1mdv2010.1
+ Revision: 495515
- 1.58
- misc spec file fixes

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.42-5mdv2010.0
+ Revision: 434543
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.42-3mdv2009.0
+ Revision: 255146
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.42-1mdv2008.1
+ Revision: 128749
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import ungifsicle


* Tue Apr 26 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.42-1mdk
- 1.42

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.35-3mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.35-2mdk
- rebuild

* Thu Oct 10 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.35-1mdk
- 1.35

* Wed Sep 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.30-1mdk
- 1.30

* Wed Apr 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.25-1mdk
- added in contribs by Pierre-Michel THEVENY <pmt@mnhn.fr> :
	- Ported to Mandrake from rpm.spec in sources tarball
	- Build on Mandrake 8.0 (rpm-4.0)
