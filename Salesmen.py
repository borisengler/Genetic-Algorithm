import random
from Cities import *
import Globals


class Population:
    def __init__(self, cities):
        self.pop = []
        self.mating_pool = []
        self.cities = cities
        self.new_pop = []
        self.best = Salesman()
        self.best.steps = []

    def pass_best(self):
        index = random.randint(5, Globals.number_of_salesmen-5)
        self.pop[index] = self.best


    def calculate_distances(self):
        for salesman in self.pop:
            for i in range(0, len(salesman.steps) - 1):
                indexA = salesman.steps[i]
                cityA = self.cities[indexA]
                indexB = salesman.steps[i+1]
                cityB = self.cities[indexB]
                salesman.distance += cityA.calculate_distance(cityB)

    def calculate_fitness(self):
        min_distance = min([salesman.distance for salesman in self.pop])

        for salesman in self.pop:
            if salesman.distance == 0:
                print(salesman.steps, len(salesman.steps))
            salesman.fitness = (min_distance / salesman.distance) ** Globals.power_of_fitness
            salesman.fitness = int(salesman.fitness*100)

    def create_mating_pool(self):
        self.mating_pool = []
        for salesman in self.pop:
            for i in range(salesman.fitness):
                self.mating_pool.append(salesman)


    def mate(self):
        best_before = Salesman()
        best_before.steps = (self.best.steps).copy()
        self.new_pop.append(best_before)
        for i in range(len(self.pop)-1):
            self.new_pop.append(Salesman())
            parentA = random.choice(self.mating_pool)
            parentB = random.choice(self.mating_pool)
            self.new_pop[i].steps = parentA.crossover(parentB)
        self.pop = self.new_pop.copy()
        self.new_pop = []


    def mutate(self):
        for salesman in self.pop:
            salesman.mutate()

    def find_best(self):
        best = sorted(self.pop, key = lambda x: x.distance)[0]
        self.best = best
        return best





class Salesman:

    def __init__(self):
        self.steps = []
        self.cities = Globals.number_of_cities
        self.distance = 0
        self.fitness = 0
        if self.steps == []:
            self.steps = [i for i in range(1, self.cities)]

            random.shuffle(self.steps)
            self.steps.append(0)
            self.steps[0], self.steps[-1] = self.steps[-1], self.steps[0]
            self.steps.append(0)

    def crossover(self, partner):
        new_steps = [0]

        self.remaining = [x for x in range(1, Globals.number_of_cities)]
        rand_start = random.choice([self.steps[1], partner.steps[1]])
        new_steps.append(rand_start)
        if rand_start == 0: print(self.steps, '\n', partner.steps)
        self.remaining.remove(rand_start)
        for i in range(1, len(self.steps)-2):

            rand = random.random()
            if rand > 0.5:
                index = i+1
                if self.steps[index] in self.remaining:
                    new_steps.append(self.steps[index])
                    self.remaining.remove(self.steps[index])
                else:
                    new_steps.append(random.choice(self.remaining))
                    self.remaining.remove(new_steps[-1])
            else:
                index = partner.steps.index(self.steps[i+1])
                if partner.steps[index] in self.remaining:
                    new_steps.append(partner.steps[index])
                    self.remaining.remove(partner.steps[index])
                else:
                    new_steps.append(random.choice(self.remaining))
                    self.remaining.remove(new_steps[-1])

        new_steps.append(0)
        return new_steps

    def mutate(self):
        for i in range(1, len(self.steps)-1):
            rand = random.random()
            if rand <= Globals.mutation_rate:
                index = random.randint(1, self.cities-1)
                self.steps[i], self.steps[index] = self.steps[index], self.steps[i]

    def copy(self, goal):
        goal.steps = self.steps
        return

