def add(num1, num2):
    return num1 + num2;

def multiply(num1, num2):
    return num1 * num2;


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

# this function will receive a tuple of arguments
def print_profile(*profile):
    print(f'name: {profile[0]}, age: {profile[1]}')

# This way the function will receive a dictionary of arguments, and can access the items accordingly
def print_user(**user):
    print(f'name: {user["name"]}, age: {user["age"]}')

def print_value(value="Test"):
    print(f'value: {value}')

doubleNumber = lambda num : num * 2

mult = lambda num1, num2 : num1 * num2



### optional parameters ####

def handle_log(name: str, option: str = None):
    print("name={}, option={}".format(name,option))


handle_log("Folau")