# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas
# lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin
# metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
# julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, nimi, vuosi):
        self.nimi = nimi
        self.julkaisuvuosi = vuosi
        
class Kirja(Julkaisu):
    def __init__(self,nimi, julkaisuvuosi, kirjoittaja, sivumaara):
        super().__init__(nimi, julkaisuvuosi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    
    def tulosta_tiedot(self):
        print(f"Teos: {self.nimi}Kirjailija: {self.kirjoittaja} Teoksessa on sivuja {self.sivumaara}")
    
class Lehti(Julkaisu):
    def __init__(self,nimi, julkaisuvuosi, paatoimittaja):
        super().__init__(nimi, julkaisuvuosi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi} Päätoimittaja: {self.paatoimittaja}")


j = Julkaisu('Magea Magasiini', 2000)

kirja = Kirja('Hytti n:o 6', 1999, 'Rosa Liksom', 200)
lehti = Lehti('Aku Ankka', 2002, 'Aki Hyyppä')

print(kirja.nimi)

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()
