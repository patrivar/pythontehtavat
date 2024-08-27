#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

t = int(input("Anna tuumamäärä: "))
while t >= 0:
    cm = t * 2.54
    print(f"{t}tuumaa on {cm:.2f} senttimetriä.")
    if t >= 0:
        t = int(input("Anna tuumamäärä: "))
else:
    print("Ohjelma lopetettu")