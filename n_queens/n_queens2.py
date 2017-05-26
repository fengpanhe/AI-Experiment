import random
import numpy as np


class NQueens(object):
    def __init__(self, n):
        self.queens_num = n
        self.queens_location = np.arange(0, self.queens_num)
        self.conflict_slope = set()
        self.slope_queens = {}
        self.conflict_num = 0

    def get_conflict_num(self):
        return self.conflict_num

    def reset_board(self):
        '''复盘'''
        print('reset')
        random.shuffle(self.queens_location)
        self.conflict_slope = set()
        self.slope_queens = {}
        self.conflict_num = 0
        col_list = []
        # print(self.queens_location)
        for i in self.queens_location:
            col_list.append(i)
        index = 0
        tmp_set = set()
        while index < self.queens_num - 100:
            col = col_list[random.randint(0, len(col_list) - 1)]
            # print(col)
            slope1 = index - col
            slope2 = index + col
            if slope1 not in tmp_set and slope2 not in tmp_set:
                self.queens_location[index] = col
                col_list.remove(col)
                tmp_set.add(slope1)
                tmp_set.add(slope2)
                index += 1
                # print(index)
        # print(col_set)
        for i in col_list:
            self.queens_location[index] = i
            index += 1
        for i in range(self.queens_num):
            self.add_queen(i)
        print(self.queens_location)

    def add_queen(self, i):
        slope1 = i - self.queens_location[i]
        slope2 = i + self.queens_location[i]
        if slope1 in self.slope_queens:
            self.conflict_num += 1
            self.slope_queens[slope1].add(i)
            self.conflict_slope.add(slope1)
        else:
            self.slope_queens[slope1] = set([i])

        if slope1 == slope2:
            return

        if slope2 in self.slope_queens:
            self.conflict_num += 1
            self.slope_queens[slope2].add(i)
            # self.conflict_num += 1
            self.conflict_slope.add(slope2)
        else:
            self.slope_queens[slope2] = set([i])

    def remove_queen(self, i):
        slope1 = i - self.queens_location[i]
        slope2 = i + self.queens_location[i]
        self.slope_queens[slope1].remove(i)

        if len(self.slope_queens[slope1]) == 0:
            self.slope_queens.pop(slope1)
        elif len(self.slope_queens[slope1]) == 1:
            self.conflict_slope.remove(slope1)
            self.conflict_num -= 1
        else:
            self.conflict_num -= 1

        if slope1 == slope2:
            return

        self.slope_queens[slope2].remove(i)
        if len(self.slope_queens[slope2]) == 0:
            self.slope_queens.pop(slope2)
        elif len(self.slope_queens[slope2]) == 1:
            self.conflict_slope.remove(slope2)
            self.conflict_num -= 1
        else:
            self.conflict_num -= 1

    def swap(self, x, y):
        # print(str(x) + ' ' + str(y))
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
        # print(self.conflict_num)
        # return
        next_conflict_num = 0
        # count = 0
        times = 0

        while(True):
            if len(self.conflict_slope) == 0:
                print('true')
                break

            if next_conflict_num == self.conflict_num:
                self.reset_board()
                times += 1
            next_conflict_num = self.conflict_num
            print('next_conflict_num' + str(next_conflict_num))

            tmp_conflict_queens = []
            for tmp_slope in self.conflict_slope:
                for x in self.slope_queens[tmp_slope]:
                    tmp_conflict_queens.append(x)
            for x in tmp_conflict_queens:
                for y in range(0, self.queens_num):
                    if self.swap(x, y):
                        break

        print('times')
        print(times)
        return self.queens_location


if __name__ == '__main__':
    queens_num = 1000000
    n_queens = NQueens(queens_num)
    queens_location = n_queens.solve()
    # queens_location = [7, 5, 2, 1, 6, 0, 3, 4]
    # print(queens_location)
    board = np.zeros((queens_num, queens_num))
    for i in range(queens_num):
        board[i][queens_location[i]] = 1
    print(board)
