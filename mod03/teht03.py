#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
#onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

S = input("Oletko nainen vai mies?")
H = int(input("Anna hemoglobiini arvosi (g/l): "))
if S == "nainen" and 117<= H <=175:
    print("Hemoglobiiniarvosi on normaali")
elif S == "nainen" and H < 117:
    print("Hemoglobiiniarvosi on alhainen")
elif S == "nainen" and H > 175:
    print("Hemoglobiiniarvosi on korkea")
elif S == "mies" and H < 134:
    print("Hemoglobiiniarvosi on alhainen")
elif S == "mies" and H > 195:
    print("Hemoglobiiniarvosi on korkea")
elif S == "mies" and 134<= H <= 195:
    print("Hemoglobiiniarvosi on normaali")
else:
    print("Aivokapasiteettisi on alhainen. Kokeileppa uudestaan.")