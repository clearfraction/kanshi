%global libscfg_ver 0.1.1


Name     : kanshi
Version  : 1.6.0
Release  : 1
URL      : https://git.sr.ht/~emersion/kanshi
Source0  : https://git.sr.ht/~emersion/kanshi/archive/v%{version}.tar.gz
Source1  : https://git.sr.ht/~emersion/libscfg/archive/v%{libscfg_ver}.tar.gz
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
%setup -q -n kanshi-v%{version} -a 1

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "

pushd libscfg-v%{libscfg_ver}
    meson --libdir=lib64 --prefix=/usr --buildtype=plain builddir2
    ninja -v -C builddir2
    DESTDIR=/ ninja -C builddir2 install
popd

meson --libdir=lib64 --prefix=/usr --buildtype=plain builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
mkdir %{buildroot}/usr/lib64
cp /usr/lib64/libscfg.so %{buildroot}/usr/lib64/libscfg.so
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/kanshi
/usr/lib64/libscfg.so
