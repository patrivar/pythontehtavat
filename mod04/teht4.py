# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

random = random.randint(1,10)

p = int(input("Arvaa numero väliltä 1-10: "))
while p != random:
    if p < random:
        print("Luku on liian pieni")
        p = int(input("Arvaa uudestaan: "))
    elif p > random:
        print("Luku on liian suuri")
        p = int(input("Arvaa uudestaan: "))

else:
    print("Arvasit oikein")