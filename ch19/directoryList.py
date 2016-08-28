'''
rev: 1
title: directory list
class: CSC102
author: jonathan reiter
description: implements the methods from the Stack class to run over a given path and its found contents
'''


import os
import sys
from stack_class import Stack



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



def scan_Dir(the_path):
    """doc"""
    the_stack = Stack()
    the_stack.push(the_path)

    #print(the_stack._Stack__elements)
    #print(the_stack.peek())


    while not the_stack.isEmpty():          # while the stack is not empty
        popped = the_stack.pop()
        print("{}Popped {}{}{} from the stack{}".format(YLW, MAG, popped, YLW, NC))
        if os.path.isdir(popped):
            for entry in os.scandir(popped):
                if not entry.name.startswith(('.', '$')) and entry.is_dir():            # Dont show files that are hidden (.) or that start with '$' 
                    print("D--- {}{}{}".format(CYN, entry.name, NC), end='')
                    print("{}\tInvoking push on {}{}{}".format(GRN, CYN, entry.name, NC))
                    the_stack.push(entry.path)
                elif not entry.name.startswith('.') and entry.is_file():
                    print("---- {}{}{}".format(RED, entry.name, NC))
                    
        
    print("{}Stack is empty{}".format(WHT_RED, NC_NC))
        



def get_Folder():
    try:
        cur_dir = os.getcwd()

        print("{}You are here: \n\t{}{}{}".format(BLU, WHT_BLK, cur_dir, NC_NC))
        print("{}Do you wish to scan this folder?{} [ {}PRESS ENTER{} = {}accept current path{}, {}PATH{} = {}specify new path{} ] \n\t".format(WHT_BLU, NC_NC,       # for the question
                                                                                                                                                WHT_RED, NC_NC,       # for ENTER
                                                                                                                                                YLW_BLK, NC_NC,
                                                                                                                                                WHT_YLW, NC_NC,       # for PATH     
                                                                                                                                                YLW_BLK, NC_NC))
        usr_choice = input()
        if usr_choice == "":
                return cur_dir

        while not os.path.isdir(usr_choice.strip()):
            print("{}Valid directory needed...{}".format(WHT_RED, NC_NC))
            print("{}You can press ENTER to accept current directory{}".format(WHT_BLU, NC_NC))
            usr_choice = input()
            if usr_choice == "":
                return cur_dir
        else:
            return usr_choice.strip()

    except KeyboardInterrupt as kybd:
        print("\n{}User killed program, exiting{}".format(WHT_RED, NC_NC))
        sys.exit()

    except Exception as err:
        print("\n{}Error raised:{} {}{}{}".format(WHT_RED, NC_NC, RED, err, NC))
        sys.exit()



def main():
    """The main function"""

    # Determine the folder
    usr_path = get_Folder()
    #usr_path = input("Give an absolute path... ").strip()

    scan_Dir(usr_path)



if __name__ == '__main__':
    sys.exit(int(main() or 0))