import math
import random

print(int('000000000000000000000001',2))

def convert_to_decimal(binary_figure):
    '''把二进制数转化为【0,9】的数'''
    decimal_figure = int(binary_figure,2)*9/math.pow(2, len(binary_figure))
    return decimal_figure


def calc_fitness(val):

def crossover(chromosome1, chromosome2):

def mutation(chromosome1, chromosome2):

def genetic_fun(population_size, string_len, pc, pm):
    '''
    遗传函数
    population_size：种群规模
    string_len: 染色体长度
    pc: 交叉概率
    pm: 变异概率
    '''
    population = []

    for i in range(population_size):
        classmethod = ''
        for j in range(0, string_len):
            chromosome = chromosome + random.choice('01')
        population.append(chromosome)
    
    fitness_sum = sum(chromosomes_fitness)

    count = 0
    while count < :
        chromosomes_fitness = []

        for chromosome in population:
            chromosomes_fitness.append(calc_fitness(chromosome))

        fitness_sum = sum(chromosomes_fitness)

        population_new = []
        while len(population_new) < population_size:
            random1 = random.randint(0, fitness_sum - 1)
            random2 = random.randint(0, fitness_sum - 1)

            chromosome1 = 0
            chromosome2 = 0

            tmp = 0
            for i in range(len(population)):
                if random1 >= tmp && random1 < tmp + chromosomes_fitness[i]:
                    chromosome1 = population[i]
                if random2 >= tmp && random2 < tmp + chromosomes_fitness[i]:
                    chromosome2 = population[i]
                tmp += chromosomes_fitness[i]
            pass

            population_new.append(crossover(chromosome1, chromosome2))
            population_new.append(mutation(chromosome1, chromosome2))
        pass

        population = population_new
        count += 1
    pass
        
        
