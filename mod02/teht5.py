#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#1 leiviskä on 20 naulaa
#1 naula on 32 luotia
#1 luoti on 13.3g
from getopt import gnu_getopt

l = 13.3
n = 32 * (l)
lei = 20 * (n)

le = float(input("Anna leivisköiden määrä: "))
na = float(input("Anna naulojen määrä: "))
luo = float(input("Anna luotien määrä"))

summa = luo * l + n * na + lei * le

gramma = summa
Kg = gramma / 1000%

print(f"Massa on nykymittojen mukaan: {int(Kg), gramma}")


