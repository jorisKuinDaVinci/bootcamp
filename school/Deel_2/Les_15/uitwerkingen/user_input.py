def get_integer(zin): # parameter kun je gebruiken als var
    getal = -1
    while getal == -1:
        try:
            getal = int(input(zin))
        except ValueError:
            print("Voer toch eens een getal in, dat doe je nu niet.")  

    return getal
