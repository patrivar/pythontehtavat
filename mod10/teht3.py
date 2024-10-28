# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi
# palohälytys, joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että
# talossasi tulee palohälytys.
import random

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, hissi_numero):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.kerros = alin_kerros
        self.numero = hissi_numero

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            while kohdekerros > self.kerros:
                print(f'Hissi {self.numero} on kerroksessa {self.kerros}')
                self.kerros_ylos()
        elif kohdekerros < self.kerros:
            while kohdekerros < self.kerros:
                print(f'Hissi {self.numero} on kerroksessa {self.kerros}')
                self.kerros_alas()
        print(f'Hissi {self.numero} on nyt kerroksessa {self.kerros}')

    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1

class Talo:
    def __init__(self, alin_kerros, ylin_kerros):
        self.hissit = []
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.luo_hissit()

    def palo(self):
        print("Talossa on palohälytys ja kaikki hissit palaavat kerrokseen 1.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)

    def luo_hissit(self):
        for i in range(3):
            hissi = Hissi(self.alin, self.ylin, i + 1)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 1 <= hissin_numero <= len(self.hissit):
            self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)
        else:
            print(f'Hissiä numero {hissin_numero} ei ole olemassa.')

talo = Talo(1, 10)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 7)
talo.aja_hissia(3, 3)
talo.palo()