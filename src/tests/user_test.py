import unittest
from repositories.users import users
from entities.user import User
from init_db import init_db


class TestUsers(unittest.TestCase):
    """Collection of tests testing the user entity, and related database operations. 
    
    """
    def setUp(self):
        self.test_repo = users
        
    
    def reset_db_between_tests(self):
        init_db()
    
    def test_add_user_adds_user(self):
        self.reset_db_between_tests()
        self.test_repo.add_user(User("name", "pw"))
        # (this is 2 because I added a test user, change later)
        self.assertEqual(len(self.test_repo.get_users()), 2)
    
    def test_add_user_adds_user_many_times(self):
        self.reset_db_between_tests()
        self.test_repo.add_user(User("name1", "pw"))
        self.test_repo.add_user(User("name2", "pw"))
        self.test_repo.add_user(User("name3", "pw"))
        # (this is 4 because I added a test user, change later)
        self.assertEqual(len(self.test_repo.get_users()), 4)
    
    def test_no_users_with_same_name(self):
        self.reset_db_between_tests()
        self.test_repo.add_user(User("name", "pw"))
        self.test_repo.add_user(User("name", "pw"))
        # (this is 2 because I added a test user, change later)
        self.assertEqual(len(self.test_repo.get_users()), 2)
    
   