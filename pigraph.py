from random import random
from random import uniform
from random import seed
import matplotlib.pyplot as plt
import numpy as np

def main():
    N = int(input("n:"))
    Seed = int(input("seed:"))
    seed(Seed)
    M = 0
    outP = [[],[]]
    inP = [[],[]]
    points = []

    for i in range(1,N+1):
        x = uniform(-1,1)
        y = uniform(-1,1)
        if (x*x + y*y <= 1):
            M += 1
            inP[0].append(x)
            inP[1].append(y)
        else:
            outP[0].append(x)
            outP[1].append(y)
        points.append(4*M/i)
        print(4*M/i)


    print(4*M/N)

    fig, ax = plt.subplots(num=None, figsize=(8, 8), dpi=80, facecolor='w',
            edgecolor='none')

    plt.scatter(inP[0], inP[1], c='red', marker=',', s=1, edgecolors='none')
    plt.scatter(outP[0], outP[1], c='blue', marker=',', s=1, edgecolors='none')

    axes = plt.gca()
    axes.set_xlim([-1,1])
    axes.set_ylim([-1,1])

    plt.show()

    fig2, ax2 = plt.subplots(num=None, figsize=(8, 8), dpi=80, facecolor='w',
            edgecolor='none')

    plt.plot(points)
    t = np.arange(0, N, 1)
    plt.plot(t, t-t+np.pi, 'r--')
    plt.axis([0, N, 3, 3.2])
    plt.show()


main()
