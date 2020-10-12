import random
import math
pc = 0.69
pm = 0.11
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
		#f =  1/(((math.cos(x[0])*math.sin(x[1]))-(x[0]/(pow(x[1],2)+1)))+0.1)
		f = -((math.cos(x[0])*math.sin(x[1]))-(x[0]/(pow(x[1],2)+1)))
		fitness.append(f)
	return fitness

def sumFitness(fitness): #total fitness function seluruh individual
	return sum(fitness)

def bestFitness(fitness): # mencari individu dengan nilai fitness terbaik di sebuah populasi
	return fitness[fitness.index(max(fitness))]

def rouletteWheel(fitness): # parent selection menggunakan Roulette Wheels
	r = random.random()
	ind = 0
	while (r > 0):
		r -= fitness[ind]/sumFitness(fitness)
		ind += 1
	return ind

def crossover(papa, mama, pc): #melakukan crossover terhadap kedua parent yang didapatkan (jika masuk dalam probabilitas)
	x = random.random()
	if (x < pc):
		stop = random.randint(0,9)
		for i in range(stop):
			papa[i] = mama[i]
			mama[i] = papa[i]
	return papa,mama

def mutasi(papa, mama, pm): #melakukan mutasi terhadap kedua parent yang didapatkan (jika masuk dalam probabilitas)
	x = random.random()
	if (x<pm):
		papa[random.randint(0,9)] = random.randint(0,9)
		mama[random.randint(0,9)] = random.randint(0,9)
	return papa,mama




pop = generatePopulation()
print("Populasi",pop)
enc = encoding(pop)
print("Phenotype",enc)
fit = fitness(enc)
print("Fitnessnya",fit)
bestFit = bestFitness(fit)
print("Best Fitness ",bestFit)
sumFit = sumFitness(fit)
print("ini sumfit ",sumFit)