

class Radix:
    def __init__(self):
        pass


    def radixSort(self, the_list, numberOfDigits):
        ''' Sort the int array list. numberOfDigits is the number of digits in the largest number in the array '''
        buckets = []
        for i in range(10):
            buckets.append([0])

        for position in range(numberOfDigits + 1):
            # Clear buckets
            for i in range(len(buckets)):
                buckets[i] = []    
        
            # Distribute the elements from list to buckets
            for i in range(len(the_list)):
                key = self.getKey(the_list[i], position)
                buckets[key].append(the_list[i])

            # Now move the elements from the buckets back to list
            k = 0 # k is an index for list
            for i in range(len(buckets)):
                for j in range(len(buckets[i])):
                    the_list[k] = buckets[i][j]
                    k += 1

    
    def getKey(self, number, position):
        '''Return the digit at the specified position. The last digit's position is 0. '''

        result = 1
        for _ in range(position):
            result *= 10

        return (number // result) % 10






    '''
    def main():
        the_list = 100 * [0]
        
        for i in range(len(the_list)):
            the_list[i] = random.randint(0, 999)
        
        radixSort(the_list, 3)
        print(the_list)


    main()

    '''