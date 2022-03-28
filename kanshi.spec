Name     : kanshi
Version  : 1.2.0
Release  : 1
URL      : https://git.sr.ht/~emersion/kanshi
Source0  : https://git.sr.ht/~emersion/kanshi/archive/v%{version}.tar.gz
Summary  : Dynamic display configuration
Group    : Development/Tools
License  : MIT
BuildRequires : cmake
BuildRequires : buildreq-meson
BuildRequires : wayland-dev wayland-protocols-dev

%description
Kanshi allows you to define output profiles that are automatically enabled
and disabled on hotplug.

%prep
%setup -q -n kanshi-v%{version}

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/kanshi
