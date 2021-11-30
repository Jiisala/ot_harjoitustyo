import unittest
from repositories.problems import problems
from repositories.users import users
from entities.problem import Problem
from entities.user import User
from init_db import init_db


class TestUsers(unittest.TestCase):
    """Collection of tests testing the problem entity, and related database operations. 
    
    """
    def setUp(self):
        """Setup, user repo needed to satisfy Foreign key constrains of the uxb table
        """
        self.test_repo = problems
        self.test_user = User("name", "pw")
        self.test_user_repo = users 
        self.test_user_repo.add_user(self.test_user)
    
    def reset_db_between_tests(self):
        init_db()
        self.test_user_repo.add_user(self.test_user)
    
    def test_add_problem_adds_problem(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(Problem("name", self.test_user, "grade", "location", "descr", "img_url"))
        
        self.assertEqual(len(self.test_repo.get_problems()), 1)
    
    def test_add_problem_adds_problem_many_times(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(Problem("name1", self.test_user, "grade", "location", "descr", "img_url"))
        self.test_repo.add_problem(Problem("name2", self.test_user, "grade", "location", "descr", "img_url"))
        self.test_repo.add_problem(Problem("name3", self.test_user, "grade", "location", "descr", "img_url"))
        self.assertEqual(len(self.test_repo.get_problems()), 3)
    
    
    def test_no_problems_with_same_name(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(Problem("name", self.test_user, "grade", "location", "descr", "img_url"))
        self.test_repo.add_problem(Problem("name", self.test_user, "grade", "location", "descr", "img_url"))
        
        self.assertEqual(len(self.test_repo.get_problems()), 1)
    
   