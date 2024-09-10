# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan
# hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma
# kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen
# rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua
# funktiota.


import math

k1 = int(input("Anna ensimmäisen pyöreän pizzan halkaisija(cm): "))
h1 = int(input("Anna ensimmäisen pizzan hinta: "))
k2 = int(input("Anna toisen pyöreän pizzan halkaisija(cm): "))
h2 = int(input("Anna toisen pizzan hinta: "))

def hin ():
    arvot1 = h1 / (math.pi * (((k1 / 2) / 100) ** 2))
    arvot2 = h2 / (math.pi * (((k2 / 2) / 100) ** 2))
    return arvot1, arvot2

arvot1, arvot2 = hin ()

if arvot1 < arvot2:
    print(f"Ensimmäinen pizza antaa paremman vastineen rahalle hinnalla {arvot1:.2f}euroa per neliö")
else:
    print(f"Toinen pizza antaa paremman vastineen rahalle hinnalla {arvot2:.2f}euroa per neliö")

