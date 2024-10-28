# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
# palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
# ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.


g = int(input("Montako gallonaa bensaa tynnyrissä on: "))

def tynnyri(g):
    if g >= 0:
        while g >= 0:
            l = g * 3.785
            print(f"Tynnyrissä on siis {l:.2f} litraa bensaa.")
            g = int(input("Montako gallonaa bensaa tynnyrissä on: "))

    print("Tynnyrissä ei ole polttoainetta")
    return

tynnyri(g)