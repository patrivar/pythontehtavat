# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen
# nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin
# mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava
# automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123,
# huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.


class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus
        print(f"Auto luotu {self.rek_nro}, huiput {self.huippunopeus}")

Auto('ABC-123', 142)