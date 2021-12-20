from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import UnidentifiedImageError
from services.logic import logic




class NewProblemView:
    """view for creating new problems.
    """

    def __init__(self, root, goto_main_view) -> None:
        self._root = root

        self._goto_main_view = goto_main_view

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _new_problem_button_funct(self):
        """functionality to create new problem. Name restricted to 25 characters, because too long names break the UI
        If UI gets re-done, restriction can be removed.
        """
        
        name = self._problem_name_field.get()
        if len(name) > 25:
            self.message_label["text"] = "Name too long, please use less than 25 characters"
            return
        grade = self._grade_field.get()
        location = self._location_field.get()
        description = self._description_field.get()
        img_url = f"./data/img/{self._img_name_label['text']}"

        if len(name) == 0:
            self.message_label["text"] = "Please give your problem a name"

        else:
            try:
                logic.new_problem(name, grade, location, description, img_url)
                self.message_label["text"] = f"Problem {name} created succesfully"
            except ValueError:
                self.message_label["text"] = f"Problem named {name} already exists."

    def _select_image_button_funct(self):
        """This will open system dialg for selecting file and send the path of selected file to logic.handle_img_path.
           If selected file was image of supported type, it will insert name of the image to corresponding label
        """

        img_path = askopenfilename()
        img_name = self._img_name_label["text"]
        try:
            img_name = logic.handle_img_path(img_path)
        except UnidentifiedImageError:
            self.message_label["text"] = "Image filetype not supported. Please use .gif, .png, .jpg, jpeg or .bmp"
            pass
       
        self._img_name_label["text"] = img_name

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)

        label = ttk.Label(master=self._frame,
                          text="Lets get creating")
        self.message_label = ttk.Label(master=self._frame,
                                       text="")
        problem_name_label = ttk.Label(master=self._frame, text="Name:")
        grade_label = ttk.Label(master=self._frame, text="Grade:")
        location_label = ttk.Label(master=self._frame, text="Location")
        description_label = ttk.Label(master=self._frame, text="Description:")
        img_label = ttk.Label(master=self._frame, text="img:")

        self._problem_name_field = ttk.Entry(master=self._frame)
        self._grade_field = ttk.Entry(master=self._frame)
        self._location_field = ttk.Entry(master=self._frame)
        self._description_field = ttk.Entry(master=self._frame)
        self._img_name_label = ttk.Label(master=self._frame, text="kivi.gif")
        
        self._img_button = ttk.Button(
            master=self._frame, text="Select image", command=self._select_image_button_funct)

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

        label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.message_label.grid(row=1, columnspan=3, column=0, padx=5, pady=5)
        problem_name_label.grid(row=2, column=0, padx=5, pady=5)
        self._problem_name_field.grid(row=2, column=1, padx=5, pady=5)
        grade_label.grid(row=3, column=0, padx=5, pady=5)
        self._grade_field.grid(row=3, column=1, padx=5, pady=5)
        location_label.grid(row=4, column=0, padx=5, pady=5)
        self._location_field.grid(row=4, column=1, padx=5, pady=5)
        description_label.grid(row=5, column=0, padx=5, pady=5)
        self._description_field.grid(row=5, column=1, padx=5, pady=5)
        img_label.grid(row=6, column=0, padx=5, pady=5)
        self._img_name_label.grid(row=6, column=1, padx=5, pady=5)
        self._img_button.grid(row=6, column=2)

        create_button.grid(row=7, column=0, padx=5, pady=5)
        back_button.grid(row=7, column=1, padx=5, pady=5, sticky="E")

        self._frame.pack()
