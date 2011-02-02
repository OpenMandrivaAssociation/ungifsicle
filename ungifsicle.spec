Summary: 	Powerful program for manipulating GIF images and animations
Name: 		ungifsicle
Version: 	1.58
Release:	%mkrel 3
Group: 		Graphics
License: 	GPLv2
URL: 		http://www.lcdf.org/gifsicle
Source0: 	http://www.lcdf.org/gifsicle/%{name}-%{version}.tar.gz
BuildRequires:	libx11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
