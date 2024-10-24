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

talli = Autotalli()
class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def auton_nopeus(self):
        print(f"Nopeus: {self.nopeus} km/h")

    def etaisyys(self):
        print(f"Auto on kulkenut {self.matka:.2f}km.")

    def ajo(self, aika):
        self.matka = aika * self.nopeus

    def tulosta_ominaisuudet(self):
        print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.nopeus}, matkamittari: {self.matka}")

class Autotalli:
    def __init__(self):
        self.autot = []
    def auto_sisaan(self, auto):
        for a in self.autot:
            if a == auto:
                return
        self.autot.append(auto)

    def tulosta_inventaario(self):
        print("Autotallissa on:")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()

    def valitunti(self):
        for auto in self.autot:
            auto.self.nopeus += random.randint(-10,15)

    def autot(self):
        for i in range(10):
            uusi_auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
            talli.auto_sisaan(uusi_auto)
        talli.tulosta_inventaario()

    def tulosta_tulokset(autot):
        print(f"{'Rekisteritunnus':<12} {'Huippunopeus':<12} {'Nopeus':<7} {'Matka':<7}")
        for auto in autot:
            print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<12} {auto.nopeus:<7} {auto.matka:<7}")

    def kilpailu(self):
        autot = talli
        kilpailu_kaynnissa = True

        while kilpailu_kaynnissa:
            for auto in autot:
                nopeuden_muutos = random.randint(-10, 15)
                auto.kiihdyta(nopeuden_muutos)
                auto.kulje(1)
                if auto.matka >= 10000:
                    kilpailu_kaynnissa = False

    tulosta_tulokset(autot)