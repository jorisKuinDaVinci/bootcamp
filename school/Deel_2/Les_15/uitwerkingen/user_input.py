def get_integer(zin): # parameter kun je gebruiken als var
    getal = -1
    while getal == -1:
        try:
            getal = int(input(zin))
        except ValueError:
            print("Voer toch eens een getal in, dat doe je nu niet.")  

    return getal

def get_float(zin_2):
    getal_2 = -1
    while getal_2 == -1:
        try:
            getal_2 = int(input(zin_2))
        except ValueError:
            print("Voer toch eens een getal in, dat doe je nu niet.")  

    return getal_2        
def get_string(zin_3):
    letter_2 = ""
    while letter_2 == "":
        letter_2 = input(zin_3)
        if len(letter_2) > 1:
            letter_2 = ""
            print("Max. 1 karakter!")
    
    return letter_2
def get_letter(vraag):
    letter = ""
    while letter == "":
        letter = input(vraag)
        if len(letter) > 1:
            letter = ""
            print("Max. 1 karakter!")
    
    return letter