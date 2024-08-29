#π≈4n/N, jos N on kaikkien pisteiden lukumäräärä ja
# n yksikköympyrän sisälle osuvien pisteiden määrä
#jos pisteen kordinaatit toteutuvat epäyhtälön x^2+y^2<1, piste on ympyrässä.

import random

#TODO: kysy N arvo käyttäjälle

N = int(input("Anna pisteiden lukumäärä")) #pisteiden kokonaismäärä
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

#TODO: lisää n arvoon 1
#TODO: Tulosta kaavan mukaan laskettu piin likiarvo