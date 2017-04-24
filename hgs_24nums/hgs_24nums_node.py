import numpy as np
class HGS24NumsNode(object):
    start_nums_table = ''
    end_nums_table = ''
    '''
    启发式搜索算法的节点
    '''
    def __init__(self, param, type):
        '''
        nums_table: 数码表
        '''
        if type == 0:
            self.nums_table = np.array(param)
            self.score = 0
            self.calc_graph_score()
            self.last_move = ''
            self.blank_location = self.get_blank_location()
            self.last_node = 0
        else:
            self.nums_table = np.array(param.nums_table)
            self.score = param.score
            self.last_move = param.last_move
            self.blank_location = [param.blank_location[0],param.blank_location[1]]
            self.last_node = param


    def get_graph_score(self):
        return self.score

    def calc_graph_score(self):
        print(" ")

    def get_blank_location(self):
        for i in range(5):
            for j in range(5):
                if self.nums_table[i][j] == -1:
                    return [i,j]
        return [0,0]

    def blank_up(self):
        '''
        数码表空位置上移
        若不能移则返回NULL
        '''
        if self.last_move == 'down' or self.blank_location[1] == 0:
            return False
        x = self.blank_location[0]
        y = self.blank_location[1]
        self.nums_table[x][y] = self.nums_table[x][y - 1]
        self.nums_table[x][y - 1] =-1

        self.last_move = 'up'
        self.blank_location = [x, y - 1]
        self.calc_graph_score
        return True

    def blank_down(self):
        '''
        数码表空位置下移
        若不能移则返回NULL
        '''
        if self.last_move == 'up' or self.blank_location[1] == 4:
            return False
        x = self.blank_location[0]
        y = self.blank_location[1]
        self.nums_table[x][y] = self.nums_table[x][y + 1]
        self.nums_table[x][y + 1] =-1

        self.last_move = 'down'
        self.blank_location = [x, y + 1]
        self.calc_graph_score
        return True

    def blank_right(self):
        '''
        数码表空位置右移
        若不能移则返回NULL
        '''
        if self.last_move == 'left' or self.blank_location[0] == 4:
            return False
        x = self.blank_location[0]
        y = self.blank_location[1]
        self.nums_table[x][y] = self.nums_table[x + 1][y]
        self.nums_table[x + 1][y] =-1

        self.last_move = 'right'
        self.blank_location = [x + 1, y]
        self.calc_graph_score
        return True

    def blank_left(self):
        '''
        数码表空位置右移
        若不能移则返回NULL
        '''
        if self.last_move == 'right' or self.blank_location[0] == 0:
            return False
        x = self.blank_location[0]
        y = self.blank_location[1]
        self.nums_table[x][y] = self.nums_table[x - 1][y]
        self.nums_table[x - 1][y] =-1

        self.last_move = 'left'
        self.blank_location = [x - 1, y]
        self.calc_graph_score
        return True