from random import randint

class Die:
    """Una classe che rappresenta un dado singolo"""

    def __init__(self, num_sides=6):
        """Default di 6 lati"""
        self.num_sides = num_sides

    def roll(self):
        """Restituisce un valore casuale da 1 e il numero dei lati"""
        return randint(1, self.num_sides)
    
    