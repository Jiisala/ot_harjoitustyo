from tkinter import ttk
from services.logic import logic


class NewUserView:

    def __init__(self, root, goto_login_view, goto_main_view) -> None:
        self._root = root
        self._goto_login_view = goto_login_view
        self._goto_main_view = goto_main_view
        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _new_user_button_funct(self):
        name = self._user_name_field.get()
        pw = self._pw_field.get()
        pw_check = self._pw_check_field.get()
        if len(name) == 0 or len(pw) == 0:
            print("This will do a thing later on when I get around implementing it")
        elif pw != pw_check:
            print(
                "here we check if pasword and pasword_check match, error handlig to be implemented")
        else:
            # Remember to add try/catch here also
            if logic.new_user(name, pw):
                logic.login(name, pw)
                self._goto_main_view()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        label = ttk.Label(master=self._frame,
                          text="Pleased to meet you, who ever you are")

        user_name_label = ttk.Label(master=self._frame, text="Name:")
        pw_label = ttk.Label(master=self._frame, text="Password:")
        pw_check_label = ttk.Label(master=self._frame, text="Password again:")
        self._user_name_field = ttk.Entry(master=self._frame)
        self._pw_field = ttk.Entry(master=self._frame, show="*")
        self._pw_check_field = ttk.Entry(master=self._frame, show="*")

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._new_user_button_funct
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._goto_login_view
        )

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        user_name_label.grid(row=2, column=0, padx=5, pady=5)
        self._user_name_field.grid(row=2, column=1, padx=5, pady=5)
        pw_label.grid(row=3, column=0, padx=5, pady=5)
        self._pw_field.grid(row=3, column=1, padx=5, pady=5)
        pw_check_label.grid(row=4, column=0, padx=5, pady=5)
        self._pw_check_field.grid(row=4, column=1, padx=5, pady=5)
        create_button.grid(row=5, column=0, padx=5, pady=5)
        back_button.grid(row=5, column=1, padx=5, pady=5, sticky="E")

        self._frame.pack()
