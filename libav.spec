Summary:	Complete solution to record, convert and stream audio and video
Name:		libav
Version:	9.7
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://libav.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	3adef6ca31a891a4e7b7bfce4b0411e5
URL:		http://libav.org
BuildRequires:	SDL-devel
BuildRequires:	flac-devel
BuildRequires:	freetype-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libvpx-devel
BuildRequires:	libx264-devel
BuildRequires:	nasm
BuildRequires:	opencore-amr-devel
BuildRequires:	perl-tools-pod
BuildRequires:	texinfo
BuildRequires:	vo-aacenc-devel
BuildRequires:	xvidcore-devel
BuildRequires:	zlib-devel
BuildConflicts:	ffmpeg-libs
Conflicts:	ffmpeg-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Libav is a complete, cross-platform solution to record, convert
and stream audio and video. It includes libavcodec - the leading
audio/video codec library.

%package devel
Summary:	libav header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libav header files.

%package progs
Summary:	libav libraries
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description progs
Utilities for converting video and audio.

%prep
%setup -q

%build
# not autoconf configure
./configure \
	--arch=%{_target_base_arch}	\
	--libdir=%{_libdir}		\
	--mandir=%{_mandir}		\
	--prefix=%{_prefix}		\
	--shlibdir=%{_libdir}		\
	--cc="%{__cc}"			\
	--extra-cflags="%{rpmcflags}"	\
	--extra-ldflags="%{rpmldflags}"	\
	--disable-debug			\
	--disable-avplay		\
	--disable-avserver		\
	--disable-static		\
	--enable-avfilter		\
	--enable-gpl			\
	--enable-libdc1394		\
	--enable-libmp3lame		\
	--enable-libopencore-amrnb	\
	--enable-libopencore-amrwb	\
	--enable-libtheora		\
	--enable-libvo-aacenc		\
	--enable-libvorbis		\
	--enable-libvpx			\
	--enable-libx264		\
	--enable-libxvid		\
	--enable-pthreads		\
	--enable-runtime-cpudetect	\
	--enable-shared			\
	--enable-vaapi			\
	--enable-version3		\
	--enable-x11grab
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libavcodec.so.??
%attr(755,root,root) %ghost %{_libdir}/libavdevice.so.??
%attr(755,root,root) %ghost %{_libdir}/libavfilter.so.?
%attr(755,root,root) %ghost %{_libdir}/libavformat.so.??
%attr(755,root,root) %ghost %{_libdir}/libavresample.so.?
%attr(755,root,root) %ghost %{_libdir}/libavutil.so.??
%attr(755,root,root) %ghost %{_libdir}/libswscale.so.?
%attr(755,root,root) %{_libdir}/libavcodec.so.*.*.*
%attr(755,root,root) %{_libdir}/libavdevice.so.*.*.*
%attr(755,root,root) %{_libdir}/libavfilter.so.*.*.*
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %{_libdir}/libavresample.so.*.*.*
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/optimization.txt
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavdevice.so
%attr(755,root,root) %{_libdir}/libavfilter.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libavresample.so
%attr(755,root,root) %{_libdir}/libavutil.so
%attr(755,root,root) %{_libdir}/libswscale.so
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavfilter
%{_includedir}/libavformat
%{_includedir}/libavresample
%{_includedir}/libavutil
%{_includedir}/libswscale
%{_pkgconfigdir}/*.pc

%files progs
%defattr(644,root,root,755)
%doc README doc/RELEASE_NOTES
%attr(755,root,root) %{_bindir}/avconv
%attr(755,root,root) %{_bindir}/avprobe
%{_datadir}/avconv

