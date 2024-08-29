# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

V = int(input("Kerro vuosiluku: "))

if V % 400 == 0 or V % 4 == 0 and not V % 100 == 0:
    print(f"Vuosi {V} on karkausvuosi")
else:
    print(f"Vuosi {V} ei ole karkausvuosi")