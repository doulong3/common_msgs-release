Name:           ros-kinetic-common-msgs
Version:        1.12.6
Release:        0%{?dist}
Summary:        ROS common_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/common_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-shape-msgs
Requires:       ros-kinetic-stereo-msgs
Requires:       ros-kinetic-trajectory-msgs
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  ros-kinetic-catkin

%description
common_msgs contains messages that are widely used by other ROS packages. These
includes messages for actions (actionlib_msgs), diagnostics (diagnostic_msgs),
geometric primitives (geometry_msgs), robot navigation (nav_msgs), and common
sensors (sensor_msgs), such as laser range finders, cameras, point clouds.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu May 03 2018 Tully Foote <tfoote@osrfoundation.org> - 1.12.6-0
- Autogenerated by Bloom

* Fri Sep 30 2016 Tully Foote <tfoote@osrfoundation.org> - 1.12.5-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Tully Foote <tfoote@osrfoundation.org> - 1.12.4-0
- Autogenerated by Bloom

