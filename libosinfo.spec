#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0x97D9123DE37A484F (toso@posteo.net)
#
Name     : libosinfo
Version  : 1.12.0
Release  : 24
URL      : https://releases.pagure.org/libosinfo/libosinfo-1.12.0.tar.xz
Source0  : https://releases.pagure.org/libosinfo/libosinfo-1.12.0.tar.xz
Source1  : https://releases.pagure.org/libosinfo/libosinfo-1.12.0.tar.xz.asc
Source2  : 97D9123DE37A484F.pkey
Summary  : A library for managing OS information for virtualization
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+
Requires: libosinfo-bin = %{version}-%{release}
Requires: libosinfo-data = %{version}-%{release}
Requires: libosinfo-lib = %{version}-%{release}
Requires: libosinfo-license = %{version}-%{release}
Requires: libosinfo-locales = %{version}-%{release}
Requires: libosinfo-man = %{version}-%{release}
Requires: clr-hardware-files
BuildRequires : buildreq-meson
BuildRequires : clr-hardware-files
BuildRequires : docbook-xml
BuildRequires : gnupg
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : libsoup-dev
BuildRequires : pkgconfig(libsoup-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)
BuildRequires : vala-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package bin
Summary: bin components for the libosinfo package.
Group: Binaries
Requires: libosinfo-data = %{version}-%{release}
Requires: libosinfo-license = %{version}-%{release}

%description bin
bin components for the libosinfo package.


%package data
Summary: data components for the libosinfo package.
Group: Data

%description data
data components for the libosinfo package.


%package dev
Summary: dev components for the libosinfo package.
Group: Development
Requires: libosinfo-lib = %{version}-%{release}
Requires: libosinfo-bin = %{version}-%{release}
Requires: libosinfo-data = %{version}-%{release}
Provides: libosinfo-devel = %{version}-%{release}
Requires: libosinfo = %{version}-%{release}

%description dev
dev components for the libosinfo package.


%package doc
Summary: doc components for the libosinfo package.
Group: Documentation
Requires: libosinfo-man = %{version}-%{release}

%description doc
doc components for the libosinfo package.


%package lib
Summary: lib components for the libosinfo package.
Group: Libraries
Requires: libosinfo-data = %{version}-%{release}
Requires: libosinfo-license = %{version}-%{release}

%description lib
lib components for the libosinfo package.


%package license
Summary: license components for the libosinfo package.
Group: Default

%description license
license components for the libosinfo package.


%package locales
Summary: locales components for the libosinfo package.
Group: Default

%description locales
locales components for the libosinfo package.


%package man
Summary: man components for the libosinfo package.
Group: Default

