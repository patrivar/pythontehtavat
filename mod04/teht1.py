#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

h = 1
while h < 1000:
    h += 1
    if h % 3 == 0:
        print(f"{h}")