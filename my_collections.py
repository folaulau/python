from collections import Counter

data = [{'name':'Folau','age':4}, {'name':'Folau','age':2}, {'name':'Femi','age':4},{'name':'Femi','age':3}]

# create a list of key-value pairs by flattening each dictionary in the list
pairs = [(k, v) for d in data for k, v in d.items()]

# use Counter to tally the key-value pairs
tally = Counter(pairs)

# print the tallies
print(tally)