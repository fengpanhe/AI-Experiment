import numpy as np
import math
class HGS24NumsNode(object):
    start_nums_table = ''
    end_nums_table = ''
    r_num = 3
    c_num = 3
    '''
    启发式搜索算法的节点
    '''
    def __init__(self, param, type = 1):
        '''
        nums_table: 数码表
        '''
        if type == 0:
            print('start')
            self.nums_table = param.copy()
            self.score = 0
            self.last_move = ''
            self.blank_location = self.get_blank_location()
            self.last_node = None
            self.move_count = 0
            self.calc_graph_score()
        else:
            self.nums_table = param.nums_table.copy()
            self.score = param.score
            self.last_move = param.last_move
            self.blank_location = param.blank_location
            self.last_node = param
            self.move_count = param.move_count
        
        # self.next_nodes = []

    def calc_graph_score(self):
        h = 0
        for i in range(len(self.nums_table)):
            j = HGS24NumsNode.end_nums_table.index(self.nums_table[i])
            i_x = i % HGS24NumsNode.c_num
            i_y = int(i / HGS24NumsNode.c_num)
            j_x = j % HGS24NumsNode.c_num
            j_y = int(j / HGS24NumsNode.c_num)
            h += (abs(i_x - j_x) + abs(i_y - j_y))
        self.score = self.move_count + h

    def get_blank_location(self):
        return self.nums_table.index(0)

    def blank_move(self,index2):
        index1 = self.blank_location
        tmp = self.nums_table[index1]
        self.nums_table[index1] = self.nums_table[index2]
        self.nums_table[index2] = tmp
        self.blank_location = index2
        self.move_count += 1
        self.calc_graph_score()


    def blank_up(self):
        '''
        数码表空位置上移
        若不能移则返回NULL
        '''
        index = self.blank_location - HGS24NumsNode.c_num
        if self.last_move == 'down' or index < 0 :
            return False
        self.last_move = 'up'

        self.blank_move(index)

        # index1 = self.blank_location
        # index2 = self.blank_location - HGS24NumsNode.c_num
        # tmp = self.nums_table[index1]
        # self.nums_table[index1] = self.nums_table[index2]
        # self.nums_table[index2] = tmp
        # self.blank_location = index2
        # self.move_count += 1
        # self.calc_graph_score()
        return True

    def blank_down(self):
        '''
        数码表空位置下移
        若不能移则返回NULL
        '''
        index = self.blank_location + HGS24NumsNode.c_num
        if self.last_move == 'up' or index >= len(self.nums_table):
            return False
        self.last_move = 'down'
        self.blank_move(index)
        return True

    def blank_right(self):
        '''
        数码表空位置右移
        若不能移则返回NULL
        '''
        index = self.blank_location + 1
        if self.last_move == 'left' or index % HGS24NumsNode.c_num == 0:
            return False

        self.last_move = 'right'
        self.blank_move(index)
        return True

    def blank_left(self):
        '''
        数码表空位置右移
        若不能移则返回NULL
        '''
        index = self.blank_location - 1
        if self.last_move == 'right' or self.blank_location % HGS24NumsNode.c_num == 0:
            return False
        self.last_move = 'left'
        self.blank_move(index)
        return True