
import random
POPULATION_SIZE = 10
POINTS_SIZE = 5
population = [] 
for i in range(POPULATION_SIZE):
    # 個体(経路)
    individual = list(range(POINTS_SIZE))
    random.shuffle(individual)
    population.append(individual)
print(population)
print('--------')

points = [] # 都市のリスト
for i in range(POINTS_SIZE):
    points.append((random.random(), random.random()))

rout=[]


for ind in range(POPULATION_SIZE):
    #canvas = canvas_list[ind]
    route = population[ind] # 経路
    rout.append(route)
    print(rout)
print(rout)
print('--------')
print(points)
print('--------')
print(points[route[0]])

for i in range(POINTS_SIZE):
    (x0, y0) = points[route[i]]

for ind in range(POPULATION_SIZE):
    #canvas = canvas_list[ind]
    route = population[ind] 
    