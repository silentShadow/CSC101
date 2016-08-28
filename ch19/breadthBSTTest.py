'''
rev: 3
title: breadth BST Test
class: CSC102
author: jonathan reiter
description: create 10 nodes and execute the Queue class to print out the nodes
'''


import sys
from BinaryTree import BinaryTree


BLK = "\033[30m"
RED = "\033[31m"
GRN = "\033[32m"
YLW = "\033[33m"
BLU = "\033[34m"
MAG = "\033[35m"
CYN = "\033[36m"
WHT = "\033[37m"
NC  = "\033[39m"
YLW_BLK = "\033[33;40m"
RED_GRN = "\033[31;42m"
GRN_BLK = "\033[32;40m"
GRN_WHT = "\033[42;37m"
WHT_CYN = "\033[37;46m"
WHT_BLK = "\033[37;40m"
WHT_RED = "\033[37;41m"
WHT_YLW = "\033[37;43m"
WHT_RED = "\033[37;41m"
WHT_BLU = "\033[37;44m"
NC_NC   = "\033[39;49m"



def main():
    """pass"""
    b = BinaryTree()
    print(CYN)
    print("size:", b.getSize())
    print("root:", b.getRoot())
    print(NC)
    print("{}Creating 10 elements... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] {}".format(BLU, NC))

    [b.insert(thing) for thing in [0,1,2,3,4,5,6,7,8,9] ]

    print(CYN)
    print("size:", b.getSize())
    print("root:", b.getRoot().element)
    print(NC)

    b.breadth()


if __name__ == '__main__':
    sys.exit(int(main() or 0))