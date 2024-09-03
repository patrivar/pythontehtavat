# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

k = int(input("Anna luku: "))

for i in range(2, k):
    if k % i == 0:
        print(f"Luku {k} ei ole alkuluku.")
        break

if k % i != 0 and k % k == 0:
    print(f"Luku {k} on alkuluku.")
