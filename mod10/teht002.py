class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            while kohdekerros > self.kerros:
                print(f'Hissi on kerroksessa {self.kerros}')
                self.kerros_ylos()
        elif kohdekerros < self.kerros:
            while kohdekerros < self.kerros:
                print(f'Hissi on kerroksessa {self.kerros}')
                self.kerros_alas()
        print(f'Hissi on nyt kerroksessa {self.kerros}')

    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print(f'Hissiä numero {hissin_numero} ei ole olemassa.')

# Pääohjelma
talo = Talo(1, 10, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2, 3)