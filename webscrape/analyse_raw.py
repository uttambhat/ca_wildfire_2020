import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#inputfilename = 'Santa_Cruz_County_raw.txt'
#inputfilename = 'Santa_Clara_County_raw.txt'
#inputfilename = 'Yolo_County_raw.txt'
#inputfilename = 'Mendocino_County_raw_2.txt'
inputfilename = 'Mendocino_county_raw_2018.txt'
inputfile = open(inputfilename, 'r')
line = inputfile.readlines()
date,revisiondate,acreage,contained=[],[],[],[]
for i in range(len(line)):
    if(line[i][0]=='t'):
        start=line[i].find(">") + len(">")
        end=line[i].find("<")
        acreage.append(float((line[i][start:end]).replace(',','')))
    elif(line[i][0]=='<'):
        start=line[i].find(">") + len(">")
        end=line[i].find("%")
        contained.append(float((line[i][start:end]).replace(',','')))
    elif(line[i][0]=='A'):
        start=line[i].find(" ") + len(" ")
        end=line[i].find("<")
        date.append(float((line[i][start:end]).replace(',','')))
    elif(line[i][0]=='R'):
        hr=int(line[i][15:17])
        mn=int(line[i][18:20])
        day=int(line[i][22:24])
        mon=line[i][25:28]
        if(mon=='Jul'):
            day=day-31 
        
        daysinceaug0=float(day)+float(hr)/24.+float(mn)/(24.*60.)
        revisiondate.append(daysinceaug0)
    

n=len(date)
date=np.array(date)
acreage=np.array(acreage)
contained=np.array(contained)
revisiondate=np.array(revisiondate)

#date_for_plot=date
date_for_plot=revisiondate[-len(acreage):]

mendocino2020=np.loadtxt("/home/uttam/Dropbox/c/wildfire/cleaned_timeseries/Mendocino_County_2020_fire_timeseries.txt")

plt.plot(date_for_plot-date_for_plot[0],contained*acreage/100.,'-o',label="Contained area")
plt.plot(date_for_plot-date_for_plot[0],acreage,'-o',label="Total fire area")
plt.plot(mendocino2020[:,0]-mendocino2020[0,0],mendocino2020[:,1]*mendocino2020[:,2]/100.,'-o',label="Contained area 2020")
plt.plot(mendocino2020[:,0]-mendocino2020[0,0],mendocino2020[:,1],'-o',label="Total fire area 2020")
plt.legend()
plt.xlabel("Number of days from start of fire)")
plt.ylabel("Acres")
plt.title(inputfilename[:-12].replace('_',' '))
plt.show()

date=date.reshape(n,-1)
acreage=acreage.reshape(n,-1)
contained=contained.reshape(n,-1)
#np.savetxt(inputfilename[:-8]+"_2020_fire_timeseries.txt",np.concatenate((date,acreage,contained),axis=1).astype(int),fmt='%i')

