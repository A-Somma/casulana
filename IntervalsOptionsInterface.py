__author__ = 'Somma'
import tkinter
import IntervalsMenuInterface
from tkinter import StringVar, messagebox





class IntervalsOptionsInterface(tkinter.Frame):

            def __init__(self, master=None):


                self.checked = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                                StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
                for var in self.checked:
                    var.set("True")

                tkinter.Frame.__init__(self, master)
                for x in range(10):
                    tkinter.Grid.columnconfigure(master, x, weight=1)
                for y in range(10):
                   tkinter.Grid.rowconfigure(master, y, weight=1)
                self.grid(row=1, column=1)
                self.options()



            def options(self):

                self.master.title("CASULANA (v.1.02.m)")
                self.master.geometry("640x140")
                self.master.configure(bg="black")

                def confirmation_slot():

                    restrict_list = []

                    for checkbox in self.checked:
                        if checkbox.get() != "True":
                            restrict_list.append(checkbox.get())

                    if len(restrict_list) == 12:
                        messagebox.showinfo(title="Avertissement", message="Votre liste de lecture est vide!")
                    else:
                        messagebox.showinfo(title="Avertissement", message="Vos préférences ont été sauvegardées!")
                        self.master.destroy()
                        root = IntervalsMenuInterface.tkinter.Tk()
                        app = IntervalsMenuInterface.IntervalMenuInterface(master=root, restrict_list=restrict_list,
                                                                           playstyle=style.get())
                        app.mainloop()







                confirmation = tkinter.Button(self, text="Confirmer Sélection", command=confirmation_slot, highlightbackground="green")


                style = StringVar()
                style.set("Mélodique")

                options = tkinter.OptionMenu(self, style, "Mélodique", "Harmonique")
                options.configure(bg="lightblue", width="11")

                list_title = tkinter.Label(self, text="Playlist:"+110*" ", fg="white", bg="black")
                style_title = tkinter.Label(self, text="Playstyle:"+10*" ", fg="white", bg="black")
                seperator = tkinter.Label(self, text=" | \n | \n | \n | \n | ", bg="lightblue")
                filler_1 = tkinter.Label(self, text="", bg="lightblue")
                filler_2 = tkinter.Label(self, text="", bg="black")
                filler_3 = tkinter.Label(self, text="", bg="black")



                seconde_mineur = tkinter.Checkbutton(self, text="Seconde mineur", offvalue="Seconde mineur", onvalue="True", bg="lightblue", var=self.checked[0])
                seconde_majeur = tkinter.Checkbutton(self, text="Seconde majeur", offvalue="Seconde majeur", onvalue="True", bg="lightblue", var=self.checked[1])
                tierce_mineur = tkinter.Checkbutton(self, text="Tierce mineur", offvalue="Tierce mineur", onvalue="True", bg="lightblue", var=self.checked[2])
                tierce_majeur = tkinter.Checkbutton(self, text="Tierce majeur", offvalue="Tierce majeur", onvalue="True", bg="lightblue", var=self.checked[3])
                quarte_juste = tkinter.Checkbutton(self,  text="Quarte juste", offvalue="Quarte juste", onvalue="True", bg="lightblue", var=self.checked[4])
                triton = tkinter.Checkbutton(self, text="Triton", bg="lightblue", offvalue="Triton", onvalue="True", var=self.checked[5])
                quinte_juste = tkinter.Checkbutton(self, text="Quinte juste", offvalue="Quinte juste", onvalue="True", bg="lightblue", var=self.checked[6])
                sixe_mineur = tkinter.Checkbutton(self, text="Sixte mineur", offvalue="Sixte mineur", onvalue="True", bg="lightblue", var=self.checked[7])
                sixte_majeur = tkinter.Checkbutton(self, text="Sixte majeur", offvalue="Sixte majeur", onvalue="True", bg="lightblue", var=self.checked[8])
                septieme_mineur = tkinter.Checkbutton(self, text="Septieme mineur", offvalue="Septieme mineur", onvalue="True", bg="lightblue", var=self.checked[9])
                septieme_majeur = tkinter.Checkbutton(self, text="Septieme majeur", offvalue="Septieme majeur", onvalue="True", bg="lightblue", var=self.checked[10])
                octave = tkinter.Checkbutton(self, text="Octave", offvalue="Octave", onvalue="True", bg="lightblue", var=self.checked[11])


                list_title.grid(row=0, column=1, columnspan=4, sticky="wens")
                style_title.grid(row=0, column=5, columnspan=4, sticky="wens")
                seconde_mineur.grid(row=1, rowspan=1, column=1, sticky="wens")
                seconde_majeur.grid(row=2, rowspan=1, column=1, sticky="wens")
                tierce_mineur.grid(row=3, rowspan=1, column=1, sticky="wens")
                tierce_majeur.grid(row=1, rowspan=1, column=2, sticky="wens")
                quarte_juste.grid(row=2, rowspan=1, column=2, sticky="wens")
                triton.grid(row=3, rowspan=1, column=2, sticky="wens")
                quinte_juste.grid(row=1, rowspan=1, column=3, sticky="wens")
                sixe_mineur.grid(row=2, rowspan=1, column=3, sticky="wens")
                sixte_majeur.grid(row=3, rowspan=1, column=3, sticky="wens")
                septieme_mineur.grid(row=1, rowspan=1, column=4, sticky="wens")
                septieme_majeur.grid(row=2, rowspan=1, column=4, sticky="wens")
                octave.grid(row=3, rowspan=1, column=4, sticky="wens")
                seperator.grid(row=1, rowspan=3, column=5, sticky="wens")
                filler_1.grid(row=2, rowspan=2, column=6, sticky="wens")
                options.grid(row=1, column=6, sticky="wens")
                confirmation.grid(row=5, column=3, sticky ="wens")
                filler_2.grid(row=5, column=1, columnspan=2, sticky="wens")
                filler_3.grid(row=5, column=4, columnspan=3, sticky="wens")