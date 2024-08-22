#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

n = int(input("Anna kolme kokonaislukua:"))
u = int(input())
m = int(input())

summa = n + u + m
tulo = n * u * m
keskiarvo = (n + u + m) / 3


print (f"Lukujen summa on: {summa}")
print (f"Lukujen tulo on: {tulo}")
print (f"Lukujen keskiarvo on: {keskiarvo}")