# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako
# tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
# uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä
# valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa
# lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina
# siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi
# Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

k = input("Haluatko lisätä lentokentän, hakea tiedot vai lopettaa (lisää/hae/lopeta): ")
m = {"EFHK":"Helsinki"}

while k != "Lopeta":
    if k == "lisää":
        i = input("Anna uuden kentän ICAO- koodi (EFHK): ")
        l = input("Anna lentokentän nimi: ")
        m[i] = l
        k = input("Haluatko lisätä lentokentän, hakea tiedot vai lopettaa (lisää/hae/lopeta): ")
    elif k == "hae":
        h = input("Minkä kentän tiedot haluat hakea (ICAO): ")
        print(f"{m[h]}")
        k = input("Haluatko lisätä lentokentän, hakea tiedot vai lopettaa (lisää/hae/lopeta): ")
    else:
        print("Arvo ei kelpaa.")
        k = input("Haluatko lisätä lentokentän, hakea tiedot vai lopettaa (lisää/hae/lopeta): ")