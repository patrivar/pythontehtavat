# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
# vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

kuukausi = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät",
            "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")


k = int(input("Monesko kuukausi on menossa? (1-12) "))
kuukausi = kuukausi[k-1]

print(kuukausi)