__author__ = 'Somma'
import fonctions
import random
import tkinter
import IntervalsMenuInterface
from tkinter import messagebox, StringVar
from AnswerBox import AnswerBox
from Counter import Stat


class IntervalsStartInterface(tkinter.Frame):
    """Document when finished"""
    def __init__(self, master=None, restrict_list=None, playstyle="Harmonique"):
        """Document when finished"""

        self.tone = 1
        self.stat = Stat(name="Total")
        self.answer = None
        self.answered = False
        self.playstyle = playstyle
        self.restrict_list = restrict_list
        self.playlist={}

        tkinter.Frame.__init__(self, master)

        for x in range(10):
            tkinter.Grid.columnconfigure(master, x, weight=1)
        for y in range(10):
            tkinter.Grid.rowconfigure(master, y, weight=1)
        self.grid(row=5, column=5)
        self.interval_commencer()

    def interval_commencer(self):
        """Document when finished"""

        self.master.title("CASULANA (v.1.02.m)")
        self.master.geometry("550x140")
        self.master.configure(bg="black")

        def highlight_correct(self, result=None):
            """Document when finished"""
            if self.answered is False:
                self.playlist[self.answer].stat.count()
                self.playlist[self.answer].configure(highlightbackground = "green")
                self.answered = True
            if result is False:
                self.playlist[self.answer].stat.wrong()
                self.stat.wrong()
            text_input.set("Question #"+str(self.stat.counter)+65*" "+"Taux de réussite: "+str(self.stat.win_rate()))

        def play_slot():
            """Document when finished"""
            if self.answered is False:
                fonctions.play(file="/Recordings/Intervalles/harmonic/"+(self.answer.replace(" ", "_")).lower()+"/", number = self.tone)

        def new_slot():
            """Document when finished"""
            if self.answered is True:
                text_input.set("Question #"+str(self.stat.counter+1)+65*" "+"Taux de réussite: "+str(self.stat.win_rate()))
                self.answer = random.choice(list(self.playlist.keys()))
                self.tone = random.randrange(1, 12, 1)

                for key in self.playlist:
                    self.playlist[key].configure(highlightbackground="blue")
                self.answered = False
                self.stat.count()
                fonctions.play(file="/Recordings/Intervalles/harmonic/"+(self.answer.replace(" ", "_")).lower()+"/", number=self.tone)

        def stats_slot():
            """Document when finished"""
            results="Taux de Réussite \n \n"
            for key in self.playlist:
                results += self.playlist[key].retrieve()
                results += "\n"

            messagebox.showinfo(title="Statistiques", message=results)

        def end_slot():
            """Document when finished"""
            self.master.destroy()
            root = IntervalsMenuInterface.tkinter.Tk()
            app = IntervalsMenuInterface.IntervalMenuInterface(master=root)
            app.mainloop()


        def seconde_mineur_slot():
            """Document when finished"""
            res = seconde_mineur.play(tone = self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def seconde_majeur_slot():
            """Document when finished"""
            res = seconde_majeur.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def tierce_mineur_slot():
            """Document when finished"""
            res = tierce_mineur.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def tierce_majeur_slot():
            """Document when finished"""
            res = tierce_majeur.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def quarte_juste_slot():
            """Document when finished"""
            res = quarte_juste.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def triton_slot():
            """Document when finished"""
            res = triton.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def quinte_juste_slot():
            """Document when finished"""
            res = quinte_juste.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def sixte_mineur_slot():
            """Document when finished"""
            res = sixte_mineur.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def sixte_majeur_slot():
            """Document when finished"""
            res = sixte_majeur.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def septieme_mineur_slot():
            """Document when finished"""
            res = septieme_mineur.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def septieme_majeur_slot():

            """Document when finished"""
            res = septieme_majeur.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def octave_slot():
            """Document when finished"""
            res = octave.play(tone=self.tone, answer=self.answer, answered=self.answered)
            highlight_correct(self, result=res)

        def temporary():
            pass

        seconde_mineur = AnswerBox(slot=seconde_mineur_slot, name="Seconde mineur", master=self)
        seconde_majeur = AnswerBox(slot=seconde_majeur_slot, name="Seconde majeur", master=self)
        tierce_mineur = AnswerBox(slot=tierce_mineur_slot, name="Tierce mineur", master=self)
        tierce_majeur = AnswerBox(slot=tierce_majeur_slot, name="Tierce majeur", master=self)
        quarte_juste = AnswerBox(slot=quarte_juste_slot, name="Quarte juste", master=self)
        triton = AnswerBox(slot=triton_slot, name="Triton", master=self)
        quinte_juste = AnswerBox(slot=quinte_juste_slot, name="Quinte juste", master=self)
        sixte_mineur = AnswerBox(slot=sixte_mineur_slot, name="Sixte mineur", master=self)
        sixte_majeur = AnswerBox(slot=sixte_majeur_slot, name="Sixte majeur", master=self)
        septieme_mineur = AnswerBox(slot=septieme_mineur_slot, name="Septieme mineur", master=self)
        septieme_majeur = AnswerBox(slot=septieme_majeur_slot, name="Septieme majeur", master=self)
        octave = AnswerBox(slot=octave_slot, name="Octave", master=self)

        play = tkinter.Button(self, text="Réécouter", command=play_slot, highlightbackground="lightblue")
        new = tkinter.Button(self, text="Nouvelle Question", command=new_slot, highlightbackground="lightblue")
        stats = tkinter.Button(self, text="Statisques", command=stats_slot, highlightbackground="lightblue")
        end = tkinter.Button(self, text="Fin de seance", command=end_slot, highlightbackground="lightblue")

        text_input = StringVar()
        text_input.set("Appuyer sur 'Nouvelle Question' pour commencer")
        text_label = tkinter.Label(self, textvariable=text_input, foreground='purple', background="pink")

        seconde_mineur.grid(row=4, column=1, sticky="wens")
        seconde_majeur.grid(row=4, column=2, sticky="wens")
        tierce_mineur.grid(row=4, column=3, sticky="wens")
        tierce_majeur.grid(row=4, column=4, sticky="wens")
        quarte_juste.grid(row=5, column=1, sticky="wens")
        triton.grid(row=5, column=2, sticky="wens")
        quinte_juste.grid(row=5, column=3, sticky="wens")
        sixte_mineur.grid(row=5, column=4, sticky="wens")
        sixte_majeur.grid(row=6, column=1, sticky="wens")
        septieme_mineur.grid(row=6, column=2, sticky="wens")
        septieme_majeur.grid(row=6, column=3, sticky="wens")
        octave.grid(row=6, column=4, sticky="wens")

        play.grid(row=1, column=2, sticky="wens")
        new.grid(row=1, column=1, sticky="wens")
        stats.grid(row=1, column=3, sticky="wens")
        end.grid(row=1, column=4, sticky="wens")

        text_label.grid(row=2, column=1, columnspan=4,sticky="wens")

        self.playlist = {"Seconde mineur": seconde_mineur, "Seconde majeur":seconde_majeur, "Tierce mineur":tierce_mineur,
                         "Tierce majeur" : tierce_majeur, "Quarte juste":quarte_juste, "Triton":triton, "Quinte juste":quinte_juste,
                         "Sixte mineur" : sixte_mineur, "Sixte majeur":sixte_majeur, "Septieme mineur":septieme_mineur,
                         "Septieme majeur":septieme_majeur,"Octave": octave}
        for restriction in self.restrict_list:
            fonctions.make_idle(self.playlist[restriction])
            self.playlist[restriction].configure(command=temporary)
            del self.playlist[restriction]

        self.answered = True
        self.tone = random.randrange(1,13)
        self.answer = random.choice(list(self.playlist.keys()))
#__________________________________________________________________