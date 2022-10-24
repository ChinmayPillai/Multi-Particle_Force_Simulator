# N-Body_Force_Simulation
Evolution of n bodies due to Gravity/Electrostatic Force given Mass, Charge, Position and Velocity

Input: CSV File named "N_Body" with data columns - 'Mass, Charge, Position_X, Position_Y, Position_Z, Velocity_X, Velocity_Y and Velocity_Z' (no header)

Output: 'n' CSV Files with data columns - 'Time(in seconds), Position_X, Position_Y and Position_Z'

Variables to Specify in code:
time_step(lower=> n\more accurate): Steps size of discretiing time (in seconds) - Force considered constant during and Output given at each time step
t_final: Time till which system is made to evolve
