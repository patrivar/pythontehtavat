# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
# lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä
# suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

l = []
k = l.append(input("Anna luku: "))

while k != "":
    k = (input("Anna luku: "))
    if k != "":
        l.append(k)
else:
    l.sort(reverse=True)
    print(l[0:5])
