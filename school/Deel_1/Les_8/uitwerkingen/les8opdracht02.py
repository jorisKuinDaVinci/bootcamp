naam = "Joris" 
zin = f"Hoi {naam}, wat is je cijfer?"
cijfer = int(input(zin))

STANDAARD_CIJFER = 6
omschrijving = "goed"

cijfer_zin = ''

if cijfer < 6:
    cijfer_zin = ("Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
elif cijfer > 6: 
    cijfer_zin = ("Jammer, {omschrijving} je resultaat is een {cijfer}")
elif cijfer > 10: 
    cijfer_zin = ("Dit kan ik niet omzetten!")    

# ik weet dat er hier niet een cijver uitkomt maar ik weet niet een andere manier om dit te coderen 
# ik weet niet waarom het niet werkt 
# zie schermafbeeldingen  