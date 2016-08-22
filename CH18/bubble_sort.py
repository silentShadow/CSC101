import timeit
import sys




def bubble_Sort(the_list):
    next_pass = True
    z = 1

    while z < len(the_list) and next_pass:
        next_pass = False

        for i in range(len(the_list) - z):
            if the_list[i] > the_list[i + 1]:
                the_list[i], the_list[i + 1] =  the_list[i + 1], the_list[i]
                next_pass = True



def main():
    """the main function here where the list is generated and pass to bubble_Sort"""
    a_list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    
    current_time = timeit.timeit()
    bubble_Sort(a_list)
    finish_time = timeit.timeit()

    for thing in a_list:
        print("{} ".format(thing), end='')
    
    print()
    print("Bubble sort took {:.6f} seconds to run".format(finish_time - current_time))



if __name__ == '__main__':
    sys.exit(int(main() or 0))
