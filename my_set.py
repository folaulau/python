
# Driver code

names = set()

names.add('folau')
names.add('lisa')
names.add('Folau')
names.add('lisa')

print("names:{}".format(names))


nums = {'1':[1,2,3],'2':[4,5,6]}

print("nums len:{}".format(len(nums)))

for num in nums:
    print("num:{}, nums={}".format(num,nums[num]))
