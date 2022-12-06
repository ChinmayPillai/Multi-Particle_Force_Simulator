'''
Find Time Period of Orbits of Particles from CSV File
'''

import csv
import numpy as np


def TimePeriod(n,filepath):
    '''
    Code to find the time period of revolution of every particle

    Args:
        n (int): Number of Particles
        filepath (string): Path of code location
    '''


    print("Time Period of Revolution of Body:\n")

    for j in range(0,n,1):
        file_name = filepath + 'Output\\Evolution_' + str(j) +'.csv'
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            start = False
            switchTime = []
            timeP = []
            timePeriod = 0
            prev = 0

            for line in csv_reader:
                
                curr = np.sign(float(line[1]))

                if(not start):
                    prev = curr
                    start = True
                else:
                    if (curr != prev):
                        switchTime.append(float(line[0]))
                        prev = curr
            
        length = len(switchTime)

        if(length <= 1):
            print(f"{j} = Not enough Information\n")
            #print("------------------------------------------------\n")
            continue
        elif(length == 2):
            print("Aprroximation")
            timePeriod = 2 * (switchTime[1]-switchTime[0]) / (60*60*24)
        else:
            for i in range(length-2):
                timeP.append(switchTime[i+2]-switchTime[i])
                #print((switchTime[i+2]-switchTime[i])/(60*60*24), end=", ")
            timePeriod = sum(timeP)/len(timeP)
            timePeriod = timePeriod / (60*60*24)

        print(f"{j} = {timePeriod} Days\n")
        #print("------------------------------------------------\n")    
 
