namen_lijst = ["Jan", "Piet", "Sander", "Tyber", "Ardus", "Jouke"] # dit is een voorbeeld van een list (deze kun je met code wijzigen)
#leeg = 0
gegeven_naam = "Peter"
try:
      gegeven_naam = input("voer een naam in!")
except ValueError:
        print("Dit is niet juist ingevoerd!(Voer een naam in!)")  


namen_lijst.append(gegeven_naam)

print(namen_lijst)


for getal in namen_lijst:
    print(getal)

namen_lijst.remove(gegeven_naam)

print(namen_lijst)