
t = input("Anna käyttäjä tunnus: ")
s = input("Anna salasana: ")
k = 0

while t != "python" or s != "rules" or k<5:
    if t != "python" or s != "rules":
        print("Käyttäjätunnus tai salasana on väärin. Yritä uudestaan.")
    t = input("Anna käyttäjä tunnus: ")
    s = input("Anna salasana: ")
    k += 1