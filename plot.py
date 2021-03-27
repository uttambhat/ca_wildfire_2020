import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("ca_fire_data.txt")

plt.plot(data[:,0],data[:,2])
plt.xlabel("Year")
plt.ylabel("Total area burned (acres)")
plt.show()

plt.plot(data[:,0],data[:,1])
plt.xlabel("Year")
plt.ylabel("Total number of fires")
plt.show()

plt.plot(data[:,0],data[:,2]/data[:,1])
plt.xlabel("Year")
plt.ylabel("Average fire size (acres)")
plt.show()

