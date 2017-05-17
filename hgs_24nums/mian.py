from IDAstar_24nums import IDAStar
from Astar_dict_24nums import AStar

import time


def main():
    pazzle_list = [[1, 2, 3, 4, 9, 5, 6, 7, 14, 13, 10, 11, 12, 8, 19, 20, 0, 22, 17, 18, 16, 15, 21, 23, 24], [5, 10, 1, 3, 4, 11, 7, 2, 8, 9, 6, 16, 17, 13, 14, 12, 21, 22, 0, 19, 15, 23, 20, 18, 24], [6, 2, 9, 12, 1, 11, 7, 10, 24, 3, 16, 15, 4, 14, 8, 21, 20, 13, 0, 5, 22, 18, 23, 19, 17], [2, 4, 8, 12, 14, 1, 7, 9, 19, 23, 3, 16, 0, 15, 22, 6, 13, 5, 18, 10, 20, 21, 17, 11, 24], [
        3, 8, 9, 14, 10, 2, 21, 13, 6, 4, 0, 7, 16, 22, 11, 5, 24, 20, 1, 18, 17, 19, 15, 23, 12], [13, 15, 10, 20, 0, 5, 1, 7, 9, 6, 19, 14, 21, 3, 2, 12, 18, 16, 17, 22, 23, 11, 24, 4, 8], [9, 5, 16, 8, 18, 22, 7, 13, 14, 12, 20, 23, 11, 24, 21, 1, 6, 10, 15, 3, 17, 2, 0, 4, 19], [15, 7, 24, 1, 10, 3, 8, 2, 20, 22, 18, 14, 5, 4, 9, 12, 16, 6, 0, 17, 19, 13, 23, 21, 11]]
    end_pazzle = []
    for i in range(25):
        end_pazzle.append(i)

    for pazzle in pazzle_list:
        t0 = time.time()
        a_star = AStar(pazzle, end_pazzle)
        t1 = time.time()
        print('AStar')
        print(a_star.solve())
        print(t1 - t0)

        t0 = time.time()
        ida_start = IDAStar(pazzle, end_pazzle)
        t1 = time.time()
        print('IDAStar')
        print(ida_start.solve())
        print(t1 - t0)

    pass


if __name__ == '__main__':
    main()
