from random import random
from random import seed
from math import sqrt

def main():
    N = int(input("n:"))
    Seed = int(input("seed:"))
    seed(Seed)
    M = 0
    for i in range(1,N+1):
        x = random()
        y = random()
        # print(str(x) + " " + str(y))
        if (x*x + y*y <= 1):
            M += 1

    pi = 4*M/N
    print("pi: " + str(pi))
    print("statistical error: " + str(pi/sqrt(N)))

main()
