msg = "Hello World"

print(msg)


class User:
    is_admin = False

    def __init__(self, user_name):
        self.username = user_name


class Admin(User):
    is_admin = True
