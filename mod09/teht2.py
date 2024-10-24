# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden
# muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava
# auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi
# eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin
# +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten
# hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei
# tarvitse vielä päivittää.

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus
        print(f"Auto luotu {self.rek_nro}, huiput {self.huippunopeus}")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def auton_nopeus(self):
        print(f"Nopeus: {self.nopeus}")


a1 = Auto('ABC-123', 142)
a1.kiihdyta(30)
a1.kiihdyta(70)
a1.kiihdyta(50)
a1.auton_nopeus()
a1.kiihdyta(-200)
a1.auton_nopeus()