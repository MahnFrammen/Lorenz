#Zach Pedersen, Rylan Casanova
#This is our work
#Prof. Citro
#CST-305

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
import math

# number of points
r = 15
# start conditions
arrivals = np.linspace(1, r, r)
duration = [2.22, 1.76, 2.13, 0.14, 0.76,
            0.70, 0.47, 0.22, 0.18, 2.41,
            0.41, 0.46, 1.37, 0.27, 0.27]

# Calculates Service Start Time
service = 0

serv = []
for i in range(0, len(arrivals)):
    if (arrivals[i] > service):
        service = arrivals[i]

    rtrn = round(service, 2)
    service += duration[i]
    serv.append(rtrn)

# Plot results (Service Start Time)
plt.title('Service Start Time')
plt.plot(arrivals, serv)
plt.xlabel('Arrival Time')
plt.ylabel('SST')
plt.show()

print(serv)

# Calculates exit time
exit = []
for i in range(0, len(arrivals)):
    exit.append(round(serv[i] + duration[i], 2))

# Plot results (Exit Time)
plt.title('Exit Time')
plt.plot(arrivals, exit)
plt.xlabel('Arrival Time')
plt.ylabel('Exit Time')
plt.show()

print(exit)

# Calculates time in queue
queue = []
for i in range(0, len(arrivals)):
    queue.append(round(serv[i] - arrivals[i], 2))

# Plot results (Exit Time)
plt.title('Queue Time')
plt.plot(arrivals, queue)
plt.xlabel('Arrival Time')
plt.ylabel('Queue Time')
plt.show()

print(queue)

# Calculates number in system
system = []
for i in range(0, len(arrivals)):
    total = 0
    for j in range(0, i + 1):
        if (exit[j] > arrivals[i]):
            total += 1
    system.append(total)

# Plot results (# in System)
plt.title('Number in System')
plt.plot(arrivals, system)
plt.xlabel('Arrival Time')
plt.ylabel('# in System')
plt.show()

print(system)

# Calculates number in queue
queue = []
for i in range(0, len(arrivals)):
    queue.append(system[i] - 1)

# Plot results (# in Queue)
plt.title('Number in Queue')
plt.plot(arrivals, queue)
plt.xlabel('Arrival Time')
plt.ylabel('# in Queue')
plt.show()

print(queue)
