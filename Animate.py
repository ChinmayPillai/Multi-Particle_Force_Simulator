import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.animation import FuncAnimation, writers
from matplotlib import animation
import csv

x_0 = []
y_0 = []
x_1 = []
y_1 = []

#Read Position Data as Input
with open('Output\Evolution_0.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader:
            x_0.append(float(line[1]))
            y_0.append(float(line[2]))
            
with open('Output\Evolution_1.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader:
            x_1.append(float(line[1]))
            y_1.append(float(line[2]))


x_0data = []
y_0data = []
x_1data = []
y_1data = []


#Set Plot Details
plt.ylabel('Y Distance (10^8 km)')
plt.xlabel('X Distance (10^8 km)')
plt.xlim(-1.6e11, 1.6e11)
plt.ylim(-1.6e11, 1.6e11)
plt.title('Earth-Sun System Evolution')


#Animate the Plot
def animate(i):
    x_0data.append(x_0[i*100])
    y_0data.append(y_0[i*100])
    x_1data.append(x_1[i*100])
    y_1data.append(y_1[i*100])
    plt.plot(x_0data, y_0data, color='r')
    plt.plot(x_1data, y_1data, color='g')

ani = FuncAnimation(plt.gcf(),animate, interval = 1, frames = 316, repeat = False)

#Export & Save Video
f = "Video.mp4" 
writervideo = animation.FFMpegWriter(fps=60) 
ani.save(f, writer=writervideo)


plt.show()
