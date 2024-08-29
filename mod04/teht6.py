#π≈4n/N, jos N on kaikkien pisteiden lukumäräärä ja
# n yksikköympyrän sisälle osuvien pisteiden määrä
#jos pisteen kordinaatit toteutuvat epäyhtälön x^2+y^2<1, piste on ympyrässä.

import random


N = int(input("Anna pisteiden lukumäärä: ")) #pisteiden kokonaismäärä
n = 0 # Ympyrään osuvien pisteiden lukumäärä
iterator = 0

while iterator < N:
    iterator += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")
    #print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Piste on yksikköympyrässä")
        if x**2 + y**2 < 1 == True:
            n = n + 1
            print(f"Näin monta pistettä {n} osui ympyrän sisälle")
        if iterator == N:
            pi = 4*n/N
            print(f"Likiarvo on {pi}")
