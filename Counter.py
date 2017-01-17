__author__ = 'Somma'


class Stat():
    """Document when finished"""
    def __init__(self, name=""):
        """Document when finished"""
        self.name = name
        self.counter = 0
        self.wrong_counter = 0

    def __str__(self):
        """Document when finished"""
        result = self.name+" : "+self.win_rate()
        return result

    def win_rate(self):
        """Document when finished"""
        if self.counter == 0:
            result = "n/d"
        else:
            result = str(int((self.counter-self.wrong_counter)*100/self.counter))+"%"
        return result

    def count(self):
        """Document when finished"""
        self.counter += 1

    def wrong(self):
        """Document when finished"""
        self.wrong_counter += 1

    def reset(self):
        """Document when finished"""
        self.counter = 0
        self.wrong_counter = 0