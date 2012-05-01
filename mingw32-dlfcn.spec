%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

%global realname dlfcn-win32

%global alphatag r11

Name:          mingw32-dlfcn
Version:       0
Release:       0.7.%{alphatag}%{?dist}.3
Summary:       Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)


License:       LGPLv2+
Group:         Development/Libraries
URL:           http://code.google.com/p/dlfcn-win32/
Source0:       http://dlfcn-win32.googlecode.com/files/%{realname}-%{alphatag}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

BuildRequires: mingw32-filesystem >= 52
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
#BuildRequires: dos2unix

Patch1:        dlfcn_configure.patch
Patch2:        dlfcn-fix-cplusplus-linkage.patch


%description
This library implements a wrapper for dlfcn, as specified in POSIX and SUS,
around the dynamic link library functions found in the Windows API.


%package static
Summary:        Static version of the MinGW Windows dlfcn library
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Static version of the MinGW Windows dlfcn library.


%{_mingw32_debug_package}


%prep
%setup -q -n %{realname}-%{alphatag}

%{__sed} -i 's/\r//' configure
%{__sed} -i 's/\r//' README
%{__sed} -i 's/\r//' COPYING

%patch1 -p1
%patch2 -p0


%build
%{_mingw32_configure} \
  --incdir=%{_mingw32_includedir} \
  --cc=i686-pc-mingw32-gcc \
  --enable-shared=yes \
  --enable-static=yes \
  --enable-strip=i686-pc-mingw32-strip
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING
%{_mingw32_bindir}/libdl.dll
%{_mingw32_libdir}/libdl.dll.a
%{_mingw32_includedir}/dlfcn.h

%files static
%defattr(-,root,root,-)
%{_mingw32_libdir}/libdl.a


%changelog
* Mon Dec 27 2010 Andrew Beekhof <abeekhof@redhat.com> - 0-0.7.r11.3
- Rebuild everything with gcc-4.4
  Related: rhbz#658833

* Fri Dec 24 2010 Andrew Beekhof <abeekhof@redhat.com> - 0-0.7.r11.2
- The use of ExclusiveArch conflicts with noarch, using an alternate COLLECTION to limit builds
  Related: rhbz#658833

* Thu Dec 23 2010 Andrew Beekhof <abeekhof@redhat.com> - 0-0.7.r11.1
- Only build mingw packages on x86_64
  Related: rhbz#658833

* Fri Oct 30 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0-0.7.r11
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage
- Fixed %%defattr line
- Added -static subpackage
- Fixed linker error with C++ applications

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.r11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.r11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0-0.4.r11
- Rebuild for mingw32-gcc 4.4

* Wed Jan 14 2009 Richard W.M. Jones <rjones@redhat.com> - 0-0.3.r11
- Use Version 0
  (https://www.redhat.com/archives/fedora-packaging/2009-January/msg00064.html)
- Revert use of dos2unix for now
  (https://www.redhat.com/archives/fedora-packaging/2009-January/msg00066.html)
- Use _smp_mflags.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1-0.2.r11
- Import into fedora-mingw temporary repository because there are packages
  which will depend on this.
- Fix the version/release according to packaging guidelines.
- Tidy up the spec file.
- Use dos2unix and keep the timestamps.

* Fri Jan 02 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - r11-1
- Initial RPM release. 
