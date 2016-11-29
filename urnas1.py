from random import randint
import matplotlib.pyplot as plt

def main():
    # As bolas na urna A são denotadas com 0 e as bolas na urna B são denotadas
    # com 1
    totalPassos = 1000
    totalCorridas = 100
    totalBolas = 100
    bolas = [0]*totalBolas
    media = [0]*totalPassos

    for corridas in range(0,totalCorridas):
        n = 100
        bolas = [0]*totalBolas
        print("Corrida %d" % corridas)
        media[0] += n/totalCorridas
        for t in range(1,totalPassos):
            troca = randint(0,totalBolas - 1)
            bolas[troca] = 1 - bolas[troca]
            if bolas[troca] == 0:
                n += 1
            else:
                n -= 1
            media[t] += n/totalCorridas

    plt.plot(media)
    plt.axis([0,totalPassos,0,totalBolas])
    plt.show()

main()
