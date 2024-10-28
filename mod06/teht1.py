# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random


def noppa():
    s = random.randint(1,6)
    if s == 6:
        print(f"{s}")
    else:
       while s != 6:
           s = random.randint(1,6)
           print(f"{s}")
    return

noppa()