from role_type import Role_Type

class User:

    def __init__(self, email, password, full_name):
        self.email = email
        self.password = password
        self.full_name = full_name
        self.role = Role_Type.basic
