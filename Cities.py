import random
from math import sqrt
import Globals

class NetworkOfCities:

    def __init__(self):
        self.cities = []

    def change_cities(self):
        for i in range(len(self.cities)):
            self.cities[i].y = 50+i*(400/Globals.number_of_cities)
            self.cities[i].x = random.randint(230, 270)


class City:

    def __init__(self, ID):
        self.ID = ID
        self.x = random.randint(50, 450)
        self.y = random.randint(50, 450)

    def calculate_distance(self, neighbor):
        return abs(sqrt((self.x - neighbor.x)**2 + (self.y - neighbor.y)**2))
