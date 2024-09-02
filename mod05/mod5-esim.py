'''
name1 = "Nikku"
name2 = "Cassu"
name3 = "Crisu"
age1 = 15
age2 = 23
age3 = 25
print(f"Hei {name1} sinun ikäsi on {age1} vuotta")
print(f"Hei {name2} sinun ikäsi on {age2} vuotta")
print(f"Hei {name3} sinun ikäsi on {age3} vuotta")
nimet2 = [name1, name2, name3]
'''

nimet = ["Nikku", "Cassu", "Crisu", "Lumi", "Tiku"]
iat = ["15", "23", "25", "13", "20"]

#Listan pituus voidaan tarkistaa len() funktiolla
lenght = len(nimet)
print(f"Listan pituus on: {lenght}")

'''
#Alkioon viitataan indeksinummerolls
print(f"Hei {nimet[3:4]}, ikäsi on {iat[3:4]} vuotta.")
'''

'''
#Listan läpikäynti while silmukan avulla
iterator = 0
#While 0 < 5:
#While 1 < 5:
#While 2 < 5:
#While 3 < 5:
#While 4 < 5:

while iterator < len(nimet):
    print(f"Hei {nimet[iterator]}, ikäsi on {iat[iterator]} vuotta.")
    iterator += 1
'''
'''
#nimet = ["Nikku", "Cassu", "Crisu", "Lumi", "Tiku"]
#iat = ["15", "23", "25", "13", "20"]
print(nimet[2:4]) # 2, 3 (ei viimeistä alkiota) 2 alkiota indeksistä 2 alkaen
print(nimet[2:]) # Antaa kaikki alkiot indeksilä 2 alkaen
print(nimet[-1]) # Listan viimeinen alkio
print(nimet[-2]) # Antaa alkion toiseksi viimeisen alkion
print(nimet[-1:-3:-1]) #Halutut alkiot käänteis järjestyksessä
#print(nimet[2:6:2]) # indeksistä 2 indekssiin 6, joka toinen
'''
'''
#Listaan voi yhdistää ja siellä voi olla erillaisia tietorakenteita
Lista1 = ["ulla", "Matti", "Ilkka"]
yhdistetty_lista =  [23, 54,25,100,22, Lista1]
print(yhdistetty_lista)
print(yhdistetty_lista[5][0])
'''

'''
names = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi != "":
    nimet.append(nimi)
    nimi = input("Anna seuraava nii tai lopeta painamlla Enter: ")

print(names)
'''

#nimet = ["Nikku", "Cassu", "Crisu", "Lumi", "Tiku"]

nimet.append("uusi nimi") #Lisää uuden alkion listan loppuun
print(nimet)
nimet.insert(0, "kala")
print(nimet)
print(nimet.index("Tiku"))
if "uusi nimi" in nimet:
    print("uusi nimi ja kala löytyi listasta ja nyt poistetaan ne")
    nimet.remove("uusi nimi")
    nimet.remove("kala")
    print(nimet)
print(nimet.index("Tiku"))

more_names = ("Iines", "Aku", "Roope", "Milla")
nimet.extend(more_names)
print(nimet)
#uusilista = nimet + more_names

nimet[3] = "Lumi-Helmi"
print(nimet)

nimet.sort()
print(nimet)

print("-----------------")
print("Listan läpikäynti for-toistorakenteen avulla")

names = []

for kirjain in "abcde":
    print(kirjain)

for alkio in [1,2,3,4,5]:
    print(alkio)

for nimi in nimet:
    print(nimi)

for numero in range(1, 11): #numerot alkaen 1 niin että 11 jätetään pois. eli luvut jotka ovat <11
    print(numero)
'''
for numero in range(1, 50, 2):
    print(numero)

for i in range(999,0, -3):
    print(i)
'''
#Käytetään edell olevia iteroimaan nimilistaa läpi
#for silmukka iteraatiolla

print(nimet)
for i in range(5):
    print(i)
    print(f"Terve {nimet[i]}")

listan_pituus = len(nimet)
print(nimet)
print(f"Listan pituus on {listan_pituus} alkiota pitkä.")
#for i in rnage (len(nimet)):
for i in range (listan_pituus):
    print(f"Terve {nimet[i]}")