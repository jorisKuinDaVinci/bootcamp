def vraagleeftijd():
    while age ==0:
        age:input ("leeftijd?")
    try:
        age = int(age)
    except:
        age= 0
    return age

leeftijd = vraagleeftijd