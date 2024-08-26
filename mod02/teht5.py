#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#1 leiviskä on 20 naulaa
#1 naula on 32 luotia
#1 luoti on 13.3g

l = 13.3
n = 32 * l
lei = 20 * n

le = float(input("Anna leivisköiden määrä: "))
na = float(input("Anna naulojen määrä: "))
luo = float(input("Anna luotien määrä: "))

summa = (luo * l + n * na + lei * le)


weight_in_grams = summa % 1000
weight_in_kilograms = summa // 1000

print(f"Massa on nykymittojen mukaan: {weight_in_kilograms:.0f}kg ja {weight_in_grams:.2f}g")
