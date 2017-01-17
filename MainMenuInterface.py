__author__ = 'Somma'

import tkinter
import fonctions


class MainMenuInterface(tkinter.Frame):
    """Document when finished"""

    def __init__(self, master=None):
        """Document when finished"""
        self.tone = 1
        self.answer = None
        self.answered = False
        self.playlist = {"empty": None}

        tkinter.Frame.__init__(self, master)

        for x in range(10):
            tkinter.Grid.columnconfigure(master, x, weight=1)
        for y in range(10):
            tkinter.Grid.rowconfigure(master, y, weight=1)
        self.grid(row=5, column=5)
        self.main_menu()

#_______________________________________________________________________________________________________________________

    def main_menu(self):
        """Document when finished"""

        def intervals_slot():
            """Document when finished"""
            fonctions.hide_stuff(intervals, chords, quit, title)
            self.intervals_menu()

        def chords_slot():
            """Document when finished"""
            fonctions.hide_stuff(intervals, chords, quit, title)
            self.chords_menu()

        #Configuring window
        self.master.title("CASULANA")
        self.master.geometry("300x120")
        self.master.configure(bg="black")

        #Creating buttons
        title = tkinter.Label(self, text="MENU", bg="lightblue", font=("Times", 12, "bold"))
        intervals = tkinter.Button(self, text="Intervalles", command=intervals_slot, highlightbackground="green")
        chords = tkinter.Button(self, text="Accords", command=chords_slot, highlightbackground="yellow")
        quit = tkinter.Button(self, text="Quit", command=self.master.destroy , highlightbackground="red")

        #placing the widgets in master
        title.grid(row=0, column=1,rowspan=1, sticky="wens")
        intervals.grid(row=1, column=1, sticky="wens")
        chords.grid(row=2, column=1, sticky="wens")
        quit.grid(row=3, column=1, sticky="wens")

#_______________________________________________________________________________________________________________________
