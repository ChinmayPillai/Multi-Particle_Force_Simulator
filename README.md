# Multi-Body_Force_Simulation

## N_Body.py

Simulation of Multi-Body Evolution due to Gravity/Electrostatic Force given Mass, Charge, Position, and Velocity


Input: CSV File named "N_Body" with data columns - 'Mass, Charge, Position_X, Position_Y, Position_Z, Velocity_X, Velocity_Y and Velocity_Z' (no header)

Output: 'n' CSV Files with data columns - 'Time(in seconds), Position_X, Position_Y and Position_Z'


Run Code after specifying the following variables within the code:

time_step (in seconds)(lower=>more accurate): Steps size of discretising time - Force considered constant during and Output given at each time step

t_final (in seconds): Time till which system is made to evolve

Engine: Specify whether to simulate Gravity or Electrostatic force, taking the other to be negligible [either GravitySim() or ElectroStaticSim()]


## Animate.py

Code to animate and export video of the evolution of the system. Videos of Solar System Simulation can be found in the folder 'Simulations Videos & Photos'


## TimePeriods.py
Code to find the time period of revolution of every particle

## Eccentricity.py
Code to find the eccentricity of orbit of every particle
