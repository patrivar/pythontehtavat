# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien
# lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
# sen palauttaman summan.

l = []
k = input("Anna luku: ")

while k != "":
    l.append(k)
    k = input("Anna luku: ")

def sum(*l):
        tsum = 0
        for sum in l:
            tsum = tsum + int(sum)
        return tsum
print(sum(*l))
