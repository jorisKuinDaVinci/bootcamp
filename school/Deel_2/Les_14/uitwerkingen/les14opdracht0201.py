lege_lijst = [] # dit is een voorbeeld van een list (deze kun je met code wijzigen)
#leeg = 0
gegeven_getal = 0
while gegeven_getal == 0:
    try:
      gegeven_getal = int(input("voer een getal in!"))
    except ValueError:
        print("Dit is niet juist ingevoerd!(Voer cijfers in!)")  


lege_lijst.append(gegeven_getal)

print(lege_lijst)


for getal in lege_lijst:
    print(getal)

for aapje in range(5):
    print(aapje)

lege_lijst.remove(gegeven_getal)

print(lege_lijst)