# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki
# parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
# sen jälkeen sekä alkuperäisen että karsitun listan.

l = []


for i in range(30):
    l.append(i+1)


def par(lista):
    l2 = []
    for o in lista:
        if o % 2 == 0:
            l2.append(o)
    return l2


print(l)
print(par(l))