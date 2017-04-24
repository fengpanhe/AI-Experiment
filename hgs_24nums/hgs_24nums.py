import numpy as np
import hgs_24nums_node as node

open_list = []
closed_list = []
start_nums_table = ''
end_nums_table = ''



def main():
    start_nums_table = np.array(
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,-1]
    )
    end_nums_table = np.array(
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,-1],
        [0,0,0,0,0]
    )
    hgs_24nums_node.start_nums_table = start_nums_table
    hgs_24nums_node.end_nums_table = end_nums_table

    start_node = hgs_24nums_node(start_nums_table,0)
    open_list.append(start_node)

    while True:
        if len(open_list) == 0:
            return False
        
        node_n = open_list.pop(0)
        closed_list.append(node_n)

        if (node_n.nums_table == end_nums_table).all():
            return True
        
        node_n_move = [Node(node_n),Node(node_n),Node(node_n),Node(node_n)]
        move_succeed = []
        move_succeed.append(node_n_move[0].blank_up())
        move_succeed.append(node_n_move[1].blank_down())
        move_succeed.append(node_n_move[2].blank_right())
        move_succeed.append(node_n_move[3].blank_left())

        for i in range(len(node_n_move)):
            if move_succeed[i]:
                no_exist = True
                node_tmp = node_n.last_node
                while True:
                    if node_tmp.nums_table == 0:
                        break
                    if (node_tmp.nums_table == node_n_move[i].nums_table).all():
                        no_exist = False
                    node_tmp = node_tmp.last_node

                if no_exist:
                    open_list.append(node_n_move[i])

        
        
                

