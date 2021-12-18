import unittest

from PIL import UnidentifiedImageError
from entities.problem import Problem
from init_db import init_db
from services.logic import logic


class TestLogic(unittest.TestCase):

    def setUp(self):

        self.test_logic = logic

    def reset_db_between_tests(self):
        init_db()
        self.test_logic.log_out()

    def init_db_clears_database(self):
        """This isn not strictly speaking test for logic class, but gets tested here anyway
        """
        self.reset_db_between_tests()
        init_db()
        len_start_problems = len(self.test_logic.get_all_problems)
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        self.test_logic.new_problem(
            "name", "grade", "location", "descr", "img_url")
        self.assertEqual(len_start_problems + 1,
                         len(self.test_logic.get_all_problems))
        init_db()
        self.assertEqual(len_start_problems, len(
            self.test_logic.get_all_problems))

    def test_new_user_adds_user(self):

        self.reset_db_between_tests()
        self.assertTrue(self.test_logic.new_user("name", "password"))

    def test_no_users_with_same_name(self):

        self.reset_db_between_tests()

        with self.assertRaises(ValueError):
            self.test_logic.new_user("name", "password")
            self.test_logic.new_user("name", "password")

    def test_adding_new_problem_works(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        start_len = len(self.test_logic.get_all_problems())
        self.test_logic.new_problem(
            "name", "grade", "location", "descr", "img_url")
        self.assertEqual(
            len(self.test_logic.get_all_problems()), start_len + 1)

    def test_adding_multiple_problems_with_same_name_wont_work(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        with self.assertRaises(ValueError):
            self.test_logic.new_problem(
                "name", "grade", "location", "descr", "img_url")
            self.test_logic.new_problem(
                "name", "grade", "location", "descr", "img_url")

    def test_login_works(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        self.assertEqual(self.test_logic.current_user.name, "name")

    def test_login_wont_work_with_false_password(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        with self.assertRaises(ValueError):
            self.test_logic.login("name", "notpassword")

    def test_login_wont_work_with_false_name(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        with self.assertRaises(ValueError):
            self.test_logic.login("notname", "password")

    def test_log_out_works(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        self.test_logic.log_out()
        self.assertIsNone(self.test_logic.current_user)

    def test_add_to_uxp_adds_to_uxp(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        self.test_logic.new_problem(
            "name", "grade", "location", "descr", "img_url")
        self.test_logic.new_user("another_name", "password")
        self.test_logic.login("another_name", "password")

        start_len = len(self.test_logic.get_problems_for_user())
        self.test_logic.add_problem_to_uxp(
            Problem("name", "name", "grade", "location", "descr", "img_url"))
        self.assertEqual(
            start_len + 1, len(self.test_logic.get_problems_for_user()))

    def test_remove_from_uxp_removes_from_uxp(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        self.test_logic.new_problem(
            "name", "grade", "location", "descr", "img_url")
        self.test_logic.new_user("another_name", "password")
        self.test_logic.login("another_name", "password")
        self.test_logic.add_problem_to_uxp(
            Problem("name", "name", "grade", "location", "descr", "img_url"))
        start_len = len(self.test_logic.get_problems_for_user())
        self.test_logic.remove_problem_from_uxp(
            Problem("name", "name", "grade", "location", "descr", "img_url"))
        self.assertEqual(
            start_len - 1, len(self.test_logic.get_problems_for_user()))

    def test_user_exists_detects_if_user_exists(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.assertTrue(self.test_logic.check_user_exists("name"))
        self.assertFalse(self.test_logic.check_user_exists("another_name"))

    def test_mark_solved_works(self):
        self.reset_db_between_tests()
        self.test_logic.new_user("name", "password")
        self.test_logic.login("name", "password")
        self.test_logic.new_problem(
            "name", "grade", "location", "descr", "img_url")
        self.test_logic.mark_solved(1, Problem(
            "name", "name", "grade", "location", "descr", "img_url"))
        self.assertEqual(self.test_logic.get_problems_for_user()[0][1], 1)
        self.test_logic.mark_solved(0, Problem(
            "name", "name", "grade", "location", "descr", "img_url"))
        self.assertEqual(self.test_logic.get_problems_for_user()[0][1], 0)

    def test_handle_img_path_returns_img_name(self):
        self.reset_db_between_tests()
        self.assertEqual(self.test_logic.handle_img_path(
            "./data/img/kivi.png"), "kivi.png")

    def test_handle_img_path_accepts_only_img_formats(self):
        self.reset_db_between_tests()
        with self.assertRaises(UnidentifiedImageError):
            self.test_logic.handle_img_path("./data/img/kivi.wrong_format")

    def test_get_path_to_thumbnail_returns_correct_path(self):
        self.reset_db_between_tests()
        path = self.test_logic.get_path_to_thumbnail("test/path/image.jpg")
        self.assertEqual(path, "./data/img/image_thumbnail.jpg")
