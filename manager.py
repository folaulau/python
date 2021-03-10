import user

class Manager(user.User):

    def __init__(self, name, age, active):
        # call super() function
        super().__init__(name, age)
        self._active = True
        print("Manager is ready")

    def is_active(self):
        return self._active

class CTO(user.User):

    def __init__(self, name, age, active):
        # call super() function
        super().__init__(name, age)
        self._active = True
        print("Manager is ready")

    def is_active(self):
        return self._active