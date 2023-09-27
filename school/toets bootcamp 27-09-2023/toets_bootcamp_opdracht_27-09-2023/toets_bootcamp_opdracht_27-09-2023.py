# opdracht 1:

# A:

# omdat Visual Studio Code je helpt door code aan te vullen, hoef je niet alles zelf te typen
# omdat Visual Studio Code je helpt door code kleuren te geven, hierdoor is de code duidelijker

# B:

# omdat als je de code opslaat je wijzigingen makelijk kan zien, hierdoor kan je makelijk terug naar een vorige versie.

# opdracht 2:

a = 5  # dit is een voorbeeld van het datatype: integer
b = 10.5# dit is een voorbeeld van het datatype: float
c = "Hallo wereld" # dit is een voorbeeld van het datatype: string

# opdracht 3:

a = 5
b = 10

c = a
a = b
b = c
print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen

# opdracht 4:

leeftijd = input("Hoe oud ben je?")
print(f"Je bent {leeftijd} jaar oud.")
print(f"Dan duurt het nog ongeveer {67 - leeftijd} jaar voordat je met pensioen mag!")

# opdracht 5:

getal1 = 200
getal2 = 5
getal3 = 12
som = lambda getal1, getal2, getal3 : getal1 + getal2 + getal3
antwoord = som(getal1, getal2, getal3)# of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

# opdracht 6:

AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if aantal_GB_internet > AANTAL_GB or aantal_minuten_gebeld > AANTAL_MINUTEN and ONBEPERKT == False:
    print("Let op: je moet bijbetalen!")    
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")

# opdracht 7:

for i in range(1, 251):
    print(i)

# opdracht 8:

# a:

lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

eten = (input(f"Wat wil je eten?"))
if eten in lijst_eten:
    print(f"Dat is een lekker idee!")
else:
    print(f"Dat is geen lekker idee!")

# b:

index = 0
langste_naam = 0
for i in range(len(lijst_eten)):
    if len(lijst_eten[i]) > langste_naam:
        langste_naam = len(lijst_eten[i])
        index = i
print(lijst_eten[index])

# opdracht 9:

while True:
    cijfer = input("Voer een cijfer in tussen 0 en 10: ")
    if cijfer.isdigit():
        if int(cijfer) >= 0 and int(cijfer) <= 10:
            break
        else:
            print("Dit is geen cijfer tussen 0 en 10!")
    else:
        print("Dit is geen cijfer!")

# opdracht 10:

MAX = 20
getal = int(input("Voer een getal in"))
if getal > MAX:
   input(f"Het getal is groter dan [MAX]")
elif getal < MAX:
    input(f"Het getal is kleiner dan [MAX]")
else:
    input(f"Het getal is gelijk aan [MAX]")