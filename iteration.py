

def show():
    """ For Loop """
    """
    for element in sequence:
        # for statement code block
    else: # optional
        # else block code
    """
    # list
    numbers = range(1,10, 2)

    for number in numbers:
        print(number)

    # string
    message = "Hello World"

    for character in message:
        print(f'char: {character}')

    # tuple
    """ id, person info """
    person = tuple(('12345',{"name":"Folau","grade":"3.5"}))
    for p in person:
        print(p)

    # set
    names = set(('Folau','Lisa','Mele'))

    for name in names:
        print(name)

    #dictionary
    profile = dict(name="Folau",age=30,job="SWE")
    for attr in profile:
        print(attr)

    teams = ['Lakers','Jazz','Suns']
    for team in teams:
        print(team)
    else:
        print("done looping through teams")

    # reversed iteration
    numbers = (1, 2, 3, 4, 5)

    for num in reversed(numbers):
        print(num)

    """ While Loop """
    """
    while condition:
        # while block code
    else: # optional
        # else block code
    """
    count = 0
    while count < 10:
        print(count)
        count+=1
    else:
        print("done counting!")