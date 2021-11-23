import unittest
from repositories.users import Users
from entities.user import User

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_repo = Users()
        
    def test_add_user_adds_user(self):
        self.test_repo.add_user(User("name", "pw"))
        self.assertEqual(len(self.test_repo.get_users()), 2) #(this is 2 because I added a test user, change later)
