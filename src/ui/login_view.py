from tkinter import ttk
from repositories.users import Users
from services.logic import  logic


class LoginView:

    def __init__(self, root, goto_new_user_view, goto_show_main_view) -> None:
        self._root = root
        self._goto_show_new_user_view = goto_new_user_view
        self._goto_show_main_view = goto_show_main_view
        self._frame = None
        

       # self._root.configure(background= "black")

        self._start()

    def destroy(self):
        self._frame.destroy()
    
    def _login_button_func(self):
        name = self.user_name_field.get()
        pw = self.pw_field.get()
       # print ("name", name, "pw", pw)
        if logic.login(name,pw):
            self._goto_show_main_view()
        else:
            print("Here we will figure out that user name or password is wrong")

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        label = ttk.Label(master=self._frame, text="Welcome ")
        user_name_label = ttk.Label(master=self._frame, text="Name:")
        pw_label = ttk.Label(master=self._frame, text="Password:")

        self.user_name_field = ttk.Entry(master=self._frame)
        self.pw_field = ttk.Entry(master=self._frame, show="*")

        sign_in_button = ttk.Button(
            master=self._frame,
            text="Log in",
            command=self._login_button_func 
        )

        new_user_button = ttk.Button(
            master=self._frame,
            text="New user",
            command=self._goto_show_new_user_view)

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        user_name_label.grid(row=2, column=0, padx=5, pady=5)
        self.user_name_field.grid(row=2, column=1, padx=5, pady=5)
        pw_label.grid(row=3, column=0, padx=5, pady=5)
        self.pw_field.grid(row=3, column=1, padx=5, pady=5)
        sign_in_button.grid(row=4, column=0, padx=5, pady=5)
        new_user_button.grid(row=4, column=1, padx=5, pady=5, sticky="E")

        self._frame.pack()
