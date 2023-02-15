

things = ["laulau", 34, {"teacher":"john","teacher_age":89}]

def generate():
    for thing in things:
        print("thing:{}".format(thing))
        if isinstance(thing,dict):
            yield thing
    
    yield {"status":"good"}

# function that has yield does not execute its code til its generator is used.
teacher = generate()

print("generator")

for attr in teacher:
    print("attr:{}".format(attr))