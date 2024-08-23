#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#Kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#Nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
import random

random_number = random.randint(100,999,)
random_number1 = random.randint(1000,9999,)
print(f"Kolmenumeroinen koodi: {random_number}")
print(f"Nelinumeroinen koodi: {random_number1}")




