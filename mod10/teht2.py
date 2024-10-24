# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina
# annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä
# talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita
# taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita
# pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, hissi_numero):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.kerros = alin_kerros
        self.numero = hissi_numero

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
    def __init__(self, alin_kerros, ylin_kerros):
        self.hissit = []
        self.alin = alin_kerros
        self.ylin = ylin_kerros


    def hissit(self):
        for i in range(3):
            hissi = Talo(f'Hissi {i+1}')
            self.hissit.append(hissi)



    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 1 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print(f'Hissiä numero {hissin_numero} ei ole olemassa.')


talo = Talo(1, 10)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 7)
talo.aja_hissiä(3, 3)
