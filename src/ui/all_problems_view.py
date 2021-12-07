from tkinter import ttk

from services.logic import logic
import textwrap


class AllProblemsView:

    def __init__(self, root, goto_main_view) -> None:

        self._root = root
        self._goto_main_view = goto_main_view
        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _wrap(self, string, length=40):
        return "\n".join(textwrap.wrap(string, length))

    def create_problems_frame(self):
        self._main_p_frame = ttk.Frame(master=self._frame)
        problems = logic.get_all_problems()

        i = 0
        for problem in problems:

            p_frame = self.create_individual_problem_frame(problem)
            p_frame.grid(row=i, column=0, columnspan=2,
                         padx=5, pady=5, sticky="W")
            i += 1

        return self._main_p_frame

    def check_uxp(self, problem):
        checklist = logic.get_problems_for_user()
        for part in checklist:
            if part[0].name == problem.name:
                print(part[0], problem)
                return True
        return False

    def create_individual_problem_frame(self, problem):

        p_frame = ttk.Frame(master=self._main_p_frame)
        self.check_uxp(problem)
        tagged_or_untagged = "TAGGED!" if self.check_uxp(
            problem) else "untagged"  # HERE BE SOMETHING FISHY

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

        tag_button = ttk.Button(master=p_frame,
                                text=tagged_or_untagged,
                                command=lambda: self.tag_button_action(problem, tag_button))

        tag_button.grid(row=0, column=1, padx=5, pady=5)
        p_label.grid(row=0, column=2, padx=5, pady=5)
        p_label1.grid(row=0, column=3, padx=5, pady=5)
        p_label2.grid(row=0, column=4, padx=5, pady=5)
        p_label3.grid(row=0, column=5, padx=5, pady=5)
        return p_frame

    def tag_button_action(self, problem, button):

        if button["text"] == "untagged":
            button["text"] = "TAGGED!"
            logic.add_problem_to_uxp(problem)
        else:
            button["text"] = "untagged"
            logic.remove_problem_from_uxp(problem)

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        #self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        self._p_frame = self.create_problems_frame()

        header_label = ttk.Label(
            master=self._frame,
            text=f"Tag some problems for you to solve",
            font="courier 20")
        # So, this does not work, find out why
        separator = ttk.Separator(master=self._frame, orient="horizontal")

        main_view_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._goto_main_view
        )

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        separator.grid(row=1, column=0, columnspan=2)
        self._p_frame.grid(row=2, column=0, columnspan=2,
                           padx=5, pady=5, sticky="W")
        main_view_button.grid(row=3, column=0, padx=5, pady=5)

        self._frame.pack()
