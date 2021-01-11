%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-stereo-msgs
Version:        1.13.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS stereo_msgs package

License:        BSD
URL:            http://wiki.ros.org/stereo_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
stereo_msgs contains messages specific to stereo processing, such as disparity
images.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon Jan 11 2021 Michel Hidalgo <michel@ekumenlabs.com> - 1.13.1-1
- Autogenerated by Bloom

* Thu May 21 2020 Tully Foote <tfoote@osrfoundation.org> - 1.13.0-1
- Autogenerated by Bloom

* Sun Feb 23 2020 Tully Foote <tfoote@osrfoundation.org> - 1.12.7-1
- Autogenerated by Bloom

