import random
import numpy as np


class NQueens(object):
    def __init__(self, n):
        self.queens_num = n
        self.queens_location = np.arange(0, self.queens_num)
        self.conflict_queens = {}
        self.conflict_num = 0

    def get_conflict_num(self):
        print(self.conflict_num)
        print(self.conflict_queens)
        return self.conflict_num

    def reset_board(self):
        '''复盘'''
        random.shuffle(self.queens_location)
        self.conflict_queens = {}
        self.conflict_num = 0
        for i in range(self.queens_num):
            tmp_array = self.queens_location.copy()
            tmp_array += i - self.queens_location[i]
            tmp_array -= np.arange(0, self.queens_num)
            for j in np.where(tmp_array == 0)[0]:
                self.add_conflict_queens(i, j)
        # for i in range(self.queens_num):
        #     slope1 = self.queens_location[i] - i
        #     slope2 = self.queens_location[i] + i
        #     if slope1 in self.conflict_queens:
        #         self.conflict_queens[slope1].add(i)
        #         self.conflict_num += 1
        #     else:
        #         self.conflict_queens[slope1] = set([i])
        #     if slope2 in self.conflict_queens:
        #         self.conflict_queens[slope2].add(i)
        #         self.conflict_num += 1
        #     else:
        #         self.conflict_queens[slope2] = set([i])


    def add_conflict_queens(self, i, j):
        if i == j:
            return
        if i in self.conflict_queens:
            if j not in self.conflict_queens[i]:
                self.conflict_queens[i].add(j)
                self.conflict_num += 1
        else:
            self.conflict_queens[i] = set([j])
            self.conflict_num += 1
            pass
        if j in self.conflict_queens:
            if i not in self.conflict_queens[j]:
                self.conflict_queens[j].add(i)
                self.conflict_num += 1
        else:
            self.conflict_queens[j] = set([i])
            self.conflict_num += 1
            pass

    def remove_conflict_queen(self, x):
        if x in self.conflict_queens:
            self.conflict_num -= 2 * len(self.conflict_queens[x])
            for queen_id in self.conflict_queens[x]:
                self.conflict_queens[queen_id].remove(x)
                if len(self.conflict_queens[queen_id]) == 0:
                    self.conflict_queens.pop(queen_id)
            self.conflict_queens.pop(x)

    def solve(self):
        self.reset_board()
        # print(self.conflict_num)
        # return
        next_conflict_num = 0
        count = 0
        times = 0
        while(True):
            times += 1
            if next_conflict_num == self.conflict_num:
                count += 1
            else:
                count = 0
            next_conflict_num = self.conflict_num
            print('next_conflict_num' + str(next_conflict_num))
            if count > self.queens_num:
                self.reset_board()
                count = 0

            # print(self.queens_location)
            # print(self.conflict_matrix)
            if self.get_conflict_num() == 0:
                print('true')
                print(self.conflict_queens)
                break

            # print(len(self.conflict_queens))
            index = random.randint(0, len(self.conflict_queens) - 1)
            x = list(self.conflict_queens.keys())[index]
            y = random.randint(0, self.queens_num - 1)
            # print(str(x) + str(y))
            xy_conflict_num = 0
            xy_conflict_num += len(self.conflict_queens[x])
            if y in self.conflict_queens:
                xy_conflict_num += len(self.conflict_queens[y])

            yx_conflict_num = 0
            queens_location_swap_xy = self.queens_location.copy()
            queens_location_swap_xy[x] = self.queens_location[y]
            queens_location_swap_xy[y] = self.queens_location[x]
            tmp_array_x = queens_location_swap_xy.copy()
            tmp_array_x += x - queens_location_swap_xy[x]
            tmp_array_x -= np.arange(0, self.queens_num)
            yx_conflict_num += self.queens_num - np.count_nonzero(tmp_array_x)
            tmp_array_y = queens_location_swap_xy.copy()
            tmp_array_y += y - queens_location_swap_xy[y]
            tmp_array_y -= np.arange(0, self.queens_num)
            yx_conflict_num += self.queens_num - np.count_nonzero(tmp_array_y)
            yx_conflict_num -= 2

            if xy_conflict_num > yx_conflict_num:
                self.queens_location = queens_location_swap_xy
                self.remove_conflict_queen(x)
                self.remove_conflict_queen(y)
                for i in np.where(tmp_array_x == 0)[0]:
                    self.add_conflict_queens(i, x)
                for i in np.where(tmp_array_y == 0)[0]:
                    self.add_conflict_queens(i, y)
        print('times')
        print(times)
        return self.queens_location


if __name__ == '__main__':
    queens_num = 1000
    n_queens = NQueens(queens_num)
    queens_location = n_queens.solve()
    # queens_location = [7, 5, 2, 1, 6, 0, 3, 4]
    # print(queens_location)
    board = np.zeros((queens_num, queens_num))
    for i in range(queens_num):
        board[i][queens_location[i]] = 1
    print(board)
