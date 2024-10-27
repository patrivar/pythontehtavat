# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti
# nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta
# auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus
# luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin
# välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h
# väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan
# kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def ajo(self, aika):
        self.matka = self.matka + aika * self.nopeus

def luoautot(määrä):
    autot = []
    for i in range(1, määrä +1):
        rek_nro = f"ABC-{i}"
        huippunopeus = random.randint(100,200)
        autot.append(Auto(rek_nro, huippunopeus))
    return autot

def tulokset(autot):
    for auto in autot:
        print(f"{auto.rek_nro:<10} {auto.huippunopeus:<8} {auto.matka:<8} {auto.nopeus:<8}")

def kisa():
    autot = luoautot(10)
    kisajatkuu = True

    while kisajatkuu == True:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.ajo(1)
            if auto.matka >= 10000:
                kisajatkuu = False

    tulokset(autot)

kisa()