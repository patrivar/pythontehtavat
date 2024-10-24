class Autotalli:
    def __init__(self):
        self.autot = []
    def auto_sisaan(self, auto):
        self.autot.append(auto)
    def auto_ulos(self):
        pass
    def tulosta_inventaario(self):
        print("Autotallissa on:")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()

class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self):
        print(f"Olen{self.nimi}, {self.ika} ja ajan autoa {self.auto.rek_nro}")
        self.auto.kiihdytä(40)
        print(self.auto.nopeus)
        self.auto.kiihdytä(140)
        print(self.auto.nopeus)
        self.auto.kiihdytä(-250)
        self.auto.tulosta_ominaisuudet

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.huippunopeus = huippunopeus

    def tulosta_ominaisuudet(self):
        print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
        print(f"Tämän hetkinen nopeus: {self.nopeus}")

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

# Luodaan olio ja sijoitetaan viittaukset niihin muuttujiin

a1 = Auto('ABC-123', 142)
a2 = Auto('XYZ-789', 250)
kuski1 = Kuljettaja('Räikkönen', 48, a1)
kuski1.aja()

# Luodaan autotalli-tyyppinen olio ja sijoitetaan autot sinne
talli = Autotalli()
talli.auto_sisaan(a1)
talli.tulosta_inventaario()

'''
a1.kiihdytä(-55)
a2.kiihdytä(300)
a1.tulosta_ominaisuudet()
a2.tulosta_ominaisuudet()
a2.kiihdytä(-150)
a2.tulosta_ominaisuudet()
'''

#mod 9 harj 1 esimerkkiratkaisu
#print(f"{a1.rek_nro}, huippunopeus: {a1.huippunopeus}")
#print(f"{a2.rek_nro}, huippunopeus: {a2.huippunopeus}")