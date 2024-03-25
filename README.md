### robot_description

A URDF model of a simple robot for Gazebo.

### TODO

1. Add a caster wheel to the front.
   1. Create from two spheres, one for support, and one for contact. _This is a first-order model. The contact sphere doesn't actually rotate._
   2. Support twice as big as contact.
   3. Borrow inertia entries from other elements. _Is this okay?_
   4. Fixed joint with chassis.
2. Check if the `Expand Joint Details: false` setting in `config.rviz` is suppressing the showing of the joint. The checkpoint project requires explicit visualization of the joints.

### References

1. [Moments of inertia](https://en.wikipedia.org/wiki/List_of_moments_of_inertia).
2. [Robotnik RB-1](https://robotnik.eu/products/mobile-robots/rb-1-base-en/).
