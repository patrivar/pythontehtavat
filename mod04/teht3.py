# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman

input_string = input("Syötä luku: ")
if input_string != "":
    max_num = min_num = int(input_string)
    while input_string != "":
        input_string = input("Syötä luku: ")
        if input_string != "":
            number = int(input_string)
            if number > max_num:
                max_num = number
            if number < min_num:
                min_num = number
    print(f"Pienin numero: {min_num}, Suurin numero: {max_num}")
else:
    print("ei lukua")