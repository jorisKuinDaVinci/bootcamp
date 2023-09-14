lege_lijst = [] # dit is een voorbeeld van een list (deze kun je met code wijzigen)
leeg = 0
while leeg == 0:
    try:
       leeg = int(input("voer 1 getal in!"))
    except ValueError:
        print("Dit is niet juist ingevoerd!(Voer cijfers in!)")  


lege_lijst.append(leeg)

print(lege_lijst)


for getal in lege_lijst:
    print(getal)

for aapje in range(5):
    print(aapje)