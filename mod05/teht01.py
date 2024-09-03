# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.


import random



A = int(input("Anna arpakuutioiden lukumäärä: "))
k = 0
luvut = []
total = 0
while k < A:
    k += 1
    luvut.append(random.randint(1,6))

for i in range(len(luvut)):
    total = total + luvut[i]
print(total)
