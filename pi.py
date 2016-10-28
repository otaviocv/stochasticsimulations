from random import random
from random import seed
import numpy as np

def main():
    N = int(input("n:"))
    Seed = int(input("seed:"))
    seed(Seed)
    M = 0
    points = []
    for i in range(1,N+1):
        x = random()
        y = random()
        # print(str(x) + " " + str(y))
        if (x*x + y*y <= 1):
            M += 1
        points.append(4*M/i)



    print("pi: " + str(4*M/N))
    print("mean: " + str(np.mean(points)))
    print("std: " + str(np.std(points)))
    print("std/sqrt(n): " + str(np.std(points)/np.sqrt(N)))

main()
