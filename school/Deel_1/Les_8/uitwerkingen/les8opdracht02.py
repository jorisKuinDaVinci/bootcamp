omschrijving = "onbekent"
naam = "Joris" 
zin = f"Hoi {naam}, wat is je cijfer?"
cijfer = int(input(zin))
if cijfer==1:
    omschrijving = "zeer slecht"
elif cijfer==2:
    omschrijving = "slecht"    
elif cijfer==3:
    omschrijving = "gering" 
elif cijfer==4:
    omschrijving = "onvoldoende" 
elif cijfer==5:
    omschrijving = "bijna voldoende" 
elif cijfer==6:
    omschrijving = "voldoende" 
elif cijfer==7:
    omschrijving = "ruim voldoende" 
elif cijfer==8:
    omschrijving = "goed" 
elif cijfer==9:
    omschrijving = "zeer goed" 
elif cijfer==10:
    omschrijving = "uitmuntend"                                 

if cijfer>6:
    print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
elif cijfer<6: 
    print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")
#elif cijfer>10: 
    #print(f"Dit kan ik niet omzetten!")  
# deze code werkt wel    

