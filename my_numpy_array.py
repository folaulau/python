import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# give it a type
ppl = np.array([{'name':'Folau','age': 20},{'name':'Lisa','age': 25}], dict)

for person in ppl:
    print("person:{}".format(person))


numbers = np.array([])

for num in numbers:
    print("num:{}".format(num))