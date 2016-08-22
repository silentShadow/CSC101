import sys
import timeit
from heap_sort import Heap



def sort_The_Heap(the_list):
    """Creating a Heap object and accessing some of the methods from the class"""
    heap = Heap()

    for thingy in the_list:
        heap.add_node(thingy)
    
    for i in range(len(the_list)):
        the_list[len(the_list) - 1 - i] = heap.remove_node()



def main():
    """Main func here"""
    some_list = [-44,-5,-3,3,3,1,-4,0,1,2,4,5,53]
    
    start = timeit.timeit()
    sort_The_Heap(some_list)
    finish = timeit.timeit()

    print("sort_The_Heap took {:.6f} seconds to complete".format(finish - start))



if __name__ == '__main__':
    sys.exit(int(main() or 0))