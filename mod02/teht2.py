#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#pii*r**2 ( * on kerto ja ** on potenssi)
import random

r = float(input("Anna ympyrän säde (m): "))
import math
area = math.pi * r **2
print(f"Ympyrä, jonka säde on {r}, pinta-ala on {area:.1f} neliömetriä.")



# satunnaisen kokonaisluvun arpominen
random_number = random.randint(1,6)
print(f"Satunnainen luku 1-6: {random_number}")
