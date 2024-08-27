'''
print(not 1 != 1)
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(True and(False or True))

result = (False or False) and (False or True)
print(f"Vertailun tulos: {result}")

print(1 == 1)
print(1 == 2 or 1 == "1")
print(1 < 2 or (1 == 1 and result))
'''
#while-silmmukat (loopit)
#Ikuinen silmukka. Ei hyvä juttu
'''
while True:
    print("Moi")
    print("Helv")
'''
'''
max_count = int(input("Montako kertaa kukutaan? "))
counter = 0
while counter < max_count:
    counter = counter + 1
    print(f"{counter}. Kerran Kukkuu")
print(f"Laskurin arvo lopuksi {counter}")
'''

#ohjelma komentorivikäyttöliittymällä
command = ""
while command != "lopeta":
    command = input("Komento, kiitos: ")
    if command == "lopeta":
        print("Lopetetaan.")
        #break# "Heittää ulos" silmukasta, ei paras ohjelmointikäytäntö
    else:
        print("En ymmärrä komentoa. Yritä uudestaan.")
print("Ohjelma sammutettu.")