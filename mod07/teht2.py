# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen
# mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
# allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

k = input("Anna nimi: ")
j = set({})

while k != "":
    if k in j:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        j.add(k)
    k = input("Anna nimi: ")

for i in j:
    print(i)