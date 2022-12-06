'''
Mult-Particle Gravity/Electrostatic Force Simulator
'''

from abc import ABC, abstractmethod
import csv
from scipy import constants


class Vector:
    '''
    Vector Class
    '''
    def __init__(self,x,y,z):
        '''
        Initialisation funtion for 'x', 'y' and 'z' components of vector

        Args:
            x (float): 'x' component of vector
            y (float): 'y' component of vector
            z (float): 'z' component of vector
        '''
        self._x = x
        self._y = y
        self._z = z
    
    #Accessor Functions
    def X(self):
        '''
        Accessor Function for 'x' component of vector

        Returns:
            float: 'x' component of vector
        '''
        return self._x

    def Y(self):
        '''
        Accessor Function for 'y' component of vector

        Returns:
            float: 'y' component of vector
        '''
        return self._y

    def Z(self):
        '''
        Accessor Function for 'z' component of vector

        Returns:
            float: 'z' component of vector
        '''
        return self._z

    #Manipulator Functions
    def NewX(self, new_x):
        '''
        Manipulator Function for 'x' component of vector

        Args:
            new_x (float): New 'x' component of vector
        '''
        self._x = new_x
    
    def NewY(self, new_y):
        '''
        Manipulator Function for 'y' component of vector

        Args:
            new_y (float): New 'y' component of vector
        '''
        self._y = new_y
    
    def NewZ(self, new_z):
        '''
        Manipulator Function for 'z' component of vector

        Args:
            new_z (float): New 'z' component of vector
        '''
        self._z = new_z
    
    #Operator Overloading
    def __add__(self,other):
        '''
        Operator Overloading for Vector Addition

        Args:
            other (Vector): Vector to add

        Returns:
            Vector: Vector obtained after addition
        '''
        v = Vector(self._x + other._x, self._y + other._y, self._z + other._z)
        return v

    def __iadd__(self,other):
        '''
        Operator Overloading for Vector Addition (+=)

        Args:
            other (Vector): Vector to add

        Returns:
            Vector: Vector obtained after addition
        '''
        self = self + other
        return self

    def __sub__(self,other):
        '''
        Operator Overloading for Vector Subtraction

        Args:
            other (Vector): Vector to subtract

        Returns:
            Vector: Vector obtained after subtraction
        '''
        v = Vector(self._x - other._x,self._y - other._y,self._z - other._z)
        return v
    
    def __mul__(self,other):
        '''
        Operator Overloading for Scalar Multiplication of Vector

        Args:
            other (float): Scalar number to multiply

        Returns:
            Vector: Vector obtained after scalar multiplication
        '''
        v = Vector(self._x * other, self._y * other, self._z * other)
        return v
    
    def __truediv__(self,other):
        '''
        Operator Overloading for Scalar Division of Vector

        Args:
            other (float): Scalar number to divide

        Returns:
            Vector: Vector obtained after scalar division
        '''
        if(other != 0):
            v = Vector(self._x / other, self._y / other, self._z / other)
        else:
            v = Vector(0,0,0)
        return v
    
    #Dot Product
    def __pow__(self,other):
        '''
        Operator Overloading for Vector Dot Product

        Args:
            other (Vector): Vector to dot product with

        Returns:
            float: Result of Dot Product
        '''
        v = (self._x * other._x) + (self._y * other._y) + (self._z * other._z)
        return v

    #Print
    def Print(self):
        '''
        Function to Print Vector
        '''
        print("(",self._x,",",self._y,",",self._z,")")
    

class Particle:
    '''
    Particle Class with attributes 
    Mass, Charge, Position(Vector) & Velocity(Vector)
    '''
    def __init__(self,m,q,r,v):
        '''
        Initialisation funtion for 'Mass', 'Charge', 'Position' and 'Velocity'

        Args:
            m (float): Mass of Particle
            q (float): Charge of Particle
            r (Vector): Position of Particle
            v (Vector): Velocity of Particle
        '''
        self._m = m
        self._q = q
        self._r = r
        self._v = v
    
    #Accessor Functions
    def M(self):
        '''
        Accessor Function for Mass of Particle

        Returns:
            float: Mass of Particle
        '''
        return self._m
    
    def Q(self):
        '''
        Accessor Function for Charge of Particle

        Returns:
            float: Charge of Particle
        '''
        return self._q

    def R(self):
        '''
        Accessor Function for Position Vector of Particle

        Returns:
            Vector: Position of Particle
        '''
        return self._r

    def V(self):
        '''
        Accessor Function for Velocity Vector of Particle

        Returns:
            Vector: Velocity of Particle
        '''
        return self._v
    
    #Manipulator Functions
    def NewM(self, new_m):
        '''
        Manipulator Function for Mass of Particle

        Args:
            new_m (float): New Mass of Particle
        '''
        self._m = new_m
    
    def NewQ(self, new_q):
        '''
        Manipulator Function for Charge of Particle

        Args:
            new_q (float): New Charge of Particle
        '''
        self._q = new_q
    
    def NewR(self, new_r):
        '''
        Manipulator Function for Position Vector of Particle

        Args:
            new_r (Vector): New Position of Particle
        '''
        self._r = new_r
    
    def NewV(self, new_v):
        '''
        Manipulator Function for Velocity Vector of Particle

        Args:
            new_v (Vector): New Velocity of Particle
        '''
        self._v = new_v

    #Print
    def Print(self):
        '''
        Funtion to print all attributes of the Particle
        '''
        print(self._m," ",self._q," (",self._r._x,",",self._r._y,",",self._r._z,") (",self._v._x,",",self._v._y,",",self._v._z,")")


