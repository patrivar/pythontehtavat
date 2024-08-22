# syötteen lukeminen ja sijoittaminen muuttujaan


name = input("Anna nimesi: ")

# name = "Patric"    antaa komennolle name arvon
# \ on escape-merkki, jolla voi tuottaa esim. tabin tai rivinvaihdon
#\n on rivin vaihto. \t tekee sarkaimen eli pitkän välin (tabin).
print ("Moi \t " + name) #"moi " + "PATRIC" -> "moi PATRIC"

#age = "2"'
#Käyttäjän syöttö on aina merkkijono
age = input ("Anna ikäsi")
print("Ikäsi on " + age)
#muutetaan merkkijono (str) kokonaisluvuksi (int) ja lisätään luku
age = int(age) + 1 # "2" -> 2 + 1 -> 3
#esitellään uusi muuttuja, johon sijoitetaan numeroarvo merkki
age_string = str(age) #muutetaan int -> string,esim. 3 -> "3"
print("Ikäsi on vuoden päästä " + age_string)
age = age + 1
# taoinen tapa, tehdään tyyppimuunnos vain tarvittavaan kohtaan
print("Ikäsi on kahden vuoden päästä " + str(age))

#käyttäjän pituus metreinä, liukulluku (float) float on likiarvo
height = 1.8       #  , antaa luvulle sulkeet
print (height)
