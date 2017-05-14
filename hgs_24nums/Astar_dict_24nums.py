import random
import operator
import bisect

from hgs_24nums_node import HGS24NumsNode as Node
from config import configs

open_list = []
open_list_score = []
open_dict = {}

closed_dict = {}
start_nums_table = ''
end_nums_table = ''


def open_list_insert(node):
    left_index = bisect.bisect_left(open_list_score, node.score)
    open_list.insert(left_index, node)
    open_list_score.insert(left_index, node.score)
    open_dict[str(node.nums_table)] = node


def open_list_remove(node):
    left_index = bisect.bisect_left(open_list_score, node.score)
    while open_list[left_index] != node:
        left_index += 1
        pass
    open_list.pop(left_index)
    open_list_score.pop(left_index)
    open_dict.pop(str(node.nums_table))


def open_list_pop(index):
    node = open_list.pop(index)
    open_list_score.pop(index)
    open_dict.pop(str(node.nums_table))
    return node


def node_compare(x):
    return x.score


def hgs(start_nums_table, end_nums_table):
    Node.start_nums_table = start_nums_table
    Node.end_nums_table = end_nums_table

    start_node = Node(start_nums_table)

    open_list_insert(start_node)

    while True:
        if len(open_list) == 0:
            print('False')
            return False

        node_n = open_list_pop(0)

        closed_dict[str(node_n)] = node_n

        if operator.eq(node_n.nums_table, end_nums_table):
            print(node_n.move_count)
            print('true')
            return True

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
                if operator.eq(node_tmp.nums_table, node_n_move[i].nums_table):
                    no_exist_per[i] = False
            node_tmp = node_tmp.last_node

        for i in range(len(node_n_move)):
            if no_exist_per[i]:
                node_tmp = node_n_move[i]
                node_tmp_num_str = str(node_tmp.nums_table)

                if node_tmp_num_str in open_dict:
                    open_node = open_dict[node_tmp_num_str]
                    if open_node.move_count > node_tmp.move_count:
                        open_list_remove(open_node)
                        open_list_insert(node_tmp)
                elif node_tmp_num_str in closed_dict:
                    closed_node = closed_dict[node_tmp_num_str]
                    if closed_node.move_count > node_tmp.move_count:
                        closed_node.last_node = node_n
                else:
                    open_list_insert(node_tmp)

        print('@' + str(len(open_list) + len(closed_dict)) + " ")
        # open_list.sort(key=node_compare)


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
    hgs(start_nums_table, end_nums_table)


main()
