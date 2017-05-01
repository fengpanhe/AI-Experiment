import math
import random
class Individual(object):

    def __init__(self, chromosome, pm):
        self.chromosome = chromosome
        self.pm = pm
        self.mutation()

        self.fitness = 0
        self.calc_fitness()
        self.score = self.fitness
    
    def mutation(self):
        if random.random() < self.pm:
            times = random.randint(0, 10)
            for i in range(times):
                index = random.randint(0, len(self.chromosome) - 1)
                new_chromosome = self.chromosome[0:index]
                if self.chromosome[index] == '1':
                    new_chromosome += '0'
                else:
                    new_chromosome += '1'
                self.chromosome = new_chromosome + self.chromosome[index+1:]

    def convert_to_decimal(self, binary_figure):
        '''把二进制数转化为[0,9]的数'''
        decimal_figure = int(binary_figure, 2) * 9 / math.pow(2, len(binary_figure))
        return decimal_figure
    
    def calc_fitness(self):
        x = self.convert_to_decimal(self.chromosome)
        y = x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
        self.fitness = y