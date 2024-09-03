#Funktio esimerkkejä
'''
def do_something():
    print("Doing")
    print("Something")
    return "tässä palautettava arvo, voi olla ihan minkä tyyppinen vaan"

return_value = do_something()
print(return_value)

#Funktio jolla parametrejä (argumennttejä)
def combine_strings(string1, string2):
    combination = f"{string1}, {string2}= "
    return combination

print(combine_strings ("auto","ajaa"))

combination = combine_strings("kuski", "jarruttaa")
combination = combine_strings(combination, "nopeasti")
print(combination)
'''
'''
# Yksinkertainen laskin, jolle voi antaa vain tasan 2 parametriä
def calculate(calc_type, number1, number2):
    if calc_type == "sum":
        return (number1 + number2)
    elif calc_type == "division":
        return number2 / number2
    return None
#reurn None on oletustoiminnallisuua

print(calculate("sum", 2.4, 3.5))
print(calculate("division", 2.4, 3))
'''

'''
# Listat ja funktiot, funktio ottaa parametrina listan lukuja ja laskee
# ja palauttaa niiden summan
def calculate_sum(numbers):
    total_sum = 0
    # kaksi tapaa tehdä for-loop listan käsittelyyn
    for i in range(len(numbers)):
        total_sum = total_sum + numbers[i]
        numbers[i] = 0 # nollataan listan käsiteltävä alkio ihan vaan huviksi
    #for num in numbers:
     #   total_sum = total_sum + num
    return total_sum


nums = [3,4,5]
print(nums)
print(calculate_sum(nums))
#Funktio muokkasi samaa listaa, mihin pääohjelman num muuttuja viittaa
print(nums)

print(calculate_sum([3,4,5,10]))
'''

'''
# Vaihtuva määrä parametreja
# * tekee kaikista parametreista (arvoista) listan
# ja sijoittaa listan numbers-muuttujaan
def calculate_sum(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

print(calculate_sum(2, 3, 8, -10, 4.67))
'''


# Nimetyt parametrit ja oletusarvot
# Yksinkertainen laskin, jolle voi antaa vain tasan 2-3 parametriä

def calculate2(number1, number2, calc_type="sum"):
    if calc_type == "sum":
        return (number1 + number2)
    elif calc_type == "division":
        return number1 / number2
    return None

#reurn None on oletustoiminnallisuua

print(calculate2(2.4, 3.5))
print(calculate2(calc_type="division", number2= 2.4, number1= 3.5))
print(calculate2(2.4, 3.5, "division"))