naam = input('wat is je naam? ')

#kleuren = ('zwart','wit','rood','oranje','groen','blauw','geel','paars','roze','bruin','grijs')
kleuren = ('zwart','wit','rood','oranje','blauw','paars','grijs')

kleur = input('Welke kleur vindt u mooi? ')

if kleur in kleuren:
    print("{naam}, ik vindt {kleur} ook een mooie kleur!")
else:
    print("Deze kleur is niet zo geweldig!")