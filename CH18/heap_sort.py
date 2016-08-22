

class Heap:
    """doc"""
    def __init__(self):
        """doc"""
        self.__the_list = []
    

    def add_node(self, node):
        """doc"""
        self.__the_list.append(node)
        c_index = len(self.__the_list) - 1

        while c_index > 0:
            p_index = (c_index - 1) // 2

            if self.__the_list[c_index] > self.__the_list[p_index]:
                self.__the_list[c_index], self.__the_list[p_index] = self.__the_list[p_index], self.__the_list[c_index]  
            else:
                break
            
            c_index = p_index
    

    def remove_node(self):
        """doc"""
        if len(self.__the_list) == 0:
            return None
        
        del_node = self.__the_list[0]
        self.__the_list[0] = self.__the_list[len(self.__the_list) - 1]
        self.__the_list.pop(len(self.__the_list) - 1)

        c_index = 0

        while c_index < len(self.__the_list):
            left_node_index  = 2 * c_index + 1
            right_node_index = 2 * c_index + 2

            if left_node_index >= len(self.__the_list):
                break
            
            max_index = left_node_index

            if right_node_index < len(self.__the_list):
                if self.__the_list[max_index] < self.__the_list[right_node_index]:
                    max_index = right_node_index
            
            if self.__the_list[c_index] < self.__the_list[max_index]:
                self.__the_list[max_index], self.__the_list[c_index] = self.__the_list[c_index], self.__the_list[max_index]
                c_index = max_index
            
            else:
                break
            
        return del_node
    

    def get_Size(self):
        """doc"""
        return len(self.__the_list)
    


    def is_Empty(self):
        """doc"""
        return self.get_Size() == 0
    


    def peek(self):
        """doc"""
        return self.__the_list[0]
    


    def get_List(self):
        """doc"""
        return self.__the_list


    def sort_The_Heap(self, the_list):
        """doc"""
        for thingy in the_list:
            self.add_node(thingy)
        
        for i in range(len(the_list)):
            the_list[len(the_list) - 1 - i] = self.remove_node()





    """
    def sort_The_Heap(the_list):
        Creating a Heap object and accessing some of the methods from the class
        heap = Heap()

        for thingy in the_list:
            heap.add_node(thingy)
        
        for i in range(len(the_list)):
            the_list[len(the_list) - 1 - i] = heap.remove_node()


    def main():
        heap_list  = [2,3,2,5,6,1,-2,3,14,12]

        sort_The_Heap(heap_list)

        for thingy in heap_list:
            print("{} ".format(thingy))


    if __name__ == '__main__':
        sys.exit(int(main() or 0))

    """