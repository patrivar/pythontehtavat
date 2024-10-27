# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
# tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus
# on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 2000
        self.huippunopeus = huippunopeus
        print(f"Auto luotu {self.rek_nro}, huiput {self.huippunopeus}")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def auton_nopeus(self):
        print(f"Nopeus: {self.nopeus} km/h")

    def etäisyys(self):
        print(f"Auto on kulkenut {self.matka:.2f}km.")

    def ajo(self, aika):
        self.matka = self.matka + aika * self.nopeus


a1 = Auto('ABC-123', 142)
a1.kiihdyta(60)
a1.ajo(1.5)

a1.etäisyys()