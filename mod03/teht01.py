#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha = float(input("Kuinka monta cm kuha on?"))

if kuha < 37:
    cm = 37 - kuha
    print(f"Kuha on {cm}cm liian pieni ja se pitää laskea takaisin veteen.")

else:
    print("Olet saanut hienon vonkaleen!")