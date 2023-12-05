import unittest
from random import randint, shuffle
from User import User
from UserRepository import UserRepository


class LogoutTest(unittest.TestCase):
    def setUp(self):
        self.test_repo = UserRepository()
        user_list = ([User(f'user{i}', 'password', is_admin=True) for i in range(randint(1, 5))] +
                     [User(f'user{i}', 'password') for i in range(6, randint(6, 15))])
        shuffle(user_list)
        for user in user_list:
            user.login()
            self.test_repo.add_user(user)

    def test_logout_non_admin(self):
        self.test_repo.logout_non_admins()
        self.assertTrue(all(user.is_admin for user in self.test_repo.users if user.is_authenticate))
