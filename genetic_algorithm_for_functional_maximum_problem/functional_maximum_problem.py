import math
import random

print(int('000000000000000000000001',2))

class genetic_algorithm(object):

    def __init__(self, population_size, string_len, pc, pm):
        '''
        遗传函数
        population_size：种群规模
        string_len: 染色体长度
        pc: 交叉概率
        pm: 变异概率
        '''
        self.population_size = population_size
        self.chromosome_len = string_len
        self.pc = pc
        self.pm = pm

    def convert_to_decimal(binary_figure):
        '''把二进制数转化为【0,9】的数'''
        decimal_figure = int(binary_figure,2)*9/math.pow(2, len(binary_figure))
        return decimal_figure


    def calc_fitness(self, val):
        x = convert_to_decimal(val)
        y = x + 10 * math.sin(5 * x) + 7 * math.cosh(4 * x)
        return y

    def crossover(self, chromosome1, chromosome2):
        if random.random() < self.pc:
            start = random.randint(0,self.chromosome_len - 1)
            end = random.randint(start, self.chromosome_len)
            tmp_str1 = chromosome1[start:end]
            tmp_str2 = chromosome2[start:end]
            for i in range(end - start):
                chromosome1[start + i] = tmp_str2[i]
                chromosome2[start + i] = tmp_str1[i]
            
        return [chromosome1,chromosome2]


    def mutation(self,chromosome):
        if random.random() < self.pm:
            times = random.randint(10)
            for i in range(times):
                index = random.randint(self.chromosome_len)
                if chromosome[index] == '1':
                    chromosome[index] = '0'
                else:
                    chromosome[index] = '0'
        return chromosome



    def genetic_fun(self,population_size, string_len, pc, pm):
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
        while count < 40:
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
                population_new.append(mutation(chromosome1))
                population_new.append(mutation(chromosome2))
            pass

            population = population_new
            count += 1
        pass


