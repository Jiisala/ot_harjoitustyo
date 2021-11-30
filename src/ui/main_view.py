from tkinter import ttk

from services.logic import logic
import textwrap


class MainView:

    def __init__(self, root, goto_new_problem_view) -> None:

        self._root = root
        self._goto_new_problem_view = goto_new_problem_view
        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _wrap(self, string, length=20):
        return "\n".join(textwrap.wrap(string, length))

    def create_problems_frame(self):
        self._main_p_frame = ttk.Frame(master=self._frame)
        problems = logic.get_all_problems()  # CHANGE TO CURRENT USER LATER!
        i = 0
        for problem in problems:
            p_frame = self.create_individual_problem_frame(problem)
            p_frame.grid(row=i, column=0, columnspan=2,
                         padx=5, pady=5, sticky="W")
            i += 1

        return self._main_p_frame

    def create_individual_problem_frame(self, problem):

        p_frame = ttk.Frame(master=self._main_p_frame)

        p_label = ttk.Label(master=p_frame,
                            text=f"NAME: {problem.get_name()}\nAUTHOR: {problem.get_author()}\nGRADE: {problem.get_grade()}\nLOCATION: {problem.get_location()}",
                            borderwidth=2,
                            relief="ridge"
                            )

        p_label2 = ttk.Label(master=p_frame,
                             text=self._wrap(
                                 f"DESCRIPTION: {problem.get_description()}"),
                             borderwidth=2,
                             relief="ridge"
                             )

        p_label3 = ttk.Label(master=p_frame, text=f"tähän tulee kuva {problem.get_img_url()}",
                             borderwidth=2,
                             relief="ridge"
                             )

        done_radio = ttk.Radiobutton(master=p_frame,
                                     text="SOLVED!")
        done_radio.grid(row=0, column=1, padx=5, pady=5)
        p_label.grid(row=0, column=2, padx=5, pady=5)
        p_label2.grid(row=0, column=3, padx=5, pady=5)
        p_label3.grid(row=0, column=4, padx=5, pady=5)
        return p_frame

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        #self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        self._p_frame = self.create_problems_frame()

        header_label = ttk.Label(
            master=self._frame,
            text=f"Hello {logic.get_user().get_name()}",
            font="courier 20")
        # So, this does not work, find out why
        separator = ttk.Separator(master=self._frame, orient="horizontal")

        create_problem_button = ttk.Button(
            master=self._frame,
            text="New problem",
            command=self._goto_new_problem_view
        )
        view_all_button = ttk.Button(
            master=self._frame,
            text="Browse problems",
            command=None
        )
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        separator.grid(row=1, column=0, columnspan=2)
        self._p_frame.grid(row=2, column=0, columnspan=2,
                           padx=5, pady=5, sticky="W")
        create_problem_button.grid(row=3, column=0, padx=5, pady=5)
        view_all_button.grid(row=3, column=1, padx=3, pady=5)

        self._frame.pack()
