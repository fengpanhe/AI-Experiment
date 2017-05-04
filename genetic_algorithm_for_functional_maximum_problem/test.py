from Population import Population
import matplotlib.pyplot as plt

colormap = plt.cm.Paired
def test(population_size, chromosome_len, pc, pm):
    fits = []
    # for j in range(50):
    population = Population(population_size, chromosome_len, pc, pm)
    for i in range(100):
        population.next_generation()
        fits.append(population.get_max_fitness())
    print(fits)
    # plt.figure(0)
    plt.plot(range(len(fits)),fits,'-x',label = '(' + str(population_size) + ', ' + str(chromosome_len) + ', ' + str(pc) + ', ' + str(pm) + ')')
    plt.annotate(r'f=' + str(fits[-1]),
         xy=(99, fits[-1]), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


def main():
    plt.rcParams['font.sans-serif']=['SimHei']
    
    plt.figure(0)
    test(200, 24, 0.8, 0.01)
    # for i in range(0,5):
    #     test(100, 24, 0.8, i / 100)
    #     print(i)

    plt.figure(0)
    plt.xlabel('次')
    plt.ylabel('max_fitness')
    plt.title('次数-最大值') # 添加图形标题
    plt.grid()
    plt.legend()
    plt.show()

main()