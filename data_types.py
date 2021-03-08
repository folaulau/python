

def showDataTypes():
    # set
    numbers = set((1, 2, 3))
    print(type(numbers))

    numbers = {1, 2, 3}
    print(type(numbers))

    firstName = "Folau"
    print(firstName)

    firstName = str("Folau")
    print(type(firstName))
    print(firstName)

    number = 2.5
    print(number, "is float number?", isinstance(number, float))

    lista = [1, 2.2, 'python']

    print(lista)

    # int
    intNum = 2
    print(type(intNum))
    print(intNum)

    # range
    evenNumbers = range(2, 20, 2)
    print(type(evenNumbers))
    for num in evenNumbers:
        print(num)

    # dict
    person = {"firstName": "Folau", "lastName": "Kaveinga"}
    print(type(person))
    print(person)

    # Bool
    isMale = True
    print(isMale)