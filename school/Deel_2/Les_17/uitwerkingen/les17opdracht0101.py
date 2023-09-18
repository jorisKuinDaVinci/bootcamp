naam = (input(f"wat is je naam?"))

#kleuren = ('zwart','wit','rood','oranje','groen','blauw','geel','paars','roze','bruin','grijs')
getallen = ('1','2','3','4','5')

getal = (input(f"Welk getal?"))

if getal in getallen:
    print(f"{naam}, je getal is {getal}!")
else:
    print(f"Geen getal gevonden.")