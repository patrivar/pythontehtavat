# Monikko ()
'''
print("\nMonikko ()\n")

# Monikko (tuple) on "kuin lista jota ei voi muokata

minun_lista = [1, 2, 3, 4, 5, 6]
print(minun_lista)

minun_monikko = (1, 2, 3, 4, 5, 6)
print(minun_monikko)

minun_monikko2 = (1, 2, (3, 4), 5, "kuusi")
print(minun_monikko2)

# Luetaan ensimmäinen alkio
print(minun_lista[0])
print(minun_monikko[0])

# Yritetään nyt muokata eka alkio numeroksi 0 ja lisätään lopuksi 7
# Listan sisältöä voi muokata, "mutable"

minun_lista[0] = 0
print(f"muokattu lista {minun_lista}")

minun_lista.append(7)
print(f"muokattu lista {minun_lista}")

# Monikon sisältö ei voi muokata, eli "immutable"
'''
'''
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''

# Monikon läpikäynti samalla tavalla kuin listan

minun_monikko3 = ("eka", "toka", "kolmas", "neljäs", "viides")

for i in minun_monikko3:
    print(i)

hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka}, {kolmas}.")

print ("\n Monikon voi antaa funktiolle parametrina: \n")


sanalista = ("eka", "toka", "kolmas", "neljäs", "viides")
def tulosta_monikko(sanalista):
    for i in sanalista:
        print(i)

tulosta_monikko(sanalista)
tulosta_monikko(hedelmät)

#############

import random

def heitä():
    (eka, toka) = random.randint(1,6), random.randint(1,6)
    return (eka, toka)

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

# Heitetään uudet

def heitä2():
    (eka, toka) = random.randint(1,6), random.randint(1,6)
    return (eka, toka)

noppa1, noppa2 = heitä2()
print(f"Nopista tuli {noppa1} ja {noppa2}.")