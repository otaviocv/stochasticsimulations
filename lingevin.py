import numpy as np
from numpy.random import normal
import math
import matplotlib.pyplot as plt

def main():
    tau =  0.01
    n = int(input("n:"))
    gamma = [1,2,3,4]
    v = [0,0,0,0]
    velocities = [[0],[0],[0],[0]]
    csi = normal(0,1)

    for i in range(0,n):
        v[0] = v[0] -tau*v[0] + math.sqrt(tau*gamma[0])*csi
        csi = normal(0,1)
        v[1] = v[1] -tau*v[1] + math.sqrt(tau*gamma[1])*csi
        csi = normal(0,1)
        v[2] = v[2] -tau*v[2] + math.sqrt(tau*gamma[2])*csi
        csi = normal(0,1)
        v[3] = v[3] -tau*v[3] + math.sqrt(tau*gamma[3])*csi
        csi = normal(0,1)
        velocities[0].append(v[0])
        velocities[1].append(v[1])
        velocities[2].append(v[2])
        velocities[3].append(v[3])
        print(v)

    print(velocities)
    plt.plot(velocities[0])
    plt.plot(velocities[1])
    plt.plot(velocities[2])
    plt.plot(velocities[3])
    plt.show()
    plt.hist(velocities[0], alpha=0.5)
    plt.hist(velocities[1], alpha=0.5)
    plt.hist(velocities[2], alpha=0.5)
    plt.hist(velocities[3], alpha=0.5)
    plt.show()

main()
