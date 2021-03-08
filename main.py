import math
from math import sqrt
import calculator
from calculator import multiply
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def say_hi(name):
    print(f'Hi {name}')

def is_adult(age):
    if age>=16:
        return True
    else:
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    say_hi('Folau')

    # method with return value
    result = is_adult(20);
    print(f'is adult {result}')

    # use built-in methods
    print(math.pow(2,3))
    print(sqrt(4))

    print(calculator.add(1,2))
    print(multiply(1, 2))

    # set
    numbers = set((1,2,3))
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

    #range
    evenNumbers = range(2, 20, 2)
    print(type(evenNumbers))
    for num in evenNumbers:
        print(num)

    # dict
    person = {"firstName":"Folau", "lastName":"Kaveinga"}
    print(type(person))
    print(person)

    # Bool
    isMale = True
    print(isMale)