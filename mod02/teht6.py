#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#Kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#Nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
import random

random_number = random.randint(0,9)
random_number1 = random.randint(0,9)
random_number2 = random.randint(0,9)
random_number3 = random.randint(1,6)
random_number4 = random.randint(1,6)
random_number5 = random.randint(1,6)
random_number6 = random.randint(1,6)
print(f"Kolmenumeroinen koodi: {random_number, random_number1, random_number2}")
print(f"Nelinumeroinen koodi: {random_number3, random_number4, random_number5, random_number6}")




