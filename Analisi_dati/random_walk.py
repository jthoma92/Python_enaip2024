from random import choice

class RandomWalk:
    """Una classe per generare le passeggiate aleatorie"""

    def __init__(self, num_points = 5000):
        """"inizializzare attributi della passeggiata"""
        self.num_points = num_points

        #cominciamo sempre a (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calcolare tutti i punti della passeggiata"""
        # Continuare a fare passi finche non arriva alla lunghezza desiderata
        while len(self.x_values) < self.num_points:

            #decidere in quale direzione andare, e quanta distanza andare
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #respingere movimenti di (0,0)
            if x_step == 0 and y_step == 0:
                continue

            #calcolare nuova posizione
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)