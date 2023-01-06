

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