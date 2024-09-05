# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
# maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

n = int(input("Montako tahkoista noppaa heitetään: "))

def noppa(n):
    s = random.randint(1,n)
    if s == n:
        print(f"{s}")
        return True
    else:
       while s != n:
           s = random.randint(1,n)
           print(f"{s}")
    return True

noppa(n)