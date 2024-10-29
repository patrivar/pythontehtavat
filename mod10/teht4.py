# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on
# ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa
# ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät
# toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
# kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle
# kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma
# simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina
# tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan
# tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu
# on päättynyt.

import random

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def ajo(self, aika):
        self.matka += aika * self.nopeus

def luoautot(maara):
    autot = []
    for i in range(1, maara + 1):
        rek_nro = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rek_nro, huippunopeus))
    return autot

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.ajo(1)

    def tulosta_tilanne(self):
        sijoitus = sorted(self.autot, key=lambda auto: auto.matka, reverse=True)
        for auto in sijoitus:
            print(f"{auto.rek_nro:<10} Huipunopeus: {auto.huippunopeus:<8} Ajettu matka: {auto.matka:<8} Nopeus: {auto.nopeus:<8}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

autot = luoautot(10)
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunnit = 0
valot = ['Punainen', 'Keltainen', 'Vihreä']

for i in valot:
    print(f"\n{i}")
print("\n")

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f"\nTilanne kun kisaa on ajettu {tunnit} tuntia:")
        kilpailu.tulosta_tilanne()

print("\nKilpailu on päättynyt!")
kilpailu.tulosta_tilanne()