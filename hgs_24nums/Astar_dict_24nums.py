import random
import operator
import bisect

from hgs_24nums_node import HGS24NumsNode as Node
from config import configs


class AStar(object):

    def __init__(self, start_nums_table, end_nums_table):
        self.start_nums_table = start_nums_table
        self.end_nums_table = end_nums_table
        Node.start_nums_table = start_nums_table
        Node.end_nums_table = end_nums_table

        self.open_list = []
        self.open_list_score = []
        self.open_dict = {}

        self.closed_dict = {}

    def open_list_insert(self, node):
        left_index = bisect.bisect_left(self.open_list_score, node.score)
        self.open_list.insert(left_index, node)
        self.open_list_score.insert(left_index, node.score)
        self.open_dict[str(node.nums_table)] = node

    def open_list_remove(self, node):
        left_index = bisect.bisect_left(self.open_list_score, node.score)
        while self.open_list[left_index] != node:
            left_index += 1
            pass
        self.open_list.pop(left_index)
        self.open_list_score.pop(left_index)
        self.open_dict.pop(str(node.nums_table))

    def open_list_pop(self, index):
        node = self.open_list.pop(index)
        self.open_list_score.pop(index)
        self.open_dict.pop(str(node.nums_table))
        return node

    def solve(self):

        start_node = Node(self.start_nums_table)

        self.open_list_insert(start_node)

        node_n = None
        while True:
            if len(self.open_list) == 0:
                print('False')
                return False

            node_n = self.open_list_pop(0)

            self.closed_dict[str(node_n)] = node_n

            if operator.eq(node_n.nums_table, self.end_nums_table):
                break
            node_n_move = []

            moved_node = node_n.blank_up()
            if moved_node is not None:
                node_n_move.append(moved_node)
            moved_node = node_n.blank_down()
            if moved_node is not None:
                node_n_move.append(moved_node)
            moved_node = node_n.blank_right()
            if moved_node is not None:
                node_n_move.append(moved_node)
            moved_node = node_n.blank_left()
            if moved_node is not None:
                node_n_move.append(moved_node)

            no_exist_per = []
            for i in range(len(node_n_move)):
                no_exist_per.append(True)

            node_tmp = node_n.last_node
            while True:
                if node_tmp is None:
                    break
                for i in range(len(node_n_move)):
                    if operator.eq(node_tmp.nums_table, node_n_move[i]. nums_table):
                        no_exist_per[i] = False
                node_tmp = node_tmp.last_node

            for i in range(len(node_n_move)):
                if no_exist_per[i]:
                    node_tmp = node_n_move[i]
                    node_tmp_num_str = str(node_tmp.nums_table)

                    if node_tmp_num_str in self.open_dict:
                        open_node = self.open_dict[node_tmp_num_str]
                        if open_node.move_count > node_tmp.move_count:
                            self.open_list_remove(open_node)
                            self.open_list_insert(node_tmp)
                    elif node_tmp_num_str in self.closed_dict:
                        closed_node = self.closed_dict[node_tmp_num_str]
                        if closed_node.move_count > node_tmp.move_count:
                            closed_node.last_node = node_n
                    else:
                        self.open_list_insert(node_tmp)

            # print('@' + str(len(self.open_list) + len(self.closed_dict)) + " ")
            # self.open_list.sort(key=node_compare)

        node_tmp = node_n.last_node
        move_steep = node_tmp.last_move
        while True:
            if node_tmp is None:
                break
            move_steep = node_tmp.last_move + move_steep
            node_tmp = node_tmp.last_node
        return {
            'move_steep': move_steep,
            'move_count': node_n.move_count
        }


def inversion_num_is_even(nums):
    nums_list = nums.copy()
    nums_list.remove(0)
    print(nums_list)
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
    a_star = AStar(start_nums_table, end_nums_table)
    print(a_star.solve())


if __name__ == '__main__':
    main()
