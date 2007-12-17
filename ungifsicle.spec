%define name	ungifsicle
%define	version 1.42
%define release	%mkrel 1

Summary: 	Powerful program for manipulating GIF images and animations
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Group: 		Graphics
License: 	GPL
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://www.lcdf.org/gifsicle

BuildRequires: X11-devel

%description
Gifsicle manipulates GIF image files on the
command line. It supports merging several GIFs
into a GIF animation; exploding an animation into
its component frames; changing individual frames
in an animation; turning interlacing on and off;
adding transparency; adding delays, disposals, and
looping to animations; adding or removing
comments; optimizing animations for space; and
changing images' colormaps, among other things.

The gifsicle package contains two other programs:
gifview, a lightweight GIF viewer for X, can show
animations as slideshows or in real time, and
gifdiff compares two GIFs for identical visual
appearance.

Those programs don't use LZW compression
to avoid patent problems

%prep
%__rm -rf $RPM_BUILD_ROOT

%setup -q
touch `find . -type f`

%build
%configure --enable-ungif
%make

%install
%makeinstall
%__mkdir_p $RPM_BUILD_ROOT/%{_prefix}/X11R6/bin $RPM_BUILD_ROOT/%{_prefix}/X11R6/man/man1
%__mv  $RPM_BUILD_ROOT/%{_bindir}/gifview $RPM_BUILD_ROOT/%{_prefix}/X11R6/bin
%__mv  $RPM_BUILD_ROOT/%{_mandir}/man1/gifview.1 $RPM_BUILD_ROOT/%{_prefix}/X11R6/man/man1

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc NEWS README
%attr (0755,root,root) %_bindir/*
%attr (0644,root,root) %_mandir/man1/*
%attr (0755,root,root) %_prefix/X11R6/bin/*
%attr (0644,root,root) %_prefix/X11R6/man/man1/*

