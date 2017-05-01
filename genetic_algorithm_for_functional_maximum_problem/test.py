from Population import Population
import matplotlib.pyplot as plt

colormap = plt.cm.Paired
def test(population_size, chromosome_len, pc, pm):
    fits = []
    for j in range(50):
        population = Population(population_size, chromosome_len, pc, pm)
        for i in range(100):
            population.next_generation()
        fits.append(population.get_max_fitness())
    print(fits)
    # plt.figure(0)
    plt.plot(range(len(fits)),fits,'-x',label = '(' + str(population_size) + ', ' + str(chromosome_len) + ', ' + str(pc) + ', ' + str(pm) + ')')


def main():
    plt.rcParams['font.sans-serif']=['SimHei']
    
    plt.figure(0)
    for i in range(0,5):
        test(100, 24, 0.8, i / 100)
        print(i)

    plt.figure(0)
    plt.xlabel('次')
    plt.ylabel('max_fitness')
    plt.title('改变交叉率(0-1.0),次数-最大值') # 添加图形标题
    plt.grid()
    plt.legend()
    plt.show()

main()