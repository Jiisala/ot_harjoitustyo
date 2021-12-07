from tkinter import ttk

from services.logic import logic
import textwrap


class MainView:

    def __init__(self, root, goto_new_problem_view, goto_all_problems_view, goto_log_in_view) -> None:

        self._root = root
        self._goto_new_problem_view = goto_new_problem_view
        self._goto_all_problems_view = goto_all_problems_view
        self._goto_log_in_view = goto_log_in_view
        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _wrap(self, string, length=40):
        return "\n".join(textwrap.wrap(string, length))

    def create_problems_frame(self):
        self._main_p_frame = ttk.Frame(master=self._frame)
        problems = logic.get_problems_for_user()

        i = 0
        for problem in problems:

            p_frame = self.create_individual_problem_frame(problem)
            p_frame.grid(row=i, column=0, columnspan=2,
                         padx=5, pady=5, sticky="W")
            i += 1

        return self._main_p_frame

    def create_individual_problem_frame(self, problem_with_solved):
        problem = problem_with_solved[0]
        solved_or_not = "SOLVED!" if problem_with_solved[1] == 1 else "unsolved"

        p_frame = ttk.Frame(master=self._main_p_frame)

        p_label = ttk.Label(master=p_frame,
                            text=f"NAME: {problem.name}\nAUTHOR: {problem.author}\nGRADE: {problem.grade}",
                            borderwidth=2,
                            relief="ridge"
                            )
        p_label1 = ttk.Label(master=p_frame,
                             text=self._wrap(f"LOCATION: {problem.location}"),
                             borderwidth=2,
                             relief="ridge"
                             )

        p_label2 = ttk.Label(master=p_frame,
                             text=self._wrap(
                                 f"DESCRIPTION: {problem.description}"),
                             borderwidth=2,
                             relief="ridge"
                             )

        p_label3 = ttk.Label(master=p_frame, text=f"tähän tulee kuva {problem.img_url}",
                             borderwidth=2,
                             relief="ridge"
                             )

        done_button = ttk.Button(master=p_frame,
                                 text=solved_or_not,
                                 command=lambda: self.done_button_action(problem, done_button))

        done_button.grid(row=0, column=1, padx=5, pady=5)
        p_label.grid(row=0, column=2, padx=5, pady=5)
        p_label1.grid(row=0, column=3, padx=5, pady=5)
        p_label2.grid(row=0, column=4, padx=5, pady=5)
        p_label3.grid(row=0, column=5, padx=5, pady=5)
        return p_frame

    def done_button_action(self, problem, button):
        value = 0
        if button["text"] == "unsolved":
            button["text"] = "SOLVED!"
            value = 1
        else:
            button["text"] = "unsolved"
        logic.mark_solved(value, problem)

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        #self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        self._p_frame = self.create_problems_frame()

        header_label = ttk.Label(
            master=self._frame,
            text=f"Hello {logic.current_user.name}",
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
            command=self._goto_all_problems_view
        )
        log_out_button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self._goto_log_in_view
        )
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        separator.grid(row=1, column=0, columnspan=2)
        self._p_frame.grid(row=2, column=0, columnspan=2,
                           padx=5, pady=5, sticky="W")
        create_problem_button.grid(row=3, column=0, padx=5, pady=5, sticky="W")
        view_all_button.grid(row=3, column=1, padx=3, pady=5, sticky="W")
        log_out_button.grid(row=3, column=2, padx=3, pady=5, sticky="W")

        self._frame.pack()
