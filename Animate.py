import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.animation import FuncAnimation, writers
from matplotlib import animation
import csv

n = 9


steps = 0

x = []
y = []


#Read Position Data as Input
for i in range(n):
    file_name = 'Output\Evolution_' + str(i) + '.csv'

    with open(file_name,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            for line in csv_reader:
                x.append(float(line[1]))
                y.append(float(line[2]))
                if(i == 0): 
                    steps += 1


xdata = []
ydata = []
#x_1data = []
#y_1data = []


#Set Plot Details
plt.ylabel('Y Distance (m)')
plt.xlabel('X Distance (m)')
#plt.xlim(-3e11, 3e11)
#plt.ylim(-3e11, 3e11)
plt.xlim(-1e12, 4.75e12)
plt.ylim(-1e12, 3e12)
plt.title('Solar System Evolution')

colour = ['r','g','b','m','c','y','k']

#Animate the Plot
def animate(i):
    for j in range(n):
        clr = j%7
        xdata = []
        ydata = []
        for k in range(i+1):
            xdata.append(x[j*steps + k*1000])
            ydata.append(y[j*steps + k*1000])
        plt.plot(xdata, ydata, color=colour[clr])

ani = FuncAnimation(plt.gcf(),animate, interval =100, frames = 157, repeat = False)

#Export & Save Video
f = "Video.mp4" 
writervideo = animation.FFMpegWriter(fps=60) 
ani.save(f, writer=writervideo)


plt.show()
