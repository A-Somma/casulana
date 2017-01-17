__author__ = 'Somma'
import tkinter
import IntervalsStartInterface
import IntervalsOptionsInterface


class IntervalMenuInterface(tkinter.Frame):
    """Document when finished"""
    def __init__(self, restrict_list=[], playstyle="Hamonique", master=None):
        """Document when finished"""

        self.answer = None
        self.answered = False
        self.playstyle = playstyle
        self.restrict_list = restrict_list

        tkinter.Frame.__init__(self, master)

        for x in range(10):
            tkinter.Grid.columnconfigure(master, x, weight=1)
        for y in range(10):
            tkinter.Grid.rowconfigure(master, y, weight=1)
        self.grid(row=5, column=5)
        self.intervals_menu()

#____________________________________________________________________________________________________

    def intervals_menu(self):
        """Document when finished"""

        def commencer_slot():
            """Document when finished"""
            self.master.destroy()
            root = IntervalsStartInterface.tkinter.Tk()
            window = IntervalsStartInterface.IntervalsStartInterface(master=root, restrict_list=self.restrict_list,
                                                                     playstyle=self.playstyle)
            window.mainloop()

        def options_slot():
            """Document when finished"""
            self.master.destroy()
            root = IntervalsOptionsInterface.tkinter.Tk()
            window = IntervalsOptionsInterface.IntervalsOptionsInterface(master=root)
            window.mainloop()

        def quit_slot():
            """Document when finished"""
            self.master.destroy()

        self.master.title("CASULANA (v.1.02.m)")
        self.master.geometry("300x120")
        self.master.configure(bg="black")
        title = tkinter.Label(self, text="Intervalles", bg="lightblue", font=("Times", 12, "bold"))
        commencer = tkinter.Button(self, text="Commencer", command=commencer_slot, highlightbackground="green")
        options = tkinter.Button(self, text="Options", command=options_slot, highlightbackground="yellow")
        quitter = tkinter.Button(self, text="Quitter", command=self.master.destroy , highlightbackground="red")


        title.grid(row=0, column=1,rowspan=1, sticky="wens")
        commencer.grid(row=1, column=1, sticky="wens")
        options.grid(row=2, column=1, sticky="wens")
        quitter.grid(row=3, column=1, sticky="wens")
#____________________________________________________________________________________________________


