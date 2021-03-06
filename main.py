import math
from math import sqrt
import functions
import functions
import if_statements
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import data_types
import iteration
from user import User
from manager import Manager
from manager import CTO
import json
import user_input
import files
import exceptions

def print_user(man):
    print(man.__dict__)
    print(man.is_active())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # function

    functions.print_hi('PyCharm')
    functions.say_hi('Folau')

    # method with return value
    result = functions.is_adult(20);
    print(f'is adult {result}')

    # use built-in methods
    print(math.pow(2,3))
    print(sqrt(4))

    print(functions.add(1, 2))
    print(functions.multiply(1, 2))

    data_types.showDataTypes()

    if_statements.showIfStatements()

    iteration.show();

    # Arbitrary arguments *
    functions.print_profile("Folau", 30)

    # Keyword Arguments
    functions.print_hi(name="Folau")

    #Arbitrary Keyword Arguments, **kwargs
    functions.print_user(name="Folau", age=30)

    # default paramater value
    functions.print_value()

    # Lambda function
    doubledNum = functions.doubleNumber(3);
    print(doubledNum) # 6

    # Lambda function
    result = functions.mult(3,3);
    print(result)# 9

    numbers = [1,2,3,4,5,6]
    new_numbers = list(filter(lambda x: (x%2==0), numbers))
    print(f'{new_numbers}') #[2, 4, 6]


    #class
    kinga = User("Kinga", 8)
    print(kinga.get_name())
    del kinga.name
    print(f'name: {kinga.get_name()}')

    # class method
    print(User.get_admin_role())

    # static method
    print(User.get_user_role())

    # OOP - inheritance, encapsulation
    man = Manager("Laulau",23, False)

    #print json string
    print(man.__dict__)

    cto = CTO("Laulau",23, False)

    print_user(man)
    print_user(cto)

    # # user input
    # user_input.show()

    # file (read/wite)
    files.show()

    #exception handling
    exceptions.show()

