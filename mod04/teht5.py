# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

t = input("Anna käyttäjä tunnus: ")
s = input("Anna salasana: ")
k = 1
while k <= 5:
    if k == 5:
        print("Pääsy evätty")
        break

    elif t != "python" or s != "rules":
        print("Käyttäjätunnus tai salasana väärin. Yritä uudestaan.")
        t = input("Anna käyttäjä tunnus: ")
        s = input("Anna salasana: ")
        k += 1

    elif t == "python" and s == "rules":
        print("Tervetuloa")
        break
