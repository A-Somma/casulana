__author__ = 'Somma'
import simpleaudio
import os

#____________________________________________________________________________________________________


def play(path=os.getcwd(), file=None, number=1):
    """Document when finished"""
    wave_obj = simpleaudio.WaveObject.from_wave_file(path+file+str(number)+".wav")
    wave_obj.play()

#____________________________________________________________________________________________________


def hide_stuff(*args):
    """Document when finished"""
    for widget in args:
        widget.grid_forget()

#____________________________________________________________________________________________________


def make_idle(*args):
    """Document when finished"""
    for widget in args:
        widget.configure(command=None, highlightbackground="yellow")

#____________________________________________________________________________________________________

def copy_dir():
    """Document when finished"""
    path = "\Recordings\Intervalles\hard\\"
    intervals = ["octave", "quarte_juste", "quinte_juste", "seconde_majeur", "seconde_mineur", "septieme_majeur", "septieme_mineur", "sixte_majeur", "sixte_mineur", "tierce_majeur", "tierce_mineur", "triton"]
    for i in intervals:
        new_path = path+i
        for n in range(1, 13):
            new_file = new_path +"\\"+str(n)+".wav"
            yield(new_path, [new_file])