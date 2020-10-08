import random
import math
def generatePopulation(): # menggunakan integer Encoding
	population = []
	x = 1
	for x in range(20): #populasi sebanyak 20 individual
		individual = []
		for y in range(10): # satu individual terdiri dari 10 gen
			individual.append(random.randint(0,9))
		population.append(individual)
	return population

def encoding(population): #encoding Integer menggunakan 5 gen
	phenotype = []
	for x in population:
		x1 = (-1)+((2-(-1))/(9*(pow(10,-1)+pow(10,-2)+pow(10,-3)+pow(10,-4)+pow(10,-5))))*((x[0]*pow(10,-1))+(x[1]*pow(10,-2))+(x[2]*pow(10,-3))+(x[3]*pow(10,-4))+(x[4]*pow(10,-5)))
		x2 = (-1)+((1-(-1))/(9*(pow(10,-1)+pow(10,-2)+pow(10,-3)+pow(10,-4)+pow(10,-5))))*((x[5]*pow(10,-1))+(x[6]*pow(10,-2))+(x[7]*pow(10,-3))+(x[8]*pow(10,-4))+(x[9]*pow(10,-5)))
		phenotype.append([x1,x2])
	return phenotype

def fitness(phenotype): #fitness function dari setiap individual
	fitness = []
	for x in phenotype:
		f = (math.cos(x[0])*math.sin(x[1]))-(x[0]/(pow(x[1],2)+1))
		fitness.append(f)
	return fitness

def sumFitness(fitness): #total fitness function seluruh individual
	return -(sum(fitness))


pop = generatePopulation()
print(pop)
enc = encoding(pop)
print(enc)
fit = fitness(enc)
print(fit)
sumFit = sumFitness(fit)
print("ini sumfit ",sumFit)