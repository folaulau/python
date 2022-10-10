data = b'GeeksForGeeks'
 
# display input
print('\nInput:')
print(data)
print(type(data))
print("data: {}".format(str(data)))
 
# converting
output = data.decode()
 
# display output
print('\nOutput:')
print(output)
print(type(output))

if type(data).__name__ == 'bytes':
    print("is byte type")

if isinstance(data, bytes):
    print("is byte typesss")