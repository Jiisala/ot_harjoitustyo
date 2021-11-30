from tkinter import ttk
from services.logic import logic


class NewProblemView:

    def __init__(self, root, goto_main_view) -> None:
        self._root = root

        self._goto_main_view = goto_main_view
        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _new_problem_button_funct(self):
        name = self._problem_name_field.get()
        grade = self._grade_field.get()
        location = self._location_field.get()
        description = self._description_field.get()
        img_url = self._img_field.get()

        if len(name) == 0:
            print("This will do a thing later on when I get around implementing it")

        else:
            # Remember to add try/catch here also
           
            logic.new_problem(name, grade, location, description, img_url)
            

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        label = ttk.Label(master=self._frame,
                          text="Lets get creating")

        problem_name_label = ttk.Label(master=self._frame, text="Name:")
        grade_label = ttk.Label(master=self._frame, text="Grade:")
        location_label = ttk.Label(master=self._frame, text="Location")
        description_label = ttk.Label(master=self._frame, text="Description:")
        img_label = ttk.Label(master=self._frame, text="img:")

        self._problem_name_field = ttk.Entry(master=self._frame)
        self._grade_field = ttk.Entry(master=self._frame)
        self._location_field = ttk.Entry(master=self._frame)
        self._description_field = ttk.Entry(master=self._frame)
        self._img_field = ttk.Entry(master=self._frame)

        create_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._new_problem_button_funct
        )

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._goto_main_view
        )

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        problem_name_label.grid(row=2, column=0, padx=5, pady=5)
        self._problem_name_field.grid(row=2, column=1, padx=5, pady=5)
        grade_label.grid(row=3, column=0, padx=5, pady=5)
        self._grade_field.grid(row=3, column=1, padx=5, pady=5)
        location_label.grid(row=4, column=0, padx=5, pady=5)
        self._location_field.grid(row=4, column=1, padx=5, pady=5)
        description_label.grid(row=5, column=0, padx=5, pady=5)
        self._description_field.grid(row=5, column=1, padx=5, pady=5)
        img_label.grid(row=6, column=0, padx=5, pady=5)
        self._img_field.grid(row=6, column=1, padx=5, pady=5)

        create_button.grid(row=7, column=0, padx=5, pady=5)
        back_button.grid(row=7, column=1, padx=5, pady=5, sticky="E")

        self._frame.pack()
