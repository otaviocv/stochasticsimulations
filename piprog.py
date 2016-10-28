from random import random
from random import uniform
from random import seed
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

def main():
    N = int(input("n:"))
    s = int(input("seed:"))
    e = float(input("epsilon:"))
    seed(s)
    M = 0
    points = []

    for i in range(1,N):
        x = uniform(-1,1)
        y = uniform(-1,1)
        if (x*x + y*y <= 1):
            M += 1
        points.append(4*M/i)
    print(4*M/N)

    # Pontos convergindo
    # plt.axis([0, N, np.pi - e, np.pi + e])
    # plt.plot(points)
    # t = np.arange(0, N, 1)
    # plt.plot(t, t-t+np.pi, 'r--')
    # plt.show()

    # Histograma
    upperLimit = 3.13
    boundLimit = 3.143

    mu = np.mean(points)
    sigma = np.std(points)
    print(mu)
    print(sigma)
    num_bins = 10000
    n, bins, patches = plt.hist(points, num_bins, normed=1, alpha=0.5)
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')

    plt.axis([upperLimit, boundLimit, 0 ,1000])
    # t = np.linspace(upperLimit, boundLimit, 100)
    # bins = np.linspace(upperLimit, boundLimit, 100)
    # plt.plot(t,mlab.normpdf(t, mu, sigma))
    plt.show()

    # the histogram of the data
    # add a 'best fit' line

main()
