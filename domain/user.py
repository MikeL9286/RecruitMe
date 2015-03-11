import role_type

class User:

    def __init__(self, email, password, full_name):
        self.email = email
        self.password = password
        self.full_name = full_name
        self.role = role_type.basic
        self.circle = []
        self.committed_teams = []