# vragen:
# while uitleg
# print

naam = input("wat is je naam?")
leeftijd = int(input("wat is leeftijd")) # 17
teller = 1

# dan print 17 keer hallo naam 
while teller <= leeftijd:
    print("Aapjes eten bananen")
    # hier kan nog veel meer code, die niets met de teller of leeftijd hoeft te doen
    print(f"hallo {naam}, dit is de {teller}e keer dat ik print")
    teller = teller + 1

print("Dit is het einde van mijn programma")    