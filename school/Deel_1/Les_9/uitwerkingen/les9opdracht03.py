snor = (input(f"heb je een snor?"))



diploma = (input(f"heb je een diploma?"))


   

leeftijd = int(input(f"wat is je leeftijd?"))


if leeftijd>18 and snor=="ja":
    print(f"Gefeliciteerd, je bent aangenomen!")
elif leeftijd==18 and snor=="ja":
    print(f"Gefeliciteerd, je bent aangenomen!")          
elif leeftijd<18 and diploma=="ja":
    print(f"Gefeliciteerd, je bent aangenomen!")
elif leeftijd==18 and snor=="nee":
    print(f"Helaas, je bent niet aangenomen.")
elif leeftijd>18 and snor=="nee":
    print(f"Helaas, je bent niet aangenomen.")           
elif leeftijd<18 and diploma=="nee":
    print(f"Helaas, je bent niet aangenomen.")     
# code werkt nu wel    