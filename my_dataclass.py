from dataclasses import dataclass, fields
from datetime import datetime

@dataclass
class User(object):
    
    insert_id: int

    def __init__(self, **kwargs):
        self.first_name: str = kwargs.get('first_name')
        self.last_name: str =kwargs.get('last_name')
        self.email: str = kwargs.get('email')


u1 = {'first_name': 'folau','email':'fkaveinag@gmail.com'}
user1 = User(**u1)
user1.first_name='folau'
User.insert_id = 2
user2 = User(first_name="hey")
user3 = User()

print("user2.insert_id:{}".format(user2.insert_id))
print("user2.first_name:{}".format(user2.first_name))
print("user2.__dict__:{}".format(user2.__dict__.keys()))

print("user1:{}".format(user1.__dict__))
print("user2:{}".format(user2.__dict__))
print("user3:{}".format(user3.__dict__))

# for field in user1:
#     print("field:{}".format(field))