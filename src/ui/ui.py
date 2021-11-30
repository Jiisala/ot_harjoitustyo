from ui.login_view import LoginView
from ui.new_user_view import NewUserView
from ui.main_view import MainView
from ui.new_problem_view import NewProblemView


class UI:

    def __init__(self, root) -> None:
        self._root = root
        self._view = None

    def run(self):
        self._show_login_view()

    def _show_login_view(self):
        self._reset_view()
        self._view = LoginView(
            self._root, self._show_new_user_view, self._show_main_view)

    def _show_new_user_view(self):
        self._reset_view()
        self._view = NewUserView(
            self._root, self._show_login_view, self._show_main_view)

    def _show_new_problem_view(self):
        self._reset_view()
        self._view = NewProblemView(
            self._root,  self._show_main_view)

    def _show_main_view(self):

        self._reset_view()
        self._view = MainView(self._root, self._show_new_problem_view)

    def _reset_view(self):
        if self._view:
            self._view.destroy()

        self._view = None
