from sqlite3.dbapi2 import DatabaseError
from tkinter import ttk
from services.logic import logic


class LoginView:
    """Login view, nothing too complicated here
    """

    def __init__(self, root, goto_new_user_view, goto_show_main_view):
        self._root = root
        self._goto_show_new_user_view = goto_new_user_view
        self._goto_show_main_view = goto_show_main_view
        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _login_button_action(self):
        name = self.user_name_field.get()
        pw = self.pw_field.get()
        try:
            logic.login(name, pw)
            self._goto_show_main_view()
        except ValueError:
            self.message_label["text"] = "Wrong username or password"
        except DatabaseError:
            self.message_label["text"] = "Faulty database, reinitialize database and launch program again"

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        label = ttk.Label(master=self._frame, text="Welcome ")
        self.message_label = ttk.Label(master=self._frame, text="")
        user_name_label = ttk.Label(master=self._frame, text="Name:")
        pw_label = ttk.Label(master=self._frame, text="Password:")

        self.user_name_field = ttk.Entry(master=self._frame)
        self.pw_field = ttk.Entry(master=self._frame, show="*")

        sign_in_button = ttk.Button(
            master=self._frame,
            text="Log in",
            command=self._login_button_action
        )

        new_user_button = ttk.Button(
            master=self._frame,
            text="New user",
            command=self._goto_show_new_user_view)

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.message_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        user_name_label.grid(row=2, column=0, padx=5, pady=5)
        self.user_name_field.grid(row=2, column=1, padx=5, pady=5)
        pw_label.grid(row=3, column=0, padx=5, pady=5)
        self.pw_field.grid(row=3, column=1, padx=5, pady=5)
        sign_in_button.grid(row=4, column=0, padx=5, pady=5)
        new_user_button.grid(row=4, column=1, padx=5, pady=5, sticky="E")

        self._frame.pack()
