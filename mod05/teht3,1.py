
def is_prime_number(num):
    result = True
    for i in range(2, num):
        if num % i == 0:
            return False
    return result

user_input = int(input("Anna kokeiltava luku joka on suurempi kuin 1: "))
result = is_prime_number(user_input)
if result == True:
    print(f"Luku {user_input} on alkuluku")
else:
    print(f"Luku {user_input} ei ole alkuluku")