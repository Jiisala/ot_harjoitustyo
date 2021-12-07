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
        self.test_user2 = User("name2", "pw2")
        self.test_problem = (
            Problem("testname", self.test_user, "grade", "location", "descr", "img_url"))
        self.test_user_repo = users
        self.test_user_repo.add_user(self.test_user)
        self.test_user_repo.add_user(self.test_user2)

    def reset_db_between_tests(self):
        init_db()
        self.test_user_repo.add_user(self.test_user)
        self.test_user_repo.add_user(self.test_user2)

    def test_add_problem_adds_problem(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(
            Problem("name", self.test_user, "grade", "location", "descr", "img_url"))

        self.assertEqual(len(self.test_repo.get_problems()), 1)

    def test_add_problem_adds_problem_many_times(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(
            Problem("name1", self.test_user, "grade", "location", "descr", "img_url"))
        self.test_repo.add_problem(
            Problem("name2", self.test_user, "grade", "location", "descr", "img_url"))
        self.test_repo.add_problem(
            Problem("name3", self.test_user, "grade", "location", "descr", "img_url"))
        self.assertEqual(len(self.test_repo.get_problems()), 3)

    def test_no_problems_with_same_name(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(
            Problem("name", self.test_user, "grade", "location", "descr", "img_url"))
        self.test_repo.add_problem(
            Problem("name", self.test_user, "grade", "location", "descr", "img_url"))

        self.assertEqual(len(self.test_repo.get_problems()), 1)

    def test_add_problem_to_uxp_adds_problem_to_uxp(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(self.test_problem)

        self.test_repo.add_to_uxp(self.test_problem, self. test_user2)
        self.assertEqual(
            len(self.test_repo.get_problems_for_user(self.test_user2)), 1)

    def test_add_remove_from_uxp_removes_problem_from_uxp(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(self.test_problem)

        self.test_repo.add_to_uxp(self.test_problem, self. test_user2)
        first_len = len(self.test_repo.get_problems_for_user(self.test_user2))
        self.test_repo.remove_problem_from_uxp(
            self.test_problem, self.test_user2)
        self.assertNotEqual(
            len(self.test_repo.get_problems_for_user(self.test_user2)), first_len)

    def test_mark_solved_works(self):
        self.reset_db_between_tests()
        self.test_repo.add_problem(self.test_problem)

        self.test_repo.add_to_uxp(self.test_problem, self. test_user2)

        unsolved = self.test_repo.get_problems_for_user(self.test_user2)[0][1]
        self.test_repo.mark_solved(1, self.test_problem, self.test_user2)
        solved = self.test_repo.get_problems_for_user(self.test_user2)[0][1]
        self.test_repo.mark_solved(0, self.test_problem, self.test_user2)
        unsolved_again = self.test_repo.get_problems_for_user(self.test_user2)[
            0][1]
        self.assertEqual(unsolved, 0)
        self.assertEqual(solved, 1)
        self.assertEqual(unsolved_again, 0)
