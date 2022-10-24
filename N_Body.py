from abc import ABC, abstractmethod
import csv


class Vector:

    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z
    
    #Accessor Functions
    def X(self):
        return self._x

    def Y(self):
        return self._y

    def Z(self):
        return self._z

    #Manipulator Functions
    def NewX(self, new_x):
        self._x = new_x
    
    def NewY(self, new_y):
        self._y = new_y
    
    def NewZ(self, new_z):
        self._z = new_z
    
    #Operator Overloading
    def __add__(self,other):
        v = Vector(self._x + other._x, self._y + other._y, self._z + other._z)
        return v

    def __iadd__(self,other):
        self = self + other
        return self

    def __sub__(self,other):
        v = Vector(self._x - other._x,self._y - other._y,self._z - other._z)
        return v
    
    def __mul__(self,other):
        v = Vector(self._x * other, self._y * other, self._z * other)
        return v
    
    def __truediv__(self,other):
        v = Vector(self._x / other, self._y / other, self._z / other)
        return v
    
    #Dot Product
    def __pow__(self,other):
        v = (self._x * other._x) + (self._y * other._y) + (self._z * other._z)
        return v

    #Print
    def Print(self):
        print("(",self._x,",",self._y,",",self._z,")")
    

class Particle:
    
    def __init__(self,m,q,r,v):
        self._m = m
        self._q = q
        self._r = r
        self._v = v
    
    #Accessor Functions
    def M(self):
        return self._m
    
    def Q(self):
        return self._q

    def R(self):
        return self._r

    def V(self):
        return self._v
    
    #Manipulator Functions
    def NewM(self, new_m):
        self._m = new_m
    
    def NewQ(self, new_q):
        self._q = new_q
    
    def NewR(self, new_r):
        self._r = new_r
    
    def NewV(self, new_v):
        self._v = new_v

    #Print
    def Print(self):
        print(self._m," ",self._q," (",self._r._x,",",self._r._y,",",self._r._z,") (",self._v._x,",",self._v._y,",",self._v._z,")")


class Simulation_Engine(ABC):
    
    def __init__(self):
        self.Force = Vector(0,0,0)

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def force(self):
        pass
    

class GravitySim(Simulation_Engine):

    _G = 6.6743e-11 # SI Units
    d_r = Vector(0,0,0)
    d_v = Vector(0,0,0)

    def force(self,p1,p2):
        self.Force += (p2.R()-p1.R()) * (self._G*p1.M()*p2.M())/(((p1.R()-p2.R())**(p1.R()-p2.R()))**(3/2))

    def run(self,p,time_step):
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

    _K = 8.99e9 # SI Units
    d_r = Vector(0,0,0)
    d_v = Vector(0,0,0)

    def force(self,p1,p2):
        self.Force += (p2.R()-p1.R()) * (self._K*p1.Q()*p2.Q())/(((p1.R()-p2.R())**(p1.R()-p2.R()))**(3/2))

    def run(self,p,time_step):
        z = Vector(0,0,0)
        p_f = Particle(0,0,z,z)
        d_r = p.V() * time_step + (self.Force * (time_step**2))/(2*p.M())
        d_v = (self.Force * time_step)/p.M()
        p_f.NewM(p.M())
        p_f.NewQ(p.Q())
        p_f.NewR(p.R() + d_r)
        p_f.NewV(p.V() + d_v)
        return p_f
    

n = 0
Particles_Curr = []

with open('N_Body.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        n += 1
        r = Vector(float(line[2]),float(line[3]),float(line[4]))
        v = Vector(float(line[5]),float(line[6]),float(line[7]))
        p = Particle(float(line[0]),float(line[1]),r,v)
        Particles_Curr.append(p)


Particles_New = Particles_Curr[:]
Engine = GravitySim()

time_step = 1000
t_final = 86400*365
steps = int(t_final / time_step)
      

#Print Particles t=0 Position
for j in range(0,n,1):
    file_name = 'Output\Evolution_' + str(j) +'.csv'
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
        file_name = 'Output\Evolution_' + str(j) +'.csv'
        with open(file_name, 'a', newline='') as add_csv:
            csv_writer = csv.writer(add_csv)
            row = [t * time_step + time_step, Particles_New[j].R().X(), Particles_New[j].R().Y(), Particles_New[j].R().Z()]
            csv_writer.writerow(row)

    #Update Particle
    Particles_Curr = Particles_New
