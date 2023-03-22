
# Driver code
dict1 = {}
dict2 = {'a': 10, 'b': 8}
dict3 = {'d': 6, 'c': 4}

dict1.update(dict2)

print(dict1)

dict1.update(dict3)

print(dict1)

# print(dict1['name'])

print("dict3.keys type={}, dict3.keys={}".format(type(dict3.keys()),  dict3.keys()))