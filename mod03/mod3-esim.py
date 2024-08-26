#Alustus ehtolauseille
'''
rahat = float(input("Anna rahamäärä: "))

if rahat>=5:
   # print("Voit ostaa latten")


#Sama kuin
rahat = float(input("Anna rahamäärä: "))
ehto = (rahat>=5)
print(ehto)

if ehto:
    #Tämä osa on lohko joka suoritetaan jos ehto on totta
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa")

print("Jatketaan ohjelmaa")

suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari==räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")
'''
#luo ohjelma joka pyytää käyttäjän numeron ja tulostaa onko luku pos, neg vai nolla
'''
luku = int(input("Anna luku: "))
if luku > 0:
    print("Tulos on positiivinen")

elif luku < 0:
    print("Tulos on negatiivinen")

else:
    print("luku on nolla")
'''

rahat = float(input("Anna rahamäärä: "))
if rahat>=5:
    print("Voit ostaa latten")
else:
    print("Olet köyhä.. menisit töihin..")

#monta vaihtoehtoa

user_input = input("valitse a, b tai c: ")
if user_input=="a":
    print("Tehdään jotain, käyttäjä valitsi kirjaimen a")
elif user_input=="b":
    print("Tehdään jotain muuta kivaa, käyttäjä valitsi b")
elif user_input=="c":
    print("Miksi valitsit c... köyhäkö olet")
    a = 4+4
    print (f"Saat almuja {a}e... köyhä")
else:
    print("Et valinnut järkevää vastausta.. takas kouluun")


ika = int(input("Anna ikäsi: "))
if ika>=65:
    print("Olet eläkeiässä.")
elif ika>=18:
    print("Olet työiässä.")
elif ika>=7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")

print('ohjelman päätös')