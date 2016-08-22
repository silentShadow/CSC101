"""
      rev   :  12
     title  :  sort Comparison
description :  grab the execution times of every sort method using a defined size of arrays
    author  :  jonathan reiter
 reference  :  None
"""



import sys
import timeit
from random import randint
from heap_sort import Heap
from quick_sort import Quick
from merge_sort_class import Merge
from radix_sort_class import Radix
from bubble_sort_class import Bubble
from selection_sort_class import Selection_Sort



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
CYN_WHT = "\033[36;47m"
WHT_MAG = "\033[37;45m"
WHT_RED = "\033[37;41m"
WHT_CYN = "\033[37;46m"
WHT_BLK = "\033[37;40m"
WHT_GRN = "\033[37;42m"
WHT_YLW = "\033[37;43m"
WHT_RED = "\033[37;41m"
WHT_BLU = "\033[37;44m"
NC_NC   = "\033[39;49m"




def pretty_Print(select, bubble, merge, quick, heap, radixes):
    """doc"""


    sel = select
    bub = bubble
    mer = merge
    qui = quick
    hea = heap
    rad = radixes
    q   = Quick()

    
    q.quick_Sort(sel)
    q.quick_Sort(bub)
    q.quick_Sort(mer)
    q.quick_Sort(qui)
    q.quick_Sort(hea)
    q.quick_Sort(rad)


    #[print("selection times: ", x) for x in sel]



    grid = """
{}Arraysize    {}   Selection   {}    Bubble    {}     Merge     {}    Quick    {}    Heap    {}    Radix    {}
{}            |
{}            |
{}50,000{}      |{}    {:.4f}       {:.4f}       {:.4f}        {:.4f}     {:.4f}      {:.4f}          {}seconds
{}            |
{}____________|__________________________________________________________________________________
{}            |
{}            |
{}100,000{}     |{}    {:.4f}       {:.4f}       {:.4f}        {:.4f}     {:.4f}      {:.4f}          {}seconds
{}            |
{}____________|__________________________________________________________________________________
{}            |
{}            |
{}150,000{}     |{}    {:.4f}       {:.4f}       {:.4f}        {:.4f}     {:.4f}      {:.4f}          {}seconds
{}            |
{}____________|__________________________________________________________________________________
{}            |
{}            |
{}200,000{}     |{}    {:.4f}       {:.4f}       {:.4f}        {:.4f}     {:.4f}      {:.4f}          {}seconds
{}            |
{}____________|__________________________________________________________________________________
{}            |
{}            |
{}250,000{}     |{}    {:.4f}       {:.4f}       {:.4f}        {:.4f}     {:.4f}      {:.4f}          {}seconds
{}            |
{}____________|__________________________________________________________________________________
{}            |
{}            |
{}300,000{}     |{}    {:.4f}       {:.4f}       {:.4f}        {:.4f}     {:.4f}      {:.4f}          {}seconds
{}            |
{}____________|__________________________________________________________________________________
{}
""".format( WHT_RED, WHT_CYN, CYN_WHT, WHT_BLU, WHT_CYN, CYN_WHT, WHT_BLU, NC_NC, # this is for the headers
            BLU,            # before 50k
            BLU,
            RED, BLU,       # 50,000
            # selection, bubble, merge,  quick,  heap,   radix
            GRN, sel[0],      bub[0], mer[0], qui[0], hea[0], rad[0], YLW,
            BLU,
            BLU,            # after 50k
            BLU,            # before 100k
            BLU,
            RED, BLU,       # 100,000
            # selection, bubble, merge,  quick,  heap,   radix
            GRN, sel[1],      bub[1], mer[1], qui[1], hea[1], rad[1], YLW,
            BLU,
            BLU,            # after 100k
            BLU,            # before 150k
            BLU,
            RED, BLU,       # 150,000
            # selection, bubble, merge,  quick,  heap,   radix
            GRN, sel[2],      bub[2], mer[2], qui[2], hea[2], rad[2], YLW,
            BLU,
            BLU,            # after 150k
            BLU,            # before 200k
            BLU,
            RED, BLU,       # 200,000
            # selection, bubble, merge,  quick,  heap,   radix
            GRN, sel[3],      bub[3], mer[3], qui[3], hea[3], rad[3], YLW,
            BLU,
            BLU,            # after 200k
            BLU,            # before 250k
            BLU,
            RED, BLU,       # 250,000
            # selection, bubble, merge,  quick,  heap,   radix
            GRN, sel[4],      bub[4], mer[4], qui[4], hea[4], rad[4], YLW,
            BLU,
            BLU,            # after 250k
            BLU,            # before 300k
            BLU,
            RED, BLU,       # 300,000
            # selection, bubble, merge,  quick,  heap,   radix
            GRN, sel[5],      bub[5], mer[5], qui[5], hea[5], rad[5], YLW,
            BLU,
            BLU,            # after 300k
            NC              # last one, reset
            )

    

    
    

    
    

    
    
    
    
    
    
    print(grid)




