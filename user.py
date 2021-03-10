
"""
First python class
"""
class User():
    name = str
    age = int
    admin_type = "ADMIN"
    user_type = "USER"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    @classmethod
    def get_admin_role(cls):
        return "ROLE_"+cls.admin_type

    @staticmethod
    def get_user_role():
        return "ROLE_" + User.user_type