%description man
man components for the libosinfo package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 97D9123DE37A484F' gpg.status
%setup -q -n libosinfo-1.12.0
cd %{_builddir}/libosinfo-1.12.0
pushd ..
cp -a libosinfo-1.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730293198
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Denable-vala=enabled \
-Denable-tests=false  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Denable-vala=enabled \
-Denable-tests=false  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libosinfo
cp %{_builddir}/libosinfo-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libosinfo/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/libosinfo-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/libosinfo/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libosinfo
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/osinfo-detect
/V3/usr/bin/osinfo-install-script
/V3/usr/bin/osinfo-query
/usr/bin/osinfo-detect
/usr/bin/osinfo-install-script
/usr/bin/osinfo-query

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Libosinfo-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libosinfo-1.0.deps
/usr/share/vala/vapi/libosinfo-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libosinfo-1.0/osinfo/osinfo.h
/usr/include/libosinfo-1.0/osinfo/osinfo_avatar_format.h
/usr/include/libosinfo-1.0/osinfo/osinfo_datamap.h
/usr/include/libosinfo-1.0/osinfo/osinfo_datamaplist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_db.h
/usr/include/libosinfo-1.0/osinfo/osinfo_deployment.h
/usr/include/libosinfo-1.0/osinfo/osinfo_deploymentlist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_device.h
/usr/include/libosinfo-1.0/osinfo/osinfo_device_driver.h
/usr/include/libosinfo-1.0/osinfo/osinfo_device_driverlist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_devicelink.h
/usr/include/libosinfo-1.0/osinfo/osinfo_devicelinkfilter.h
/usr/include/libosinfo-1.0/osinfo/osinfo_devicelinklist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_devicelist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_entity.h
/usr/include/libosinfo-1.0/osinfo/osinfo_enum_types.h
/usr/include/libosinfo-1.0/osinfo/osinfo_filter.h
/usr/include/libosinfo-1.0/osinfo/osinfo_firmware.h
/usr/include/libosinfo-1.0/osinfo/osinfo_firmwarelist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_image.h
/usr/include/libosinfo-1.0/osinfo/osinfo_imagelist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_install_config.h
/usr/include/libosinfo-1.0/osinfo/osinfo_install_config_param.h
/usr/include/libosinfo-1.0/osinfo/osinfo_install_config_paramlist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_install_script.h
/usr/include/libosinfo-1.0/osinfo/osinfo_install_scriptlist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_list.h
/usr/include/libosinfo-1.0/osinfo/osinfo_loader.h
/usr/include/libosinfo-1.0/osinfo/osinfo_macros.h
/usr/include/libosinfo-1.0/osinfo/osinfo_media.h
/usr/include/libosinfo-1.0/osinfo/osinfo_medialist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_os.h
/usr/include/libosinfo-1.0/osinfo/osinfo_os_variant.h
/usr/include/libosinfo-1.0/osinfo/osinfo_os_variantlist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_oslist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_platform.h
/usr/include/libosinfo-1.0/osinfo/osinfo_platformlist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_product.h
/usr/include/libosinfo-1.0/osinfo/osinfo_productfilter.h
/usr/include/libosinfo-1.0/osinfo/osinfo_productlist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_resources.h
/usr/include/libosinfo-1.0/osinfo/osinfo_resourceslist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_tree.h
/usr/include/libosinfo-1.0/osinfo/osinfo_treelist.h
/usr/include/libosinfo-1.0/osinfo/osinfo_version.h
/usr/lib64/libosinfo-1.0.so
/usr/lib64/pkgconfig/libosinfo-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-OsinfoFilter.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-avatar-format.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-datamap.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-datamaplist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-db.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-deployment.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-deploymentlist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-device-driver.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-device-driverlist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-device.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-devicelink.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-devicelinkfilter.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-devicelinklist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-devicelist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-entity.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-enum-types.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-firmware.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-firmwarelist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-image.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-imagelist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-install-config-param.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-install-config-paramlist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-install-config.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-install-script.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-install-scriptlist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-list.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-loader.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-media.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-medialist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-os-variant.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-os-variantlist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-os.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-oslist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-platform.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-platformlist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-product.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-productfilter.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-productlist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-resources.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-resourceslist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-tree.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-treelist.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo-osinfo-version.html
/usr/share/gtk-doc/html/Libosinfo/Libosinfo.devhelp2
/usr/share/gtk-doc/html/Libosinfo/annotation-glossary.html
/usr/share/gtk-doc/html/Libosinfo/api-index-full.html
/usr/share/gtk-doc/html/Libosinfo/ch01.html
/usr/share/gtk-doc/html/Libosinfo/depr-index.html
/usr/share/gtk-doc/html/Libosinfo/home.png
/usr/share/gtk-doc/html/Libosinfo/index.html
/usr/share/gtk-doc/html/Libosinfo/left-insensitive.png
/usr/share/gtk-doc/html/Libosinfo/left.png
/usr/share/gtk-doc/html/Libosinfo/object-tree.html
/usr/share/gtk-doc/html/Libosinfo/right-insensitive.png
/usr/share/gtk-doc/html/Libosinfo/right.png
/usr/share/gtk-doc/html/Libosinfo/style.css
/usr/share/gtk-doc/html/Libosinfo/up-insensitive.png
/usr/share/gtk-doc/html/Libosinfo/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libosinfo-1.0.so.0.1012.0
/usr/lib64/libosinfo-1.0.so.0
/usr/lib64/libosinfo-1.0.so.0.1012.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libosinfo/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libosinfo/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/osinfo-detect.1
/usr/share/man/man1/osinfo-install-script.1
/usr/share/man/man1/osinfo-query.1

%files locales -f libosinfo.lang
%defattr(-,root,root,-)

