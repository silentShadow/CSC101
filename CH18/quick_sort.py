
class Quick:
    """This is the Quick class sort"""
    def __init__(self):
        pass


    def quick_Sort(self, the_list):
        """quick_Sort kicks things off by specifying the first and last items from the_list"""
        self.sort_Helper(the_list, 0, len(the_list) - 1)


    def sort_Helper(self, the_list, first, last):
        """sort_Helper sets up the pivot and start sorting"""
        if last > first:
            pivot = self.sort_Partition(the_list, first, last)
            self.sort_Helper(the_list, first, pivot - 1)
            self.sort_Helper(the_list, pivot + 1, last)


    def sort_Partition(self, the_list, first, last):
        """sort_Partition does the grunt work by checking to see if idexes are higher or lower than the pivot and moving them accordingly"""
        pivot = the_list[first]
        low   = first + 1
        high  = last

        while high > low:
            while low <= high and the_list[low] <= pivot:       # From the left
                low += 1
            
            while low <= high and the_list[high] > pivot:       # From the right
                high -= 1
            
            if high > low:                                      # Do a swap
                the_list[high], the_list[low] = the_list[low] , the_list[high]

        while high > first and the_list[high] >= pivot:
            high -= 1
        
        if pivot > the_list[high]:
            the_list[first] = the_list[high]
            the_list[high] = pivot
            return high
        else:
            return first




    




