from tkinter import  ttk

from services.logic import logic
import textwrap

class MainView:

    def __init__(self, root) -> None:
        
        self._root = root

        self._frame = None

        self._start()

    def destroy(self):
        self._frame.destroy()
    #For wrappig long lines in column
    def _wrap(self, string, length =20):
        return "\n".join(textwrap.wrap(string, length))
   
    def create_problem_frame(self, problem):
        #Maybe I should create a "main frame" and then a different frame for each problem. 
        p_frame = ttk.Frame(master= self._frame)
        
        p_label = ttk.Label(master= p_frame,
        text= "NAME: jokunimi\nAUTHOR: Essi Merkkinen\nGRADE: 6A\nLOCATION: ongemlapaikka joka on ihan kiva paikka", 
        borderwidth=2, 
        relief="ridge" 
        )
        
        p_label2 = ttk.Label(master= p_frame,
        text= self._wrap("DESCRIPTION: Kuvaus voi olla vaikka kuinka kivasti pitkäkin koska tässä käytetään nyt sitä wrappia ja se ei niin haittaa "),
        borderwidth=2, 
        relief="ridge"
        )

        p_label3 = ttk.Label(master= p_frame, text= "tähän tulee kuva", 
        borderwidth=2, 
        relief="ridge"
        )

        done_radio = ttk.Radiobutton(master=p_frame,
        text="SOLVED!")
        done_radio.grid(row =0, column=1, padx=5, pady=5)
        p_label.grid(row=0, column=2, padx=5, pady=5)
        p_label2.grid(row=0, column=3, padx=5, pady=5)
        p_label3.grid(row=0, column=4, padx=5, pady=5)
        return p_frame    
    
    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        #self._frame.grid_columnconfigure(1, weight=1)
        self._frame.configure(padding=15)
        
        self._p_frame = self.create_problem_frame("ongelma")
        
        header_label = ttk.Label(
            master=self._frame,
            text=f"Hello {logic.get_user().get_name()}",
            font="courier 20")
        separator = ttk.Separator(master=self._frame, orient="horizontal") #So, this does not work, find out why 
       
        create_problem_button = ttk.Button(
            master=self._frame,
            text="New problem",
            command= None
        ) 
        view_all_button = ttk.Button(
            master=self._frame,
            text="Browse problems",
            command= None
        ) 
        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        separator.grid(row=1, column=0, columnspan=2)
        self._p_frame.grid(row=2, column=0, columnspan= 2, padx=5, pady=5)
        create_problem_button.grid(row=3, column=0, padx=5, pady=5)
        view_all_button.grid(row=3, column=1, padx=3, pady=5)
       

        self._frame.pack()
