woord_lijst = ["Doos", "Schoen", "Huis", "School", "Bank", "Bed"] # dit is een voorbeeld van een list (deze kun je met code wijzigen)
#leeg = 0
gegeven_woord = "Trein"
gegeven_woord_2 = "Bus"
try:
      gegeven_woord = input("voer een woord in!")
except ValueError:
        print("Dit is niet juist ingevoerd!(Voer een woord in!)")                                   


woord_lijst.append(gegeven_woord)

print(woord_lijst)




for getal in woord_lijst:
    print(getal)

for aapje in range(5):
    print(aapje)    

woord_lijst.remove(gegeven_woord)

print(woord_lijst)