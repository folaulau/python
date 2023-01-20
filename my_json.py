import json

# json loads - converts json string to python dictionary

print("\nUsing json.loads\n")
# it must be single quotes outside and double quotes inside, the other way around does not work. 
#user =  "{ 'name':'John', 'age':30, 'city':'New York'}"

try:
    user =  "{ 'name':'John', 'age':30, 'city':'New York'}"

    json_user = json.loads(user)

    print("json_user={}, type={}".format(json_user, type(json_user)))
except Exception as e:
    print("You cannot json.loads json string that its fields are single quoted, exception, msg={}".format(e))

user =  '{ "name":"John", "age":30, "city":"New York"}'

json_user = json.loads(user)

print("json_user={}, type={}".format(json_user, type(json_user)))

print("\ntry json.dumps first and then json.loads\n")

# try json.dumps first and then json.loads
user =  "{ 'name':'John', 'age':30, 'city':'New York'}"

json_dumped_user = json.dumps(user)
print("json_dumped_user={}, type={}".format(json_dumped_user, type(json_dumped_user)))

json_loaded_user = json.loads(json_dumped_user)
print("json_loaded_user={}, type={}".format(json_loaded_user, type(json_loaded_user)))

print("\n\n")

user =  '{ "name":"John", "age":30, "city":"New York"}'

json_dumped_user = json.dumps(user)
print("json_dumped_user={}, type={}".format(json_dumped_user, type(json_dumped_user)))

json_loaded_user = json.loads(json_dumped_user)
print("json_loaded_user={}, type={}".format(json_loaded_user, type(json_loaded_user)))

print("\n\n")

# json dumps - python dictionary to string json

print("\nUsing json.dumps\n")

user = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("user={}, type={}".format(user, type(user)))

json_dumped_user = json.dumps(user)
print("json_dumped_user={}, type={}".format(json_dumped_user, type(json_dumped_user)))

try:
    json_loaded_user = json.loads(user)
except Exception as e:
    print("You cannot json.loads an already dictionary object, exception, msg={}".format(e))
