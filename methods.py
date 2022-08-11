

## returning muultiple things from a method

def getUserInfo():

    return "Folau", "Kaveinga", 34

firstName, lastName, age = getUserInfo()

print("firstName: {}".format(firstName))
print("lastName: {}".format(lastName))
print("age: {}".format(age))