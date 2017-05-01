from hgs_24nums_node import HGS24NumsNode as Node
import numpy as np

def test(num):
    num1 = num.copy()
    num1[2] = 0
    print(num1)

start_nums_table = [1,2,3,4,5]
test(start_nums_table)
print(start_nums_table)
