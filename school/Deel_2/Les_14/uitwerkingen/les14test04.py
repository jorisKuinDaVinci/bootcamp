# studenten inschrijven
#leeftijd_tuple = (12, 15, 17, 21, 13) # dit is een voorbeeld van een tuple (herken je aan de haakjes)
leeftijd_lijst = [12, 15, 17, 21, 13] # dit is een voorbeeld van een list (deze kun je met code wijzigen)
leeftijd = 0
while leeftijd == 0:
    try:
       leeftijd = int(input("wat is je leeftijd?"))
    except ValueError:
        print("Dit is niet juist ingevoerd!(Voer cijfers in!)")  


leeftijd_lijst.append(leeftijd)

print(leeftijd_lijst)


totaal = 0
for getal in leeftijd_lijst:
    totaal = totaal + getal

print(totaal)
gemiddelde  = totaal / len(leeftijd_lijst)
print(gemiddelde)