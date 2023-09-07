# Hoi Joris, wat is je leeftijd?
naam = "Joris" 
zin = f"Hoi {naam}, wat is je leeftijd?"
leeftijd = int(input(zin))

STUDENTEN_TARIEF = 25 # constanten
STANDAARD_TARIEF = 27,58
SENIOREN_TARIEF = 35
prijs = STANDAARD_TARIEF

aanbiedings_zin = ''

# dus o.b.v. leeftijd moet er een aanbieding komen en oh ja,  nog geen 18 dan: roep je ouders
# tot 50 is 2 gb extra 
# vanaf 50 gratis sms
# tot 25 jaar studenten
# vaaf 50 senioren_tarief
if leeftijd < 18:
    aanbiedings_zin = ("je mag helaas zelf nog geen abbomemnt afsluiten!")
elif leeftijd < 50: 
    aanbiedings_zin = ("Je krijgt van ons gratis 2 GB extra data (vanaf 25 GB)")
    if leeftijd < 25:
     prijs = STUDENTEN_TARIEF
    
   
else:
    prijs = SENIOREN_TARIEF
    aanbiedings_zin = ("je krijgt van ons (zolang de vooraad strekt)") 

if leeftijd >= 18:
 tekst = f"Ons abonnement is {prijs} per maand!!! En je krijgt van ons: "
 print(tekst + " " + aanbiedings_zin)     

 # < kleiner dan 
 # > groter dan
 # = gelijk aan
 # != niet gelijk aan 
 # 
