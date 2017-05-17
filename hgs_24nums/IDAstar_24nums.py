import random
import operator

from ida_star_node import IdaStarNode as Node
from config import configs


class IDAStar(object):
    """docstring for  ida_star"""

    def __init__(self, start_nums_table, end_nums_table):
        self.start_nums_table = start_nums_table
        self.end_nums_table = end_nums_table
        self.stop_depth = 0
        Node.start_nums_table = start_nums_table
        Node.end_nums_table = end_nums_table

    def extend_node(self, node):
        # print(node.move_count)
        if operator.eq(node.nums_table, self.end_nums_table):
            # print('true')
            return node.last_move
        if node.score > self.stop_depth:
            return None
        return_move = None
        moved_node = node.blank_up()
        if moved_node is not None:
            return_move = self.extend_node(moved_node)
            if return_move is not None:
                return node.last_move + return_move
        moved_node = node.blank_down()
        if moved_node is not None:
            return_move = self.extend_node(moved_node)
            if return_move is not None:
                return node.last_move + return_move
        moved_node = node.blank_right()
        if moved_node is not None:
            return_move = self.extend_node(moved_node)
            if return_move is not None:
                return node.last_move + return_move
        moved_node = node.blank_left()
        if moved_node is not None:
            return_move = self.extend_node(moved_node)
            if return_move is not None:
                return node.last_move + return_move
        return None

    def solve(self):
        start_node = Node(self.start_nums_table)
        self.stop_depth += start_node.score
        # h = 0
        # for i in range(len(self.start_nums_table)):
        #     j = self.end_nums_table.index(self.start_nums_table[i])
        #     i_x = i % configs['COLNUM']
        #     i_y = int(i / configs['COLNUM'])
        #     j_x = j % configs['COLNUM']
        #     j_y = int(j / configs['COLNUM'])
        #     h += (abs(i_x - j_x) + abs(i_y - j_y))
        # self.stop_depth = h
        print(self.stop_depth)
        result_move = None
        while result_move is None:
            result_move = self.extend_node(start_node)
            self.stop_depth += 1
            pass
        return {
            'move_steep': result_move,
            'move_count': len(result_move)
        }


def inversion_num_is_even(nums):
    nums_list = nums.copy()
    nums_list.remove(0)
    inversion_num = 0
    for i in range(len(nums_list) - 1):
        for j in range(i + 1, len(nums_list)):
            if nums_list[i] > nums_list[j]:
                inversion_num += 1
    print(inversion_num)
    if inversion_num % 2 == 0:
        return True
    else:
        return False
        pass


def main():
    r_num = configs['ROWNUM']
    c_num = configs['COLNUM']
    nums = []
    for i in range(r_num * c_num):
        nums.append(i)

    random.shuffle(nums)
    start_inversion_attribute = inversion_num_is_even(nums)
    start_nums_table = nums.copy()
    # start_nums_table = [0, 1, 4, 2, 7, 6, 3, 8, 5]
    print('start_nums_table:')
    print(start_nums_table)

    random.shuffle(nums)
    while start_inversion_attribute != inversion_num_is_even(nums):
        random.shuffle(nums)
    end_nums_table = nums.copy()
    # end_nums_table = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    print('end_nums_table:')
    print(end_nums_table)
    ida_star = IDAStar(start_nums_table, end_nums_table)
    print(ida_star.solve())


if __name__ == '__main__':
    main()
