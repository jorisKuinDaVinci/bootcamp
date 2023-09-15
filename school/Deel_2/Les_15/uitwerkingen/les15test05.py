
def divide (getal1, getal2, operator):
    if operator == '/':
        result = getal1 / getal2
    elif operator == '*':
        result = getal1 * getal2
    else:
        result = 0
            
    return result

def divide (getal1, getal2):
    result = getal1 / getal2
    return result

g1 = int(input('getal1? '))
g2 = int(input('getal2? '))

print(  divide(g1, g2)  )
