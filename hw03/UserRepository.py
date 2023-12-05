from hw03 import User


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        if user.is_authenticate:
            self.users.append(user)

    def logout_non_admins(self) -> None:
        for i in self.users:
            if not i.is_admin:
                i.logout()
