#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#Kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#Nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
import random

from mod02.teht2 import random_number

n = float(input("montako numeroisen koodin haluat (3 vai 4): "))




if n == "3":
    random_number = random.randint(0, 9)
 print ("f"(random_number, random_number, random_number))

elif n == "4":

     random_number = random.randint (1,6
 print ("f"(random_number, random_number, random_number, random_number))
