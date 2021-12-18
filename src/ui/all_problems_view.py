from tkinter import ttk, Canvas, Scrollbar, OptionMenu, StringVar, PhotoImage
from PIL import Image, ImageTk

from services.logic import logic
import textwrap


class AllProblemsView:
    """View for viewing all problems created by all users

    Attributes:
        Attributes related to view changing are propably self expalanary.
        Self._sort_bool boolean used to decide if sorting should be reversed or not.
    """

    def __init__(self, root, goto_main_view) -> None:

        self._root = root
        self._goto_main_view = goto_main_view
        self._frame = None
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
            String: String wrapped so that maximun line length is length ginven
        """
        return "\n".join(textwrap.wrap(string, length))

    def _sort_by_key(self, problems):
        """Helper function for sorting the list of problems

        Args:
            problems (list):  list of problem entities.

        Returns: sorted list
        """

        def sort_order(problem):
            tagged = 1 if self.check_uxp(
                problem) else 0
            key = self.var.get()
            if key != "Sort by":
                return tagged, getattr(problem, key)
            return tagged, problem.name
        return sorted(problems, key=sort_order, reverse=self._sort_bool)

    def create_problems_frame(self):
        self._main_p_frame = ttk.Frame(master=self._frame)
        problems = logic.get_all_problems()

        i = 0
        problems = self._sort_by_key(problems)
        for problem in problems:

            p_frame = self.create_individual_problem_frame(problem)
            p_frame.grid(row=i, column=0, columnspan=2,
                         padx=5, pady=5, sticky="W")
            i += 1

        return self._main_p_frame

    def check_uxp(self, problem):
        """calls function from main logic in order to find if user already tagged a particular problem 

        Args:
            problem (problem): problem entity to check

        Returns:
            Boolean: Tagged or not
        """
        checklist = logic.get_problems_for_user()
        for part in checklist:
            if part[0].name == problem.name:

                return True
        return False

    def show_image(self, img_url):
        """Shows fullsized image in system default image viewer"""
        with Image.open(img_url) as pic:
            pic.show()

    def create_individual_problem_frame(self, problem):

        p_frame = ttk.Frame(master=self._main_p_frame)
        tagged_or_untagged = "TAGGED!" if self.check_uxp(
            problem) else "untagged"
        picture = ImageTk.PhotoImage(Image.open(
            logic.get_path_to_thumbnail(problem.img_url)))

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
            text=f"Tag some problems for you to solve",
            font="courier 20")

        sort_button = ttk.Button(
            master=self._frame,
            text="Sort v",
            command=lambda: self.sort_button_action(sort_button)
        )

        main_view_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._goto_main_view
        )

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.dropdown.grid(row=1, column=0)
        sort_button.grid(row=1, column=1)
        self._p_frame.grid(row=2, column=0, columnspan=2,
                           padx=5, pady=5, sticky="EW")
        main_view_button.grid(row=3, column=0, padx=5, pady=5, sticky="W")

        canvas.grid(row=0, column=0)
        sb.grid(row=0, column=1, sticky="ENS")
        self.container_frame.pack()
