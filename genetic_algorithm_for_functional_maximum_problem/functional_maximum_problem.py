import math
import random

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

    def convert_to_decimal(self, binary_figure):
        # print(binary_figure + '  len:' + str(math.pow(2, len(binary_figure))))
        '''把二进制数转化为[0,9]的数'''
        decimal_figure = int(binary_figure, 2) * 9 / math.pow(2, len(binary_figure))
        return decimal_figure


    def calc_fitness(self, val):
        x = self.convert_to_decimal(val)
        y = x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
        return y + 17

    def crossover(self, chromosome1, chromosome2):
        if random.random() < self.pc:
            start = random.randint(0,self.chromosome_len - 1)
            end = random.randint(start, self.chromosome_len)
            tmp_str1 = chromosome1[start:end]
            tmp_str2 = chromosome2[start:end]
            chromosome1 = chromosome1[0:start] + tmp_str2 + chromosome1[end:]
            chromosome2 = chromosome2[0:start] + tmp_str1 + chromosome2[end:]
        return [chromosome1,chromosome2]


    def mutation(self,chromosome):
        if random.random() < self.pm:
            times = random.randint(0, 10)
            for i in range(times):
                index = random.randint(0, self.chromosome_len - 1)
                new_chromosome = chromosome[0:index]
                if chromosome[index] == '1':
                    new_chromosome += '0'
                else:
                    new_chromosome += '1'
                chromosome = new_chromosome + chromosome[index+1:]
        return chromosome



    def genetic_fun(self):
        '''
        遗传函数
        population_size：种群规模
        string_len: 染色体长度
        pc: 交叉概率
        pm: 变异概率
        '''
        population = []

        for i in range(self.population_size):
            chromosome = ''
            for j in range(self.chromosome_len):
                chromosome = chromosome + random.choice('01')
            population.append(chromosome)


        count = 0
        while count < 400:

            chromosomes_fitness = []
            for chromosome in population:
                chromosomes_fitness.append(self.calc_fitness(str(chromosome)))

            fitness_sum = int(sum(chromosomes_fitness))

            population_new = []
            while len(population_new) < self.population_size:
                random1 = random.randint(0, fitness_sum - 1)
                random2 = random.randint(0, fitness_sum - 1)

                chromosome1 = 0
                chromosome2 = 0

                tmp = 0
                for i in range(len(population)):
                    if random1 >= tmp and random1 < tmp + chromosomes_fitness[i]:
                        chromosome1 = population[i]
                    if random2 >= tmp and random2 < tmp + chromosomes_fitness[i]:
                        chromosome2 = population[i]
                    tmp += chromosomes_fitness[i]
                pass

                crossover_chromosome = self.crossover(chromosome1, chromosome2)
                chromosome1 = crossover_chromosome[0]
                chromosome2 = crossover_chromosome[1]
                population_new.append(self.mutation(chromosome1))
                population_new.append(self.mutation(chromosome2))
            pass

            population = population_new
            count += 1
        pass

        chromosomes_fitness = []
        for chromosome in population:
            chromosomes_fitness.append(self.calc_fitness(chromosome))
        
        return max(chromosomes_fitness) - 17

def main():
    test = genetic_algorithm(500, 24, 0.6, 0.01)
    result = test.genetic_fun()
    print(result)
main()