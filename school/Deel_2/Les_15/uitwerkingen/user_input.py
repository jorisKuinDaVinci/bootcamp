def get_integer(zin): # parameter kun je gebruiken als var
    getal = -1
    while getal == -1:
        try:
            getal = int(input(zin))
        except ValueError:
            print("Voer toch eens een getal in, dat doe je nu niet.")  

    return getal

def get_float():
    float = ""
    while float == "":
        float = input(float)
        if len(float) > 1:
            float = ""
            print("Max. 1 float!")
    
    return float
#def get_string():
def get_letter(vraag):
    letter = ""
    while letter == "":
        letter = input(vraag)
        if len(letter) > 1:
            letter = ""
            print("Max. 1 karakter!")
    
    return letter