import unittest

from init_db import init_db
from services.logic import logic

class TestLogic(unittest.TestCase):

    def setUp(self):
        
        self.test_logic = logic
        
        

    def reset_db_between_tests(self):
        init_db()
       

    def test_new_user_adds_user(self):
        
        self.reset_db_between_tests()
        self.assertTrue(self.test_logic.new_user("name", "password"))
    
    def test_no_users_with_same_name(self):
        
        self.reset_db_between_tests()
        self.test_logic.new_user("name","password")
        self.assertFalse(self.test_logic.new_user("name", "password"))

    def test_login_works(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name","password")
        self.test_logic.login("name","password")
        self.assertEqual(self.test_logic.current_user.name, "name")

    def test_login_wont_work_with_false_password(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name","password")
        self.test_logic.login("name","notpassword")
        self.assertEqual(self.test_logic.current_user, None)     

    def test_login_wont_work_with_false_name(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name","password")
        self.test_logic.login("notname","password")
        self.assertEqual(self.test_logic.current_user, None)         
        

    