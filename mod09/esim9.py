'''
koirat = [
    {'koira' : 'Lissu', 'ikä' : 3},
    {'koira' : 'Reko', 'ikä' : 7}
]

print(koirat)
eka_koira = koirat[0]
print(eka_koira['koira'])

#-- Määritellään ensin luokka
# Luokka on "ohje" olion luomiselle

class Koira:
    pass

# 2. Olio on luokan ilmentymä
# Pääohjelmasta voi luoda useita olioita

# Luodaan koira-olio
Ullan_koira = Koira()
Elviiran_koira = Koira()

# Annetaan koira-olioille ominaisuuksia
# Ominaisuudet ovat oliokohtaisia, kaikki oat koiria,
# Mutta nimi, syntymävuosi, karvanlaatu tms. muuttuu

Ullan_koira.nimi ='Lissu'
Ullan_koira.syntymävuosi = 2015

Elviiran_koira.nimi = 'Reko'
Elviiran_koira.syntymävuosi = 2016

print(f'Ullan koiran nimi on {Ullan_koira.nimi} ja hän on syntynyt vuonna {Ullan_koira.syntymävuosi}')
print(f'Elviiran koiran nimi on {Elviiran_koira.nimi} ja on hän syntynyt vuonna {Elviiran_koira.syntymävuosi}')

# edellisessä esimerkissä tehtiin luokka ilman ominaisuuksia ja metodeja
# Ominaisuudet annettiin yksi kerrallaan
# Tämä on työlästä ja oikea tapa onkin määritellä ja alustaa ominaisuudet luokan avulla
'''

'''
Luokkien perusrakenne
'''

# Luokkien nimissä on CamelCase

class LuokanNimi:

    # __init__ on funktio, erityinen sellainen jota kutsutaan konstruktoriksi
    # Tätä funktiota kutsutaan aina automaattisesti kun luodaan luokasta olio / instanssi
    # Alustajan loppuun EI kirjoiteta return-lausetta

    def __init__(self, parametri1, parametri2):
        self.atribuutti1 = parametri1
        self.atribuutti2 = parametri2

    def metodi(self):
        return

    def metodi2(self):
        return

'''
Laajennetaan yllä olevaa koira-esimerkkiä niin että se alustaan koirien ominaisuudet
'''

class Koira:
    def __init__(self, nimi, syntymävuosi, väri, koko):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.väri = väri
        self.koko = koko

    def printtaa_tiedot(self):
        print(f'Koiran nimi on {self.nimi} ja syntymävuosi on {self.syntymävuosi}')
        return

k1 = Koira('Lissu', 2015, 'Musta', 'Iso')
k2 = Koira('Reko', 2016, 'Oranssi', 'Keskikokoinen')
k3 = Koira('Raippa', 2020, 'Sininen', 'Pieni')

print(k2.väri)
print(k3.koko)

'''
Laajennetaan yllä olevaa ohjelmaa ja tehdään sinne metodi jossa printataan koirien tiedot
'''

k1.printtaa_tiedot()

'''
Laajennetaan yllä olevaan Koira-luokka esimerkkiä niin että lisätään sinne uusi metodi.
Metodi on funktio jota voi kutsua olion ilmentymille. Eli jokainen Koira-olio voi esim. haukkua.'''

class Koira:

    tehty = 0

    def __init__(self, nimi, syntymävuosi, väri, koko, haukahdus = 'hauhauhau'):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.väri = väri
        self.koko = koko
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

    def printtaa_tiedot(self):
        print(f'Koiran nimi on {self.nimi} ja syntymävuosi on {self.syntymävuosi}')
        return
    def hauku(self, kerrat):
        print(f'koira {self.nimi} haukkuu {kerrat} kertaa.')
        for i in range(kerrat):
            print(self.haukahdus)
        return
k1 = Koira('Lissu', 2015, 'Musta', 'Iso', 'wof')
k2 = Koira('Reko', 2016, 'Oranssi', 'Keskikokoinen', 'hau')

# tämän olion luonnista puuttuu haukahdus atribuutti jonka vuoksi se käyttää oletusarvoksi annettua atribuuttia.
k3 = Koira('Raippa', 2020, 'Sininen', 'Pieni')

k1.hauku(5)
k2.hauku(6)
k3.hauku(1)
print(f'Koiria tehty {Koira.tehty}')