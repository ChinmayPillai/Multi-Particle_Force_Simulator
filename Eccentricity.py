'''
Find Eccentricity of Orbits of Particles from CSV File
'''

import csv
import numpy as np


def Eccentricity(n, filepath):
    '''
    Code to find the eccentricity of orbit of every particle

    Args:
        n (int): Number of Particles
        filepath (string): Path of code location
    '''


    print("Eccentricity of Orbit of Body:\n")

    for j in range(0,n,1):
        file_name = filepath + 'Output\\Evolution_' + str(j) +'.csv'
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            start = False
            max = -1
            min = 1e15
            prev = 0
            switch = 0

            for line in csv_reader:
                
                pt = np.array([float(line[1]), float(line[2]), float(line[3])])
                curr = np.linalg.norm(pt)
                sign = np.sign(float(line[1]))

                if(not start):
                    max = curr
                    min = curr
                    prev = sign
                    start = True
                    continue
                else:
                    if (sign != prev):
                        prev = sign
                        switch += 1

                if(switch == 1 or switch == 2):
                    if (max < curr):
                        max = curr
                    if (curr < min):
                        min = curr
                elif(switch > 2):
                    break

        if(switch < 2):
            print(f"{j}: Not Enough Information\n")
        else:
            if(switch == 2):
                print("Approximation")
            #print(f"{j}:\nMax: {max/1e10}, Min: {min/1e10}\n")
            a = (max + min) / 2
            b = np.sqrt(max * min)
            e = np.sqrt(1 - ((b/a)**2))
            print(f"{j} = {e}\n")

