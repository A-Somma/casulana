__author__ = 'Somma'
import tkinter
import fonctions
from Counter import Stat


class AnswerBox(tkinter.Button):
    """Document when finished"""

    def __init__(self, slot=None, name="", master=""):
        """Document when finished"""
        tkinter.Button.__init__(self, master, text=name, command=slot, highlightbackground="blue")
        self.name = name
        self.stat = Stat(name=name)

    def play(self, tone=None, answer=None, answered=False):
        """Document when finished"""
        fonctions.play(file="/Recordings/Intervalles/harmonic/"+(self.name.replace(" ", "_")).lower()+"/", number=tone)
        if answer != self.name and answered is False:
            self.configure(highlightbackground="red")
            return False
        else:
            return True

    def retrieve(self):
        """Document when finished"""
        return str(self.stat)
