import random
class Autotalli:
    def __init__(self):
        self.autot = []
    def auto_sisaan(self, auto):
        # Tarkistetaan ettei auto ole jo tallissa
        # Parempi tapa olisi muuttaa lista joukoksi, jolloin dublikaatteja ei sallita
        for a in self.autot:
            if a == auto: # => True jos viittaavat samaan olioon. Eli olio on jo tallissa.
                return
        self.autot.append(auto)

    def auto_ulos(self,auto):
        self.autot.remove(auto)

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
        self.auto.kulje(1)
        self.auto.kiihdytä(140)
        print(self.auto.nopeus)
        self.auto.kulje(0.1)
        self.auto.kiihdytä(-250)
        self.auto.tulosta_ominaisuudet

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus
        print(f"Auto luotu {self.rek_nro}, huiput {self.huippunopeus}")

    def tulosta_ominaisuudet(self):
        print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.nopeus}, matkamittari: {self.matka}")

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        #Aika tunneissa
        self.matka += aika * self.nopeus


# Luodaan olio ja sijoitetaan viittaukset niihin muuttujiin

a1 = Auto('ABC-123', 142)
a2 = Auto('XYZ-789', 250)
kuski1 = Kuljettaja('Räikkönen', 48, a1)
kuski1.aja()

# Luodaan autotalli-tyyppinen olio ja sijoitetaan autot sinne

talli = Autotalli()

talli.auto_sisaan(a1)
#talli.auto_sisaan(a2)
#talli.tulosta_inventaario()
#talli.auto_ulos(a1)
#talli.tulosta_inventaario()


#Luodaan 10 erillaista auto-oliota autotalliin
for i in range(10):
    uusi_auto = Auto(f"ABC-{i+1}", random.randint(100,200))
    talli.auto_sisaan(uusi_auto)
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