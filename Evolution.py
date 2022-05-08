import random
from Cities import *
from Salesmen import *
import Globals
import tkinter as tk
import time



def create_map(cities, canvas, generation, best, worst):
    canvas.create_rectangle(0, 0, Globals.width, Globals.height, fill = 'white')
    canvas.create_text(Globals.width /2, Globals.height-30, fill="darkblue", font="Times 20 italic bold",
                       text="Generation " + str(generation))
    canvas.create_text(90, 30, fill="green", font="Times 10 italic bold",
                       text="Best distance: " + str(int(best)))
    canvas.create_text(Globals.width - 90, 30, fill="red", font="Times 10 italic bold",
                       text="Worst distance: " + str(int(worst)))
    for i in range(len(cities)):
        if i == 0:
            canvas.create_oval(cities[i].x-5, cities[i].y-5, cities[i].x+5, cities[i].y+5, fill = 'green')
        else:
            canvas.create_oval(cities[i].x-5, cities[i].y-5, cities[i].x+5, cities[i].y+5, fill = 'red')



network = NetworkOfCities()
network.cities = [City(i) for i in range(Globals.number_of_cities)]
population = Population(network.cities)
population.pop = [Salesman() for i in range(Globals.number_of_salesmen)]
population.calculate_distances()

best_to_worst = sorted(population.pop, key = lambda x: x.distance)
print('min: ', best_to_worst[0].distance,
'max: ',best_to_worst[-1].distance)
population.calculate_fitness()

population.create_mating_pool()
best_of_generations_steps = []
worst_of_generations_steps = []
best_distances = []
worst_distances = []

best_of_generations_steps.append(best_to_worst[0].steps)
worst_of_generations_steps.append(best_to_worst[-1].steps)
best_distances.append(best_to_worst[0].distance)
worst_distances.append(best_to_worst[-1].distance)


for i in range(Globals.number_of_generations):
    if i%5 == 0:
        print('Generation: ' + str(i))
    #print('distance: ', min([x.distance for x in population.pop]))
    #print(population.find_best().steps)
    population.mate()
    population.mutate()
    population.calculate_distances()
    population.calculate_fitness()
    population.create_mating_pool()

    best_to_worst = sorted(population.pop, key=lambda x: x.distance)
    print(best_to_worst[0].distance)
    best_distances.append(best_to_worst[0].distance)
    worst_distances.append(best_to_worst[-1].distance)
    best_of_generations_steps.append(best_to_worst[0].steps)
    worst_of_generations_steps.append(best_to_worst[-1].steps)


print('min: ', sorted(population.pop, key = lambda x: x.distance)[0].distance,
'max: ',sorted(population.pop, key = lambda x: x.distance)[-1].distance)
time.sleep(1)
root = tk.Tk()
c = tk.Canvas(root, width = Globals.width, height = Globals.height)

c.pack()
c.update()
a = input()
time.sleep(0.5)


create_map(network.cities, c, 0, best_distances[0], worst_distances[0])
for j in range(len(best_of_generations_steps[0])-1):
    index = best_of_generations_steps[0][j]
    index2 = best_of_generations_steps[0][j+1]
    x1 = network.cities[index % Globals.number_of_cities].x
    y1 = network.cities[index % Globals.number_of_cities].y
    x2 = network.cities[index2 % Globals.number_of_cities].x
    y2 = network.cities[index2 % Globals.number_of_cities].y
    c.create_line(x1, y1, x2, y2, fill = 'green', width = 2)





for i in range(Globals.number_of_generations+1):
    if i%5 == 0:
        create_map(network.cities, c, i, best_distances[i], worst_distances[i])
        c.update()
        c.pack()
        for j in range(len(best_of_generations_steps[i])-1):
            index = best_of_generations_steps[i][j]
            index2 = best_of_generations_steps[i][j+1]
            x1 = network.cities[index % Globals.number_of_cities].x
            y1 = network.cities[index % Globals.number_of_cities].y
            x2 = network.cities[index2 % Globals.number_of_cities].x
            y2 = network.cities[index2 % Globals.number_of_cities].y
            c.create_line(x1, y1, x2, y2, fill = 'green', width = 2)

        c.update()
        if Globals.worst:
            time.sleep(0.5)
            create_map(network.cities, c, i, best_distances[i], worst_distances[i])
            for j in range(len(best_of_generations_steps[i]) - 1):
                index = worst_of_generations_steps[i][j]
                index2 = worst_of_generations_steps[i][j + 1]
                x1 = network.cities[index % Globals.number_of_cities].x
                y1 = network.cities[index % Globals.number_of_cities].y
                x2 = network.cities[index2 % Globals.number_of_cities].x
                y2 = network.cities[index2 % Globals.number_of_cities].y
                c.create_line(x1, y1, x2, y2, fill='red', width=2)
            c.update()

        time.sleep(0.5)
    c.update()
    c.pack()
a = input()

c.pack()
