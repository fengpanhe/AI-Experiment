import random
import numpy as np
import time


class NQueens(object):
    def __init__(self, n):
        self.queens_num = n
        self.queens_location = np.arange(0, self.queens_num)
        self.conflict_slope1 = set()
        self.conflict_slope2 = set()
        self.slope_queens1 = {}
        self.slope_queens2 = {}
        self.conflict_num = 0

    def get_conflict_num(self):
        return self.conflict_num

    def reset_board(self):
        '''复盘'''
        print('reset')
        random.shuffle(self.queens_location)
        self.conflict_slope1 = set()
        self.conflict_slope2 = set()
        self.slope_queens1 = {}
        self.slope_queens2 = {}
        self.conflict_num = 0
        col_list = set(self.queens_location)
        index = 0
        while index < self.queens_num - 100:
            col = col_list.pop()
            slope1 = index - col
            slope2 = index + col
            if slope1 not in self.slope_queens1 and slope2 not in self.slope_queens2:
                self.queens_location[index] = col
                self.add_queen(index)
                index += 1
            else:
                col_list.add(col)
        for i in col_list:
            self.queens_location[index] = i
            self.add_queen(index)
            index += 1

    def add_queen(self, i):
        slope1 = i - self.queens_location[i]
        slope2 = i + self.queens_location[i]
        if slope1 in self.slope_queens1:
            self.conflict_num += 1
            self.slope_queens1[slope1].add(i)
            self.conflict_slope1.add(slope1)
        else:
            self.slope_queens1[slope1] = set([i])

        if slope1 == slope2:
            return

        if slope2 in self.slope_queens2:
            self.conflict_num += 1
            self.slope_queens2[slope2].add(i)
            self.conflict_slope2.add(slope2)
        else:
            self.slope_queens2[slope2] = set([i])

    def remove_queen(self, i):
        slope1 = i - self.queens_location[i]
        slope2 = i + self.queens_location[i]
        self.slope_queens1[slope1].remove(i)

        if len(self.slope_queens1[slope1]) == 0:
            self.slope_queens1.pop(slope1)
        elif len(self.slope_queens1[slope1]) == 1:
            self.conflict_slope1.remove(slope1)
            self.conflict_num -= 1
        else:
            self.conflict_num -= 1

        if slope1 == slope2:
            return

        self.slope_queens2[slope2].remove(i)
        if len(self.slope_queens2[slope2]) == 0:
            self.slope_queens2.pop(slope2)
        elif len(self.slope_queens2[slope2]) == 1:
            self.conflict_slope2.remove(slope2)
            self.conflict_num -= 1
        else:
            self.conflict_num -= 1

    def swap(self, x, y):
        if x == y:
            return False
        fx = self.queens_location[x]
        fy = self.queens_location[y]
        xy_conflict_num = self.conflict_num

        self.remove_queen(x)
        self.remove_queen(y)
        self.queens_location[x] = fy
        self.queens_location[y] = fx
        self.add_queen(x)
        self.add_queen(y)

        yx_conflict_num = self.conflict_num

        if xy_conflict_num < yx_conflict_num:
            self.remove_queen(x)
            self.remove_queen(y)
            self.queens_location[x] = fx
            self.queens_location[y] = fy
            self.add_queen(x)
            self.add_queen(y)
            return False
        return True

    def solve(self):
        self.reset_board()
        print(self.conflict_num)
        next_conflict_num = 0
        times = 0
        count = 0
        while(True):
            if self.conflict_num == 0:
                print('true')
                break
            if next_conflict_num == self.conflict_num:
                count += 1
            if count > 3:
                self.reset_board()
                times += 1
            next_conflict_num = self.conflict_num
            print('next_conflict_num' + str(next_conflict_num))

            tmp_conflict_queens = set()
            for tmp_slope in self.conflict_slope1:
                for x in self.slope_queens1[tmp_slope]:
                    tmp_conflict_queens.add(x)
            for tmp_slope in self.conflict_slope2:
                for x in self.slope_queens2[tmp_slope]:
                    tmp_conflict_queens.add(x)
            for x in tmp_conflict_queens:
                for y in range(0, self.queens_num):
                    if self.swap(x, y):
                        break

        print('times')
        print(times)
        return self.queens_location


if __name__ == '__main__':
    queens_num = 100000
    n_queens = NQueens(queens_num)
    time_start = time.time()
    queens_location = n_queens.solve()
    time_end = time.time()
    print(time_end - time_start)
