naam = (input(f"wat is je naam?"))

#kleuren = ('zwart','wit','rood','oranje','groen','blauw','geel','paars','roze','bruin','grijs')
getallen = ('1','2','3','4','5')

getal = (input(f"Welk getal?"))

if getal in getallen:
    print(f"{naam}, je getal is {getal}!")
    if getal == "3":
        print("Je hebt het getal goed geraden!")
    else:
        if getal == "2":
            print("Je hebt het getal niet goed geraden!")    
        if getal == "1":
            print("Je hebt het getal niet goed geraden!") 
        if getal == "4":
            print("Je hebt het getal niet goed geraden!")  
        if getal == "5":
            print("Je hebt het getal niet goed geraden!")            
else:
    print(f"Geen getal gevonden.")