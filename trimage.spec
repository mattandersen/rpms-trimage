Name:		trimage
Version:	1.0.5
Release:	1%{?dist}
Summary:	GUI and command-line interface to optimize image files
Group:      Applications/Multimedia
License:	MIT
URL:		https://trimage.org/


Source0:	%{name}-%{version}.tar.gz
Patch0:		trimage-1.0.5-fix-egg-version.patch
BuildArch:	noarch
BuildRequires:	python2-devel
Requires:	python2
Requires:	PyQt4
Requires:	jpegoptim
Requires:	advancecomp
Requires:	optipng
Requires:	pngcrush


%description
Trimage is a cross-platform GUI and command-line interface to optimize image
files for websites, using optipng, pngcrush, advpng and jpegoptim, depending on
the filetype (currently, PNG and JPG files are supported). It was inspired by
imageoptim. All image files are losslessy compressed on the highest available
compression levels, and EXIF and other metadata is removed. Trimage gives you
various input functions to fit your own workflow: A regular file dialog,
dragging and dropping and various command line options.


%prep
%setup -q -n Trimage-%{version}
%patch0 -p1


%build
export CFLAGS="$RPM_OPT_FLAGS"
python setup.py build


%install
python setup.py install --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_mandir}/man1/%{name}*
%{python2_sitelib}/%{name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{name}/*


%changelog
* Sun Jun 18 2017 Matthew Andersen <matthew@barelystable.com> - 1.0.5-1
- Initial package for Fedora
