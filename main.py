import math
from math import sqrt
import calculator
from calculator import multiply
import if_statements
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import data_types

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

    data_types.showDataTypes()

    if_statements.showIfStatements()