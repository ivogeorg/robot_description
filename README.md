### robot_description

A URDF model of a simple robot for Gazebo.

### TODO

1. Add "hubcaps" to the outside of the two rear wheels to make rotation visible.
   1. Create from a box and place on the "outside" of wheel.
   2. Add under the wheel link.
   3. No joint necessary.
2. Add a caster wheel to the front.
   1. Create from two spheres, one for support, and one for contact. _This is a first-order model. The contact sphere doesn't actually rotate._
   2. Support twice as big as contact.
   3. Borrow inertia from other elements.
   4. Fixed joint with chassis.

### References

1. [Moments of inertia](https://en.wikipedia.org/wiki/List_of_moments_of_inertia).
2. [Robotnik RB-1](https://robotnik.eu/products/mobile-robots/rb-1-base-en/).
