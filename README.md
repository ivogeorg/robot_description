### robot_description

A URDF model of a simple robot for Gazebo.

### TODO

1. Check if the `Expand Joint Details: false` setting in `config.rviz` is suppressing the showing of the joint. The checkpoint project requires explicit visualization of the joints.
2. Check why:
   1. the robot caster wheel "sinks" underneath the surface in Gazebo;
   2. why the robot "leans" forward.

### References

1. [Moments of inertia](https://en.wikipedia.org/wiki/List_of_moments_of_inertia).
2. [Robotnik RB-1](https://robotnik.eu/products/mobile-robots/rb-1-base-en/).
3. [Gazebo ROS-URDF](http://gazebosim.org/tutorials?tut=ros_urdf).
4. [ROS link](http://wiki.ros.org/urdf/XML/link).
5. [ROS joint](http://wiki.ros.org/urdf/XML/joint).
6. [ROS-URDF Materials](https://classic.gazebosim.org/tutorials?tut=ros_urdf#Materials:Usingpropercolorsandtextures). _Note that the [source](https://github.com/gazebosim/gazebo-classic/blob/master/media/materials/scripts/gazebo.material) is all scripts which parameterize sets of internal Gazebo simulation capabilities._
7. [Gazebo physics friction](http://gazebosim.org/tutorials?tut=friction).
8. [Engineering Toolbox friction](https://www.engineeringtoolbox.com/friction-coefficients-d_778.html).
9. [Gazebo ROS packages and plugins](http://wiki.ros.org/gazebo_ros_pkgs).
10. [Gazebo ROS packages and plugins (Github)](https://github.com/ros-simulation/gazebo_ros_pkgs).
11. [ROS XACRO](http://wiki.ros.org/xacro).

