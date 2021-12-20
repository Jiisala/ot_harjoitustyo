
from tkinter import Canvas, OptionMenu, ttk, Scrollbar, StringVar
from PIL import Image, ImageTk
from services.logic import logic
import textwrap


class MainView:
    """As the title says, program main view

    Attributes:
        Attributes related to view changing are propably self expalanary.
        Self._sort_bool boolean used to decide if sorting should be reversed or not.
    """

    def __init__(self, root, goto_new_problem_view, goto_all_problems_view, goto_log_in_view) -> None:

        self._root = root
        self._goto_new_problem_view = goto_new_problem_view
        self._goto_all_problems_view = goto_all_problems_view
        self._goto_log_in_view = goto_log_in_view
        self._sort_bool = False

        self._start()

    def destroy(self):
        self.container_frame.destroy()

    def _wrap(self, string, length=40):
        """Helper function for text wrapping

        Args:
            string (Str): String to wrap
            length (int, optional): length of a line. Defaults to 40.

        Returns:
            String: String, wrapped so that maximun line length is length given
        """
        return "\n".join(textwrap.wrap(string, length))

    def _sort_by_key(self, problems):
        """Helper function for sorting the list of problems

        Args:
            problems (list):  List of tuples. tuple[0]= problem entitity, tuple[1] = one or zero indicating solved or not.

        Returns: sorted list
        """
        def sort_order(problem):
            key = self.var.get()
            if key != "Sort by":
                return problem[1], getattr(problem[0], key)
            return problem[1], problem[0].name
        return sorted(problems, key=sort_order, reverse=self._sort_bool)

    def create_problems_frame(self):
        self._main_p_frame = ttk.Frame(master=self._frame)
        problems = logic.get_problems_for_user()
        i = 0
        problems = self._sort_by_key(problems)
        for problem in problems:

            p_frame = self.create_individual_problem_frame(problem)
            p_frame.grid(row=i, column=0, columnspan=2,
                         padx=5, pady=5, sticky="W")
            i += 1

        return self._main_p_frame

    def show_image(self, img_url):
        """Shows fullsized image in system default image viewer"""
        with Image.open(img_url) as pic:
            pic.show()

    def create_individual_problem_frame(self, problem_with_solved):
        problem = problem_with_solved[0]
        solved_or_not = "SOLVED!" if problem_with_solved[1] == 1 else "unsolved"

        picture = ImageTk.PhotoImage(Image.open(
            logic.get_path_to_thumbnail(problem.img_url)))
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

        p_label3 = ttk.Label(master=p_frame, image=picture,
                             borderwidth=2,
                             relief="ridge"
                             )
        p_label3.photo = picture
        p_label3.bind("<Button-1>", lambda e: self.show_image(problem.img_url))

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

    def sort_button_action(self, button):

        if button["text"] == "Sort v":
            button["text"] = "sort ^"
            self._sort_bool = True

        else:
            button["text"] = "Sort v"
            self._sort_bool = False

        new_frame = self.create_problems_frame()
        new_frame.grid(row=2, column=0, columnspan=2,
                       padx=5, pady=5, sticky="W")

    def log_out_button_action(self):
        logic.log_out()
        self._goto_log_in_view()

    def create_dropdown(self):
        OPTIONS = ["Sort by", "name", "grade", "author", "location"]
        self.var = StringVar(master=self._frame)
        self.var.set(OPTIONS[0])
        dropdown = OptionMenu(self._frame, self.var, *OPTIONS)
        return dropdown

    def _start(self):
        self.container_frame = ttk.Frame(master=self._root)
        canvas = Canvas(master=self.container_frame)
        sb = Scrollbar(master=self.container_frame,
                       orient="vertical", command=canvas.yview)
        self._frame = ttk.Frame(master=canvas)
        self._frame.configure(padding=15)
        self._frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self._frame, anchor="nw")
        canvas.configure(yscrollcommand=sb.set, width=1200, height=800)

        self.dropdown = self.create_dropdown()
        self._p_frame = self.create_problems_frame()

        header_label = ttk.Label(
            master=self._frame,
            text=f"Hello {logic.current_user.name}",
            font="courier 20")

        create_problem_button = ttk.Button(
            master=self._frame,
            text="New problem",
            command=self._goto_new_problem_view
        )
        sort_button = ttk.Button(
            master=self._frame,
            text="Sort v",
            command=lambda: self.sort_button_action(sort_button)
        )
        view_all_button = ttk.Button(
            master=self._frame,
            text="Browse problems",
            command=self._goto_all_problems_view
        )
        log_out_button = ttk.Button(
            master=self._frame,
            text="Log out",
            command=self.log_out_button_action
        )
        header_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.dropdown.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        sort_button.grid(row=1, column=1,  padx=5, pady=5, sticky="W")
        self._p_frame.grid(row=2, column=0, columnspan=3,
                           padx=5, pady=5, sticky="EW")
        create_problem_button.grid(row=3, column=0, padx=5, pady=5, sticky="W")
        view_all_button.grid(row=3, column=1, padx=3, pady=5, sticky="W")
        log_out_button.grid(row=3, column=2, padx=3, pady=5, sticky="W")

        canvas.grid(row=0, column=0)
        sb.grid(row=0, column=1, sticky="ENS")
        self.container_frame.pack()
