from tkinter import ttk


class MainView:

    def __init__(self, root) -> None:
        
        self._root = root

        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        #self._frame.grid_columnconfigure(1, weight=1)

        self._frame.configure(padding=15)

        label = ttk.Label(
            master=self._frame,
            text="Hello current user",
            font="courier 20")

        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self._frame.pack()
