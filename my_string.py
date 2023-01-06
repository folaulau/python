

from ipaddress import ip_address


def highlight_spotlight_finding(finding: str, start_pos: int):

    print("finding text: {}".format(finding))

    open_tick = -1
    
    try:
        open_tick = finding.find("`", start_pos)
    except:
        pass
    
    print("open_tick pos: {}".format(open_tick))

    if open_tick == -1:
        return finding

    close_tick = -1

    try:
        close_tick = finding.find("`", open_tick + 1)
    except:
        pass

    print("close_tick pos: {}".format(close_tick))

    if close_tick == -1:
        return finding

    begin_text = finding[:open_tick]

    highligh_text = finding[(open_tick+1):close_tick]

    highligh_text = '<span style="background-color: #ffff00; font-weight: bold;">'+ highligh_text +'</span>'

    end_text = finding[(close_tick+1):]
    
    print("highligh_text: {}".format(highligh_text))
    print("begin_text: {}".format(begin_text))
    

    new_text = begin_text+highligh_text+end_text
    
    print("new_text: {}".format(new_text))
    print("\n\n")

    if len(end_text) > 0:
        return highlight_spotlight_finding(new_text, close_tick)
    else:
        return new_text

text = "`I love you`, but I m`cant stand you`. Yeah yea yea, I cant x`hold it anymore`b. what you `think?"

highlighted_text = highlight_spotlight_finding(text,0)

print("\nhighlighted_text: {}".format(highlighted_text))



"""
split
"""

ip_address = '116.88.201.253, 165.225.112.156, 10.40.0.38'
ip_addresses = ip_address.split(", ")
ip_addr = ip_addresses[0]
print("ip_addr:{}".format(ip_addr))

ip_address = '116.88.201.253'
ip_addresses = ip_address.split(", ")
ip_addr = ip_addresses[0]
print("ip_addr1:{}".format(ip_addr))

ip_address = ''
ip_addresses = ip_address.split(", ")
ip_addr = ip_addresses[0]
print("ip_addr2:{}".format(ip_addr))


"""
convert string to bytes
"""

# initializing string 
test_string = "GFG is best"
  
# printing original string 
print("The original string : " + str(test_string))
  
# Using bytes(str, enc)
# convert string to byte 
res = bytes(test_string, 'utf-8')
  
# print result
print("The byte converted string is  : " + str(res) + ", type : " + str(type(res)))


# string format
# Any object which is not a string can be formatted using the %s operator as well.
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
name = "Folau"
age = 36
height = 103.3456
str_formatted = "name=%s, age=%s, height=%.2f" %(name, age, height)
print(str_formatted)

# string repeat sequence
# Python also supports multiplying strings to form a string with a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

#using double quotes makes it easy to include apostrophes
mystring = "Don't worry about apostrophes"
print(mystring)

# Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = "a", 4
print(a, b)




one = 1
two = 2
hello = "hello"

# This will not work!
try:
    print(one + two + hello)
except Exception as ex:
    print(ex)
# must convert one and two to str, like str(one)
print(str(one) + str(two) + hello)

# get character from string
hello = "hello"
#If you just have one number in the brackets, it will give you the single character at that index
print(hello[0])
print(hello.index("e"))

#If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in
print("hello[:3]=%s" % hello[:3])
#If you leave out the second number, it will give you a slice from the first number to the end
print("hello[3:]=%s" % hello[3:])

# substring
print(hello[2:4])

astring = "Hello world!"
print("astring=%s"%astring)
print("astring[3:7]=%s" % astring[3:7])
# [start:stop:step]
print("astring[3:7:2]=%s" % astring[3:7:2])
# reverse string
print(astring[::-1])

# string split
astring = "Hello world!"
afewwords = astring.split(" ")
print("afewwords=%s"%afewwords)