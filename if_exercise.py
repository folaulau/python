

name = ""

if name:
    print("good")
else:
    print("bad")


name = None

if name:
    print("good")
else:
    print("bad")


name = "Laulau" if 9 == 9 else "Kinga"

print("name={}".format(name))