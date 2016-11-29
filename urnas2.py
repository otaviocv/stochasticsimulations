from random import randint
from random import uniform
import matplotlib.pyplot as plt

def bernoulli(p):
    teste = uniform(0,1)
    if teste <= p:
        return True
    return False

def main():
    # As bolas na urna A são denotadas com 0 e as bolas na urna B são denotadas
    # com 1
    totalBolas = 100
    totalPassos = 1000000
    bolas = [0]*50 + [1]*50
    n = [totalBolas/2, totalBolas/2]
    q = float(input("q:"))
    media = [0]*totalPassos
    media[0] += totalBolas/2

    for t in range(0,totalPassos):
        troca = randint(0,totalBolas -1)
        if n[bolas[troca]] <= totalBolas/2:
            if bernoulli(q):
                bolas[troca] = 1 - bolas[troca]
                if bolas[troca] == 0:
                    n[0] += 1
                    n[1] -= 1
                else:
                    n[1] += 1
                    n[0] -= 1
        else:
            if bernoulli(1-q):
                bolas[troca] = 1 - bolas[troca]
                if bolas[troca] == 0:
                    n[0] += 1
                    n[1] -= 1
                else:
                    n[1] += 1
                    n[0] -= 1
        media[t] = n[0]/totalBolas


    plt.hist(media[100000:])
    plt.axis([0,1,0,600000])
    plt.show()




main()
