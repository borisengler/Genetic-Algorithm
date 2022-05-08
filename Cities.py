import random
from math import sqrt
import Globals

class NetworkOfCities:

    def __init__(self):
        self.cities = []

class City:

    def __init__(self, ID):
        self.ID = ID
        self.x = random.randint(50, 450)
        self.y = random.randint(50, 450)

    def calculate_distance(self, neighbor):
        return abs(sqrt((self.x - neighbor.x)**2 + (self.y - neighbor.y)**2))
