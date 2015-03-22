Name:           ros-jade-common-msgs
Version:        1.12.2
Release:        0%{?dist}
Summary:        ROS common_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/common_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-shape-msgs
Requires:       ros-jade-stereo-msgs
Requires:       ros-jade-trajectory-msgs
Requires:       ros-jade-visualization-msgs
BuildRequires:  ros-jade-catkin

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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Mar 21 2015 Tully Foote <tfoote@osrfoundation.org> - 1.12.2-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Tully Foote <tfoote@osrfoundation.org> - 1.12.1-0
- Autogenerated by Bloom

* Mon Dec 29 2014 Tully Foote <tfoote@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

