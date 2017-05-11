import random
import operator

from hgs_24nums_node import HGS24NumsNode as Node
from config import configs

open_list = []
closed_list = []
start_nums_table = ''
end_nums_table = ''


def node_compare(x):
    return x.score


def hgs(start_nums_table, end_nums_table):
    Node.start_nums_table = start_nums_table
    Node.end_nums_table = end_nums_table

    start_node = Node(start_nums_table)
    open_list.append(start_node)

    while True:
        if len(open_list) == 0:
            print('False')
            return False

        node_n = open_list.pop(0)
        closed_list.append(node_n)

        if operator.eq(node_n.nums_table, end_nums_table):
            print(node_n.move_count)
            print('true')
            return True

        node_n_move = []
        node_n_move0 = node_n.new_node()
        node_n_move1 = node_n.new_node()
        node_n_move2 = node_n.new_node()
        node_n_move3 = node_n.new_node()

        if node_n_move0.blank_up():
            node_n_move.append(node_n_move0)
        if node_n_move1.blank_down():
            node_n_move.append(node_n_move1)
        if node_n_move2.blank_right():
            node_n_move.append(node_n_move2)
        if node_n_move3.blank_left():
            node_n_move.append(node_n_move3)

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
                open_list.append(node_tmp)
                i = 0
                for open_node in open_list[:len(open_list) - 1]:
                    if operator.eq(open_node.nums_table, node_tmp.nums_table):
                        if open_node.move_count > node_tmp.move_count:
                            open_list.remove(open_node)
                        else:
                            open_list.remove(node_tmp)
                            pass
                        break
                    i += 1
                if i != len(open_list) - 1:
                    break
                for closed_node in closed_list:
                    if operator.eq(closed_node.nums_table,
                                   node_tmp.nums_table):
                        if closed_node.move_count <= node_tmp.move_count:
                            if open_list.count(node_tmp) != 0:
                                open_list.remove(node_tmp)
                        else:
                            closed_node.last_node = node_n
                    break

        print('@' + str(len(open_list) + len(closed_list)) + " ")
        open_list.sort(key=node_compare)


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
