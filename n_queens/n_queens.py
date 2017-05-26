import random
import numpy as np


class NQueens(object):
    def __init__(self, n):
        self.queens_num = n
        self.queens_location = []
        self.conflict_matrix = np.zeros((n, n), int)
        self.conflict_num = 0
        for i in range(self.queens_num):
            self.queens_location.append(i)

    def get_conflict_num(self):
        self.conflict_num = np.count_nonzero(self.conflict_matrix)
        print(self.conflict_num)
        return self.conflict_num

    def reset_board(self):
        '''复盘'''
        random.shuffle(self.queens_location)
        self.conflict_matrix = np.zeros((self.queens_num, self.queens_num), int)
        for i in range(self.queens_num):
            for j in range(i + 1, self.queens_num):
                if abs(j - i) == abs(self.queens_location[i] -
                                     self.queens_location[j]):
                    self.conflict_matrix[i][j] = 1
                    self.conflict_matrix[j][i] = 1
    # def conflict_i_j(self, i, j):
    #     if i in self.conflict_dict:
    #         if j not in self.conflict_dict[i]:
    #             self.conflict_dict[i][j] = 1
    #             self.conflict_num += 1
    #     else:
    #         self.conflict_dict[i] = {j: 1}
    #         pass
    #     if j in self.conflict_dict:
    #         if i not in self.conflict_dict[j]:
    #             self.conflict_dict[j][i] = 1
    #             self.conflict_num += 1
    #     else:
    #         self.conflict_dict[j] = {i: 1}
    #         pass

    def solve(self):
        self.reset_board()
        next_conflict_num = 0
        count = 0
        while(True):
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
                print(self.conflict_matrix)
                return self.queens_location

            rows = np.where(self.conflict_matrix == 1)[0]
            # cols = np.where(self.conflict_matrix == 1)[1]
            index = random.randint(0, len(rows) - 1)
            x = rows[index]
            y = random.randint(0, self.queens_num - 1)
            # print(str(x) + str(y))
            xy_conflict_num = 0
            xy_conflict_num += np.count_nonzero(self.conflict_matrix[x])
            xy_conflict_num += np.count_nonzero(self.conflict_matrix[y])
            for i in range(self.queens_num):
                if i == x or i == y:
                    continue
                if self.conflict_matrix[i][x] == 1:
                    xy_conflict_num += 1
                if self.conflict_matrix[i][y] == 1:
                    xy_conflict_num += 1
            yx_conflict_num = 0
            for i in range(self.queens_num):
                if i == x or i == y:
                    continue
                if abs(i - x) == abs(self.queens_location[i] -
                                     self.queens_location[y]):
                    yx_conflict_num += 2
                if abs(i - y) == abs(self.queens_location[i] -
                                     self.queens_location[x]):
                    yx_conflict_num += 2
            if abs(x - y) == abs(self.queens_location[x] -
                                 self.queens_location[y]):
                yx_conflict_num += 2

            if xy_conflict_num > yx_conflict_num:
                tmp = self.queens_location[x]
                self.queens_location[x] = self.queens_location[y]
                self.queens_location[y] = tmp
                self.conflict_matrix[x] = 0
                self.conflict_matrix[y] = 0
                for i in range(self.queens_num):
                    self.conflict_matrix[i][x] = 0
                    self.conflict_matrix[i][y] = 0
                for i in range(self.queens_num):
                    if i == x or i == y:
                        continue
                    if abs(i - x) == abs(self.queens_location[i] -
                                         self.queens_location[x]):
                        self.conflict_matrix[i][x] = 1
                        self.conflict_matrix[x][i] = 1
                    if abs(i - y) == abs(self.queens_location[i] -
                                         self.queens_location[y]):
                        self.conflict_matrix[i][y] = 1
                        self.conflict_matrix[y][i] = 1
                if abs(x - y) == abs(self.queens_location[x] -
                                     self.queens_location[y]):
                    self.conflict_matrix[x][y] = 1
                    self.conflict_matrix[y][x] = 1


if __name__ == '__main__':
    queens_num = 1000
    n_queens = NQueens(queens_num)
    queens_location = n_queens.solve()
    queens_location = [7, 5, 2, 1, 6, 0, 3, 4]
    print(queens_location)
    board = np.zeros((queens_num, queens_num))
    for i in range(queens_num):
        board[i][queens_location[i]] = 1
    print(board)
