

## returning muultiple things from a method

def getUserInfo():

    return "Folau", "Kaveinga", 34

firstName, lastName, age = getUserInfo()

print("firstName: {}".format(firstName))
print("lastName: {}".format(lastName))
print("age: {}".format(age))

## call back function
def call_stripe(key: str, call_bank):
    print("key:{}".format(key))
    call_bank("now")

def call_bank_api(msg: str):
    print("msg:{}".format(msg))

call_stripe("mykey", call_bank_api)