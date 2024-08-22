#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan


height = float(input("Anna suorakulmion korkeus (cm): "))
width = float(input("Anna suorakulmion leveys (cm): "))

area = height * width
perimeter = 2 * (height + width)

print (f"Suorakulmion pinta-ala on: {area}")
print (f"Suorakulmion piiri on: {perimeter}")