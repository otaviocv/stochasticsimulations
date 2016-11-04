import numpy as np
from numpy.random import normal
import math
import matplotlib.pyplot as plt

def main():
    tau =  0.01
    n = int(input("n:"))
    gamma = [1,5,10,20]
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
        # print(v)

    correlacao = [[],[],[],[]]
    for i in range(0, n//2):
        means = [0,0,0,0]
        for j in range(0, n-i):
            means[0] += velocities[0][j]*velocities[0][j+i]/(n-i)
            means[1] += velocities[1][j]*velocities[1][j+i]/(n-i)
            means[2] += velocities[2][j]*velocities[2][j+i]/(n-i)
            means[3] += velocities[3][j]*velocities[3][j+i]/(n-i)
        correlacao[0].append(means[0])
        correlacao[1].append(means[1])
        correlacao[2].append(means[2])
        correlacao[3].append(means[3])

    # print(velocities)
    p1 = plt.plot(velocities[0])
    p2 = plt.plot(velocities[1])
    p3 = plt.plot(velocities[2])
    p4 = plt.plot(velocities[3])
    plt.legend((p1[0], p2[0], p3[0], p4[0]), (str(gamma[0]), str(gamma[1]),
        str(gamma[2]), str(gamma[3])))
    plt.show()
    plt.hist(velocities[3], alpha=0.5)
    plt.hist(velocities[2], alpha=0.5)
    plt.hist(velocities[1], alpha=0.5)
    plt.hist(velocities[0], alpha=0.5)
    plt.legend((p4[0], p3[0], p2[0], p1[0]), (str(gamma[0]), str(gamma[1]),
        str(gamma[2]), str(gamma[3])))
    plt.show()
    plt.plot(correlacao[0])
    plt.plot(correlacao[1])
    plt.plot(correlacao[2])
    plt.plot(correlacao[3])
    plt.legend((p1[0], p2[0], p3[0], p4[0]), (str(gamma[0]), str(gamma[1]),
        str(gamma[2]), str(gamma[3])))
    plt.show()

main()
