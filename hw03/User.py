class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.is_authenticate = False

    def authenticate(self, username, password):
        return (username == self.username) and (password == self.password)

    def logout(self):
        self.is_authenticate = False

    def login(self):
        self.is_authenticate = True
