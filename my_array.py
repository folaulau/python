

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("array: {}".format(array))
a = array[1 : 4]
print("array[1 : 4]: {}".format(a))
b = array[0 : 8]
print("array[0 : 8]: {}".format(b))
c = array[6 : ]
print("array[6 : ]: {}".format(c))
d = array[ : 5]
print("array[ : 5]: {}".format(d))


e = array[0 : 15]
print("array[0 : 15]: {}".format(e))


# append

list_a = [1,2,3]

print("list_a:{}".format(list_a))

list_a.append(23)

print("list_a:{}".format(list_a))

list_a.append([45,6,7,9])

print("list_a:{}".format(list_a))

list_a = list_a + [45,6,7,9]

print("list_a:{}".format(list_a))

# using + operator to join lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print("all_numbers=%s" % all_numbers)

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator
my_list = [1,2,3] * 5
print("my_list=%s" % my_list)

# list comprehension
# syntax -> newlist = [expression for item in iterable if condition == True]
sentence = "the quick brown fox jumps over the lazy dog, over"
words = sentence.split()
modified_words = [word for word in words if word not in ["the","over"]]
print("words:", words)
print("modified_words:", modified_words)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
modified_words = [word if word != "lazy" else "tonga" for word in words if word not in ["the","over"]]
print("words:", words)
print("modified_words:", modified_words)

# remove elements from list during iteration

my_names = ["lau","lau1","lau2","lau3","lau4"]

print("my_names:", my_names)

for name in my_names:
    print("name:{}".format(name))
    if name in ["lau1","lau3"]:
        my_names.remove(name)

print("my_names:", my_names)