t = "python"
s = "rules"
inputt = input("Anna käyttäjätunnus")
inputs = input("Anna salasana")
k = 1

while (inputt != t or inputs != s) and k < 5:
    inputt = input("Anna käyttäjätunnus")
    inputs = input("Anna salasana")
    k += 1
if k == 5:
    print("Pääsy evätty")
else:
    print("Tervetuloa")