##################
##  Radix sort  ##
##################

def radix(the_list):
    """doc"""
    print("{}Running radix...{}".format(WHT_BLU, NC_NC))

    times = []

    rads = Radix()

    for item in the_list:
        #print("\t...another loop...")
        start = timeit.timeit()
        rads.radixSort(item, 3)     
        end = timeit.timeit()

        times.append(end - start)
        #print("\t...")

    #print(times)


    return times




##################
##  Merge sort  ##
##################

def merges(the_list):
    """doc"""
    print("{}Running merges...{}".format(WHT_BLU, NC_NC))

    times = []

    m = Merge()


    for item in the_list:
        #print("\t...another loop...")
        start = timeit.timeit()
        m.merge_Sort(item)
        end = timeit.timeit()

        times.append(end - start)
        #print("\t...")

    #print(times)


    return times




##################
##  Heap sort   ##
##################

def heaps(the_list):
    """doc"""
    print("{}Running heaps...{}".format(WHT_BLU, NC_NC))

    times = []

    h = Heap()

    for item in the_list:
        #print("\t...another loop...")
        start = timeit.timeit()
        h.sort_The_Heap(item)
        end = timeit.timeit()

        times.append(end - start)
        #print("\t...")

    #print(times)


    return times





###################
##  Bubble sort  ##
###################

def bubbles(the_list):
    """doc"""
    print("{}Running bubbles...{}".format(WHT_BLU, NC_NC))

    times = []

    bubble = Bubble()

    for item in the_list:
        #print("\t...another loop...")
        start = timeit.timeit()
        bubble.bubble_Sort(item)
        end = timeit.timeit()

        times.append(end - start)
        #print("\t...")

    #print(times)


    return times




##################
##  Quick sort  ##
##################

def quicks(the_list):
    """doc"""
    print("{}Running quicks...{}".format(WHT_BLU, NC_NC))

    times = []
   
    q = Quick()

    for item in the_list:
        #print("\t...another loop...")
        start = timeit.timeit()
        q.quick_Sort(item)
        end = timeit.timeit()

        times.append(end - start)
        #print("\t...")


    #print(times)


    return times




######################
##  Selection sort  ##
######################

def selection(the_list):
    """doc"""
    
    print("{}Running selection sort...{}".format(WHT_BLU, NC_NC))

    times = []
    
    s = Selection_Sort()

    for item in the_list:
        #print("\t...another loop...")
        start = timeit.timeit()
        s.selectionSort(item)
        end = timeit.timeit()

        times.append(end - start)
        #print("\t...")

    #print(times)


    return times




def main():
    """This is the main func"""

    sys.setrecursionlimit(400000)

    sizes = [50000, 100000, 150000, 200000, 250000, 300000]
    k50   = [randint(0,10) for x in range(sizes[0])]
    k100  = [randint(0,10) for x in range(sizes[1])]
    k150  = [randint(0,10) for x in range(sizes[2])]
    k200  = [randint(0,10) for x in range(sizes[3])]
    k250  = [randint(0,10) for x in range(sizes[4])]
    k300  = [randint(0,10) for x in range(sizes[5])]
    lsts  = [k50, k100, k150, k200, k250, k300]


    ######################
    ##  Selection sort  ##
    ######################

    select_sort = selection(lsts)


    ###################
    ##  Bubble sort  ##
    ###################
    
    bubble_sort = bubbles(lsts)


    ##################
    ##  Quick sort  ##
    ##################
    
    quick_sort = quicks(lsts)


    ##################
    ##  Merge sort  ##
    ##################
    
    merge_sort = merges(lsts) 


    ##################
    ##  Heap sort   ##
    ##################
    
    heap_sort = heaps(lsts)
  

    ##################
    ##  Radix sort  ##
    ##################
    
    rad_sort = radix(lsts)

    
    
    # Call pretty_Print to show all of the stats
    pretty_Print( select_sort, bubble_sort, merge_sort, quick_sort, heap_sort, rad_sort )



if __name__ == '__main__':
    sys.exit(int(main() or 0))