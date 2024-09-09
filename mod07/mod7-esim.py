#Monikko ()
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

############################################################################################################

print("\nJOUKKO eli set {} \n")

# Joukko (set) on järjestämätön tietorakenne, eli  sen alkiot voivat olla missä tahansa järjestyksessä
# Koska joukon alkioille ei ole määritelty järjstystä, ei alkioihin voi myöskään viitata indeksillä
# Toisin kuin listassa tai monikossa, sama alkio voi esiintyä jukossa vain kertaalleen, eli jopppukossa
# ei voi olla kahta samansisältöistä alkiota

#joukko eli set
joukko = {1, 2, 3, 4, 5, 6,}
#joukko merkataan aaltosulkeilla
print(joukko)

print(f"Numero 6 voi esiintyä listassa useasti")
minun_lista = [6, 2, 3, 4, 5, 6]
print(minun_lista)

print(f"Numero 6 voi esiintyä listassa useasti")
minun_monikko = [6, 2, 3, 4, 5, 6]
print(minun_monikko)

print(f"Numero 6 EI voi esiintyä listassa useasti")
minun_joukko = {6, 2, 3, 4, 5, 6}
print(minun_joukko)

# Yllä oleva ei sinänsä tuota virhettä, kuten ei add-metodi

minun_joukko.add(7)
print(minun_joukko)
minun_joukko.remove(7)
print(minun_joukko)

##############################################################################################################

pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

# alkiot iteroiidaan läpi for/in rakenteella

for p in pelit:
    print(p)
    # löytyykö cluedo, jos röytyy, printtaa jotain
    if p == "Cluedo":
        print("Onhan se cluedo siellä!")

# if / in haku toimii samalla tavalla kuin listoissa

if "Monopoli" in pelit:
    print("On se Monokin siellä")

##############################################################################################################

autolista = []
autolista.append("Audi")
print(autolista)

#Tästä tuleekin sanakirja eli dictionary
autojoukko = {}
print(type(autojoukko)) # <class 'dict'>

#tyhjä joukko luodaan edellä esitetystä oiketen set-funktion avulla.
autojoukko = set()
autojoukko.add("Audi")
print(type(autojoukko)) #tämä on <class 'set'>
print(autojoukko)

################################################################################################################

print("\n SANAKIRJA {} \n")

# Sanakirja (dictionary) on Pythonin käytetyimpiä tietorakenteita.
# Sanakijaan voidaan tallentaa avain-arvopareja.

oppilaat = {"Aapeli": 25, "Bertta": 31, "Lucy":22, "Liiru": 5, "Minni": 23}
print(oppilaat)

# mitä ovat tietueet / item?
print(oppilaat.items()) #ilmoittaa kaikki tietuet erillisissä suluissa

# mitä ovat avaimet sanakirjassa?
print(oppilaat.keys()) #antaa avaimet eli tässä tapauksessa nimet

# mitä ovat arvoja sanakirjassa?
print(oppilaat.values()) #antaa arvot eli tässä tapauksessa iät eli numerot

# kun sanakirjaa käydään läpi for/in rakennetta käyttäen,
# saa kierrosmuuttuja arvokseen vuoron perään kunkin sanakirjassa esiintyvän avaimen
'''
# tietueet eli avain-arvoparit
for i in oppilaat:
    print(i)

print(oppilaat["Lucy"]) # antaa "avaimeen" liitetyn "arvon" tässä tapauksessa lucyyn liitetyn numeron("Lucy":22)

avain="Lucy"
print(oppilaat[avain]) # nämä 2 tapaa ovat molemmat oikein mutta alemmpi tarvitsee 2 koodiriviä 1 sijaan
'''
# etsi kaikki arvot
for i in oppilaat:
    print(i)

# if / in rakenteella voidaan myös hakea sanakirjasta tietoa
nimi = input("Anna nimi, niin etsin sen sanakirjasta: ")
if nimi in oppilaat:
    print(f"Oppilas {nimi} löytyi ja hänen ikänsä on {oppilaat[nimi]}.")

# Kun olemassa olevaan sankirjaan lisätän arvo,
# käytetään notaatiota sanakirja[avain] = arvo

# lisätään uusi oppilas mikäli ei löydy
# jos avain löytyy, se muokkaa olemassa olevaa, muuten luodaan uusi
oppilaat["Ulla"] = 24
print(oppilaat)

