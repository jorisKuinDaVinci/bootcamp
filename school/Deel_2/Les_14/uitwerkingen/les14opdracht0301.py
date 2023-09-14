fruit_lijst = ["Appel", "Framboos", "Banaan", "Kiwi", "Peer", "Aardbei"] # dit is een voorbeeld van een list (deze kun je met code wijzigen)
#leeg = 0
gegeven_fruit = "Bes"
try:
      gegeven_fruit = input("voer een fruit in!")
except ValueError:
        print("Dit is niet juist ingevoerd!(Voer een fruit in!)")  


fruit_lijst.append(gegeven_fruit)

print(fruit_lijst)


for getal in fruit_lijst:
    print(getal)

fruit_lijst.remove(gegeven_fruit)

print(fruit_lijst)