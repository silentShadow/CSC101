# The function for sorting elements in ascending order

class Selection_Sort:
    def __init__(self):
        pass

    def selectionSort(self, the_list):
        for i in range(len(the_list) - 1):
            # Find the minimum in the lst[i : len(lst)]
            currentMin, currentMinIndex = the_list[i], i
    
            for j in range(i + 1, len(the_list)):
                if currentMin > the_list[j]:
                    currentMin, currentMinIndex = the_list[j], j

            # Swap lst[i] with lst[currentMinIndex] if necessary
            if currentMinIndex != i:
                the_list[currentMinIndex], the_list[i] = the_list[i], currentMin

