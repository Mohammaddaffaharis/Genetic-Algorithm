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

def fitness(phenotype): #fitness function dari setiap individual di dalam populasi
	fitness = []
	for x in phenotype:
		f =  1/(((math.cos(x[0])*math.sin(x[1]))-(x[0]/(pow(x[1],2)+1)))+0.1)
		fitness.append(f)
	return fitness

def sumFitness(fitness): #total fitness function seluruh individual
	total = 0
	for i in fitness:
		total = total + i
	return total

def bestFitness(fitness): # mencari individu dengan nilai fitness terbaik di sebuah populasi (digunakan untuk elitism)
	return fitness.index(max(fitness))

def rouletteWheel(fitness): # parent selection menggunakan Roulette Wheels
	r = random.random()
	total = sumFitness(fitness)
	ind = 0
	while (r > 0) and (ind <= 18):
		r = r - fitness[ind]/total
		ind = ind + 1
	return ind

def crossover(papa, mama, pc): #melakukan crossover terhadap kedua parent yang didapatkan (jika masuk dalam probabilitas)
	x = random.random()
	if (x < pc):
		stop = random.randint(0,9)
		for i in range(stop):
			papa[i],mama[i] = mama[i], papa[i]
			#mama[i] = papa[i]
	return papa,mama

def mutasi(papa, mama, pm): #melakukan mutasi terhadap kedua parent yang didapatkan (jika masuk dalam probabilitas)
	x = random.random()
	if (x<pm):
		papa[random.randint(0,9)] = random.randint(0,9)
		mama[random.randint(0,9)] = random.randint(0,9)
	return papa,mama


#============ M A I N   P R O G R A M ============

pop = generatePopulation() #generate populasi awal
for i in range(100): #generate 100 generasi
	enc = encoding(pop)
	fit = fitness(enc)
	newPop = []
	bestFit = pop[bestFitness(fit)]
	newPop.append(bestFit)
	newPop.append(bestFit)
	i = 0
	while(i < 18):
		q = rouletteWheel(fit)
		r = rouletteWheel(fit)
		papa = pop[q]
		mama = pop[r]
		bocil = crossover(papa,mama,pc)
		bocil = mutasi(bocil[0],bocil[1],pm)
		newPop.append(bocil[0])
		newPop.append(bocil[1])
		i += 2
	pop = newPop

enc = encoding(pop)
fit = fitness(enc)
hasil = pop[bestFitness(fit)]
arrHasil = []
arrHasil.append(hasil)

print('========== Nilai Minimalisasi ==========\n')
print('Kromosom terbaik :', hasil)
print('Hasil decode     :', encoding(arrHasil))
print('Fitness terbaik  :', fitness(arrHasil))





