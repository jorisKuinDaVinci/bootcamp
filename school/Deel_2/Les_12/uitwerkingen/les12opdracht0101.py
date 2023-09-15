name = input('Wat is jouw naam? ')
print('Hallo', name)
leeftijd = input('Wat is je leeftijd? ')
print('Hallo', name, 'je leeftijd is', leeftijd)

def telop (leeftijd, getal2):
    resultaat= leeftijd + getal2
    return resultaat

print(telop(leeftijd,5))