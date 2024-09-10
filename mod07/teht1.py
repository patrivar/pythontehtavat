# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
# vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

kuukausi = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu",
            "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")


k = int(input("Monesko kuukausi on menossa? (1-12) "))
kuukausi = kuukausi[k-1]

if k == 2 or 3 or 4:
    print("Kevättä eletään.")
elif k == 5 or 6 or 7:
    print("Elätään kesä aikaa.")
elif k == 8 or 9 or 10:
    print("Eletään kaunista syksyä.")
else:
    print("Talvikausi meneillään.")