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
print(f"Hei {nimet[3]}, ikäsi on {iat[3]} vuotta.")
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

