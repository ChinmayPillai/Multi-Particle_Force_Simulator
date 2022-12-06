# Multi-Body_Force_Simulation

## N_Body.py

Simulation of Multi-Body Evolution due to Gravity/Electrostatic Force given Mass, Charge, Position, and Velocity


- Input: CSV File named "N_Body" with data columns - 'Mass, Charge, Position_X, Position_Y, Position_Z, Velocity_X, Velocity_Y and Velocity_Z' (no header)

- Output: 'n' CSV Files with data columns - 'Time(in seconds), Position_X, Position_Y and Position_Z'


**Arguments:**
-	time_step (int): Steps size of discretising time (lower⇒more accurate): Force considered constant during this period and Output given at each time step. 
-	t_final (int): Time till which system is made to evolve
-	Engine (GravitySim or ElectroStaticSim): Specify whether to simulate Gravity or Electrostatic force, taking the other to be negligible [either GravitySim() or ElectroStaticSim()]
-	filepath (string): Path of input CSV

**Example execution from command-line:**
- python ./N_Body.py --time_step 10000 --t_final 5000000 --engine GravitySim --input .



## Description

We tackle this problem by discretising time and taking the force to be constant for a ‘time_step’ time. At every instant, for all particles, we find the net force on that particle due to all other particles and update its position and velocity due to this net force. Letting this evolve gives us our required simulation.

We first define a ‘Vector’ class followed by a ‘Particle’ class with parameters – Mass, Charge, Position (Vector), and Velocity (Vector). We define functions to read and write these variables and operator overloading functions on the class. 
Then we define a Simulation Engine class consisting of a Force vector and two virtual functions – force() and run(). 
Two new Engine classes inherit this class – Gravity Simulator and Electrostatic Force Simulator, each of which have a different force function. 

- force() – Takes two particles as arguments and calculates the force between them

- run() – Takes a particle and time_step as arguments and updates the position and velocity of the particle due to the Net force acting on it

We run three nested ‘for’ loops. The innermost loop is to calculate the force on one particle due to all other particles using the force() function. The middle loop uses the net force on a particle to update its position and velocity using the run() function and does this for all particles. The outermost loop is to go through the time instances, making the system evolve.



## Animate.py

Code to animate and export video of the evolution of the system. Videos of Solar System Simulation can be found in the folder 'Simulations Videos & Photos'


**Arguments:**
-	n (int): Number of Particles
-	filepath (string): Path of folder containing input CSVs
-	output (string): Path of folder for output Video
-	in_step (int): Adjust resolution of animation. Skip (in_step-1) many lines from CSV between each input line. 0 is for no skips and higher in_step gives faster computation
-	interval (int): Interval in msec between each frame for animation
-	frames (int): Number of frames in output video


**Example execution from command-line:**
- python ./Animate.py --n 9 --input ./Output --output . --in_step 10 --interval 100 --frames 50



## TimePeriods.py
Code to find the time period of revolution of every particle

**Arguments:**
-	n (int): Number of Particles
-	filepath (string): Path of folder containing input CSV

**Example execution from command-line:**
- python ./TimePeriods.py --n 9 --input ./Output


## Eccentricity.py
Code to find the eccentricity of orbit of every particle

**Arguments:**
-	n (int): Number of Particles
-	filepath (string): Path of folder containing input CSV

**Example execution from command-line:**
- python ./Eccentricity.py --n 9 --input ./Output

## Execution Time
Code that takes both a function and its arguments as its own arguments and returns the result
of the function along with the time required to execute that function in seconds.
