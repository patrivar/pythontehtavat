import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

def luo_autot(maara):
    autot = []
    for i in range(1, maara + 1):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))
    return autot

def tulosta_tulokset(autot):
    print(f"{'Rekisteritunnus':<12} {'Huippunopeus':<12} {'Nopeus':<7} {'Matka':<7}")
    for auto in autot:
        print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<12} {auto.nopeus:<7} {auto.matka:<7}")

def kilpailu():
    autot = luo_autot(10)
    kilpailu_kaynnissa = True

    while kilpailu_kaynnissa:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)
            if auto.matka >= 10000:
                kilpailu_kaynnissa = False
                break

    tulosta_tulokset(autot)

if __name__ == "__main__":
    kilpailu()