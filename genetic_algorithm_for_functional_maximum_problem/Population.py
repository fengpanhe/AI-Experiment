from Individual import Individual

import random


def compare(individual):
    return individual.fitness

class Population(object):

    def __init__(self, population_size, chromosome_len, pc, pm):
        '''
        遗传函数
        population_size：种群规模
        chromosome_len: 染色体长度
        pc: 交叉概率
        pm: 变异概率
        '''
        self.population_size = population_size
        self.chromosome_len = chromosome_len
        self.pc = pc
        self.pm = pm
        self.generation_count = 0
        self.population = []

        for i in range(self.population_size):
            chromosome = ''
            for j in range(self.chromosome_len):
                chromosome = chromosome + random.choice('01')
            self.population.append(Individual(chromosome,self.pm))
    
    
    def crossover(self, chromosome1, chromosome2):
        if random.random() < self.pc:
            start = random.randint(0,self.chromosome_len - 1)
            end = random.randint(start, self.chromosome_len)
            tmp_str1 = chromosome1[start:end]
            tmp_str2 = chromosome2[start:end]
            chromosome1 = chromosome1[0:start] + tmp_str2 + chromosome1[end:]
            chromosome2 = chromosome2[0:start] + tmp_str1 + chromosome2[end:]
        return [chromosome1,chromosome2]

    


    def next_generation(self):
        self.population.sort(key = compare)

        population_new = []


        for individual in self.population[int(self.population_size * 9 / 10):]:
            population_new.append(individual)

        min_fitness = self.population[0].fitness
        score_sum = 0
        for individual in self.population:
            individual.score = individual.fitness - min_fitness
            score_sum += individual.score

        while len(population_new) < self.population_size:
            random1 = random.uniform(0, score_sum)
            random2 = random.uniform(0, score_sum)
            chromosome1 = self.population[self.population_size - 1].chromosome
            chromosome2 = self.population[self.population_size - 1].chromosome
            tmp = 0
            for individual in self.population:
                if random1 > tmp and random1 <= tmp + individual.score:
                    chromosome1 = individual.chromosome
                if random2 > tmp and random2 <= tmp + individual.score:
                    chromosome2 = individual.chromosome
                tmp += individual.score
            pass
            crossover_chromosome = self.crossover(chromosome1, chromosome2)
            chromosome1 = crossover_chromosome[0]
            chromosome2 = crossover_chromosome[1]
            population_new.append(Individual(chromosome1, self.pm))
            population_new.append(Individual(chromosome2, self.pm))
        pass
        self.population = population_new



        self.generation_count += 1
    
    def get_max_fitness(self):
        max_fitness = self.population[0].fitness
        for individual in self.population:
            if individual.fitness > max_fitness:
                max_fitness = individual.fitness
        
        return max_fitness