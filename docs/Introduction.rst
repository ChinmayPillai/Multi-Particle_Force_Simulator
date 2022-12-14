Introduction
^^^^^^^^^^^^

We tackle this problem by discretising time and taking the force to be constant for a
‘time_step’ time. At every instant, for all particles, we find the net force on that particle due
to all other particles and update its position and velocity due to this net force. Letting this
evolve gives us our required simulation.

We first define a ‘Vector’ class followed by a ‘Particle’ class with parameters – Mass,
Charge, Position (Vector), and Velocity (Vector). We define functions to read and write these
variables and operator overloading functions on the class.

Then we define a Simulation Engine class consisting of a Force vector and two virtual
functions – force() and run().

Two new Engine classes inherit this class – Gravity Simulator and Electrostatic Force
Simulator, each of which have a different force function.

- **force()** – Takes two particles as arguments and calculates the force between them
- **run()** – Takes a particle and time_step as arguments and updates the position and velocity of
the particle due to the Net force acting on it

| 

We run three nested ‘for’ loops. The innermost loop is to calculate the force on one particle
due to all other particles using the force() function. The middle loop uses the net force on a
particle to update its position and velocity using the run() function and does this for all
particles. The outermost loop is to go through the time instances, making the system evolve.


Author:
=======
Chinmay Pillai