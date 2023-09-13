autos = ('fiat','bmw','mercedes','volkswagen','jaguar')
print('we hebben meerdere occasions')
for aanbieding in autos:
        print(aanbieding)

auto = input('Wat wilt u kopen? ')

if auto in autos:
    print('wat biedt u?')
else:
    print('Helaas, daar valt niets aan te verdienen!') 


print(autos[2])       