class Simulation_Engine(ABC):
    '''
    Simulation Engine Class with Force Vector and Virtual Functions
    '''
    def __init__(self):
        '''
        Initialise Force Vector and set it to '0'
        '''
        self.Force = Vector(0,0,0)

    @abstractmethod
    def run(self):
        '''
        Virtual Function for run()
        '''
        pass
    
    @abstractmethod
    def force(self):
        '''
        Virtual Function for force()
        '''
        pass
    

class GravitySim(Simulation_Engine):
    '''
    Gravity Simulator Engine inherited from Simulation_Engine
    '''
    _G = constants.gravitational_constant #6.6743e-11 # SI Units
    d_r = Vector(0,0,0)
    d_v = Vector(0,0,0)

    def force(self,p1,p2):
        '''
        Calculates the force between 2 particles and adds it to the Force Vector

        Args:
            p1 (Particle): Particle 1
            p2 (Particle): Particle 2
        '''
        self.Force += (p2.R()-p1.R()) * (self._G*p1.M()*p2.M())/(((p1.R()-p2.R())**(p1.R()-p2.R()))**(3/2))

    def run(self,p,time_step):
        '''
        Updates the position and velocity of the particle due to 
        the Net force acting on it

        Args:
            p (Particle): Particle
            time_step (float): Time Step used for time Discretisation
        
        Returns:
            Particle: Updated Particle
        '''
        z = Vector(0,0,0)
        p_f = Particle(0,0,z,z)
        d_r = p.V() * time_step + (self.Force * (time_step**2))/(2*p.M())
        d_v = (self.Force * time_step)/p.M()
        p_f.NewM(p.M())
        p_f.NewQ(p.Q())
        p_f.NewR(p.R() + d_r)
        p_f.NewV(p.V() + d_v)
        return p_f


class ElectroStaticSim(Simulation_Engine):
    '''
    ElectroStatic Force Simulator Engine inherited from Simulation_Engine
    '''
    _K = 1 / (4 * constants.pi * constants.epsilon_0) #8.99e9 # SI Units
    d_r = Vector(0,0,0)
    d_v = Vector(0,0,0)

    def force(self,p1,p2):
        '''
        Calculates the force between 2 particles and adds it to the Force Vector

        Args:
            p1 (Particle): Particle 1
            p2 (Particle): Particle 2
        '''
        self.Force += (p2.R()-p1.R()) * (self._K*p1.Q()*p2.Q())/(((p1.R()-p2.R())**(p1.R()-p2.R()))**(3/2))

    def run(self,p,time_step):
        '''
        Updates the position and velocity of the particle due to 
        the Net force acting on it

        Args:
            p (Particle): Particle
            time_step (float): Time Step used for time Discretisation
        
        Returns:
            Particle: Updated Particle
        '''
        z = Vector(0,0,0)
        p_f = Particle(0,0,z,z)
        d_r = p.V() * time_step + (self.Force * (time_step**2))/(2*p.M())
        d_v = (self.Force * time_step)/p.M()
        p_f.NewM(p.M())
        p_f.NewQ(p.Q())
        p_f.NewR(p.R() + d_r)
        p_f.NewV(p.V() + d_v)
        return p_f
    

def Simulator(time_step, t_final, Engine, filepath):
    '''
    Simulator for Multi-Body Evolution due to Gravity/Electrostatic Force given Mass, Charge, Position, and Velocity

    Args:
        time_step (int): Steps size of discretising time: Force considered constant during this period and Output given at each time step
        t_final (int): Time till which system is made to evolve
        Engine (GravitySim or ElectroStaticSim): Specify whether to simulate Gravity or Electrostatic force, taking the other to be negligible [either GravitySim() or ElectroStaticSim()]
        filepath (string): Path of code location
    '''


    n = 0
    Particles_Curr = []


    with open(filepath + 'N_Body.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            n += 1
            r = Vector(float(line[2]),float(line[3]),float(line[4]))
            v = Vector(float(line[5]),float(line[6]),float(line[7]))
            p = Particle(float(line[0]),float(line[1]),r,v)
            Particles_Curr.append(p)


    Particles_New = Particles_Curr[:]
    steps = int(t_final / time_step)
        

    #Print Particles t=0 Position
    for j in range(0,n,1):
        file_name = filepath + 'Output\\Evolution_' + str(j) +'.csv'
        with open(file_name, 'w', newline='') as new_csv:
            csv_writer = csv.writer(new_csv)
            row = [0,Particles_Curr[j].R().X(),Particles_Curr[j].R().Y(),Particles_Curr[j].R().Z()]
            csv_writer.writerow(row)


    #Calculate at every discrete time interval
    for t in range(0,steps,1):

        #Calculate for every Particle
        for j in range(0,n,1):

            #Calculate Force on the Particle
            Engine.Force = Vector(0,0,0)
            for i in range(0,n,1):
                if(i != j):
                    Engine.force(Particles_Curr[j],Particles_Curr[i])

            #Find Paricles New Position and Velocity
            Particles_New[j] = Engine.run(Particles_Curr[j],time_step)

            #Print Particle's New Position
            file_name = filepath + 'Output\\Evolution_' + str(j) +'.csv'
            with open(file_name, 'a', newline='') as add_csv:
                csv_writer = csv.writer(add_csv)
                row = [t * time_step + time_step, Particles_New[j].R().X(), Particles_New[j].R().Y(), Particles_New[j].R().Z()]
                csv_writer.writerow(row)

        #Update Particle
        Particles_Curr = Particles_New
