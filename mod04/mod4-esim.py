import random

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

#noppapeli
#mikä on kahde yhtäaikaisen kutosen todennäköisyys?
'''
rounds = 100
round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter += 1
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        #print(f"{roll_counter}. Heiton silmäluvut: {die1} ja {die2}.")
    #print(f"Noppaa heitettiin {roll_counter} kertaa.")
    total_rolls = total_rolls + roll_counter
print(f"kaksi kuutosta saatiin keskimäärin {total_rolls/rounds} heitolla/kierros.")

#ohjelma komentorivikäyttöliittymällä
#(valikko sovellus johon sisällytetty ylemmät)
'''

command = ""
while command != "lopeta":
    command = input("Komento, kiitos: ")
    if command == "lopeta":
        print("Lopetetaan.")
        #break# "Heittää ulos" silmukasta, ei paras ohjelmointikäytäntö

    elif command == "kukkuu":
        max_count = int(input("Montako kertaa kukutaan? "))
        counter = 0
        while counter < max_count:
            counter = counter + 1
            print(f"{counter}. Kerran Kukkuu")
        print(f"Laskurin arvo lopuksi {counter}")

    elif command == "noppa":
        rounds = 100
        round_counter = 0
        total_rolls = 0
        while round_counter < rounds:
            round_counter += 1
            die1 = die2 = roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                # print(f"{roll_counter}. Heiton silmäluvut: {die1} ja {die2}.")
            # print(f"Noppaa heitettiin {roll_counter} kertaa.")
            total_rolls = total_rolls + roll_counter
        print(f"kaksi kuutosta saatiin keskimäärin {total_rolls / rounds} heitolla/kierros.")

    else:
        print("En ymmärrä komentoa. Yritä uudestaan.")

print("Ohjelma sammutettu.")

#Tulostetaan 2 potenssit
x = 2
while x < 2:
    print(x)
    x = x * 2 #Voidaan merkitä myös x *= 2