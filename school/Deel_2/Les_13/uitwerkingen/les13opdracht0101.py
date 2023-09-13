naam = (input(f"wat is je naam?"))

#kleuren = ('zwart','wit','rood','oranje','groen','blauw','geel','paars','roze','bruin','grijs')
kleuren = ('zwart','wit','rood','oranje','blauw','paars','grijs')

kleur = (input(f"Welke kleur vindt je mooi?"))

if kleur in kleuren:
    print(f"{naam}, ik vindt {kleur} ook een mooie kleur!")
else:
    print(f"Deze kleur is niet zo geweldig!")
# deze code werkt    