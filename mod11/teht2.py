# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton
# ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi
# sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
# polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
import random

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus
        print(f"Auto luotu {self.rek_nro}, huiput {self.huippunopeus}")

    def kiihdyta(self, nopeudenmuutos):
        self.nopeus += nopeudenmuutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def ajo(self, aika):
        self.matka += aika * self.nopeus


class Sahkoauto(Auto):
    akkukapasiteetti = 0
    def __init__(self, rek_nro, huippunopeus, akkukapasiteetti):
        super().__init__(rek_nro, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        print(f"Autolla {self.rek_nro} matkaa on kertynyt {self.matka}km kun nopeus oli {self.nopeus}km/h")


class Polttomoottoriauto(Auto):
    bensatankki = 0
    def __init__(self, rek_nro, huippunopeus, bensatankki):
        super().__init__(rek_nro, huippunopeus)
        self.bensatankki = bensatankki

    def tulosta_tiedot(self):
        print(f"Autolla {self.rek_nro} matkaa on kertynyt {self.matka}km kun nopeus oli {self.nopeus}km/h")

autot = []
autot.append(Sahkoauto( 'ABC-15', 180, 52.5))
autot.append(Polttomoottoriauto('ACD-123', 165, 32.3))

for auto in autot:
    nopeudenmuutos = random.randint(1, 180)
    auto.kiihdyta(nopeudenmuutos)
    auto.ajo(3)
    auto.tulosta_tiedot()