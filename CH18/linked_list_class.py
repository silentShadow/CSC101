class LinkedList:
    """doc"""

    def __init__(self):
        """doc"""
        self.__head = None                                  # Basically the root Node
        self.__tail = None                                  # The last Node
        self.__size = 0




    def __iter__(self):
        """Return an iterator for a linked list"""
        return LinkedListIterator(self.__head)




    def getFirst(self):
        """Return the head element in the list"""
        if self.__size == 0:
            return None
        else:
            return self.__head.element




    def getLast(self):
        """Return the last element in the list"""
        if self.__size == 0:
            return None
        else:
            return self.__tail.element




    def addFirst(self, e):
        """Add an element to the beginning of the list"""
        newNode = Node(e)                                   # Create a new node
        newNode.next = self.__head                          # link the new node with the head
        self.__head = newNode                               # head points to the new node
        self.__size += 1                                    # Increase list size

        if self.__tail == None:                             # the new node is the only node in list
            self.__tail = self.__head



 
    def addLast(self, e):
        """Add an element to the end of the list"""
        newNode = Node(e)                                   # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode             # The only node in list
        else:
            self.__tail.next = newNode                      # Link the new with the last node
            self.__tail = self.__tail.next                  # tail now points to the last node
    
        self.__size += 1                                    # Increase size




    def add(self, e):
        """Same as addLast"""
        self.addLast(e)




    def insert(self, index, e):
        """Insert a new element at the specified index in this list The index of the head element is 0""" 
        if index == 0:
            self.addFirst(e)                                # Insert first
        elif index >= self.__size:
            self.addLast(e)                                 # Insert last
        else:                                               # Insert in the middle
            current = self.__head
            for _ in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1



 
    def removeFirst(self):
        """Remove the head node and return the object that is contained in the removed node."""
        if self.__size == 0:
            return None                                     # Nothing to delete
        else:
            temp = self.__head                              # Keep the first node temporarily
            self.__head = self.__head.next                  # Move head to point the next node
            self.__size -= 1                                # Reduce size by 1
            if self.__head == None: 
                self.__tail = None                          # List becomes empty 
            return temp.element                             # Return the deleted element




    def removeLast(self):
        """Remove the last node and return the object that is contained in the removed node"""
        if self.__size == 0:
            return None                                     # Nothing to remove
        elif self.__size == 1:                              # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None                # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for _ in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element



 
    def removeAt(self, index):
        """Remove the element at the specified position in this list. Return the element that was removed from the list."""
        if index < 0 or index >= self.__size:
            return None                                     # Out of range
        elif index == 0:
            return self.removeFirst()                       # Remove first 
        elif index == self.__size - 1:
            return self.removeLast()                        # Remove last
        else:
            previous = self.__head
    
            for _ in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element




    def isEmpty(self):
        """Return true if the list is empty"""
        return self.__size == 0
    



    def getSize(self):
        """Return the size of the list"""
        return self.__size



    def __str__(self):
        """doc"""
        result = "["

        current = self.__head
        for _ in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", "                              # Separate two elements with a comma
            else:
                result += "]"                               # Insert the closing ] in the string

        return result



    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None



    # Return true if this list contains the element o 
    def contains(self, e):
        print("Implementation left as an exercise")
        return True




    def remove(self, e):
        """Remove the element and return true if the element is in the list"""
        
        print("Removing {}...".format(e))

        if self.__size == 0:
            return False                                                                    # Nothing to remove
        
        elif self.__size == 1:                                                              # Only one element in the list
            self.__head = self.__tail = None                                                # list becomes empty
            self.__size = 0
            return False
        
        else:
            curr_node = self.__head
            prev_node = None

            while curr_node:                                                                # Loop over the nodes
                if curr_node.element == e:                                                  # If there is a match then remove that node
                    print("match! {}".format(curr_node.element))
                    if prev_node:
                        print("prev node {}".format(prev_node.element))
                        prev_node.next = curr_node.next
                        print("updated.. {}".format(prev_node.next.element))

                    else:
                        self.__head = curr_node.next
                    
                    self.__size -= 1
                    return True
                
                
                else:
                    print("curr_node is... {}".format(curr_node.element))
                    prev_node = curr_node
                    curr_node = curr_node.next
                    print("next is... {}".format(curr_node.element))
            return False
    










    def get(self, index):
        """Return the element from this list at the specified index """
        print("Implementation left as an exercise")
        return None




    def indexOf(self, e):
        """Return the index of the head matching element in this list. Return -1 if no match."""
        print("Implementation left as an exercise")
        return 0



 
    def lastIndexOf(self, e):
        """Return the index of the last matching element in this list. Return -1 if no match."""
        print("Getting index of {}".format(e))

        curr_node  = self.__head

        while curr_node:
            if curr_node.element == e:
                return curr_node.element
            else:
                curr_node = curr_node.next

        return -1




    def set(self, index, e):
        """Replace the element at the specified position in this list with the specified element. */"""
        print("Replacing {} at index {}...".format(e, index))

        new_node = Node(e)                          # set a new node object
        #new_node.next(self.__head)                  # point the new node at the current head thus making this at the head of the list


        if index < 0 or index >= self.__size:
            print("You are out of the list range 0-{}".format(self.__size))
            return None                                     # Out of range

        elif index == 0:
            self.addFirst(e)
            self.removeFirst()                              # Remove first

        elif index == self.__size - 1:
            self.addLast(e)
            self.removeLast()                               # Remove last

        else:
            current = self.__head
            print("current {}".format(current.element))
            for _ in range(1, index):                                   # Loop till the index value is found
                current = current.next
                print("looping... {}".format(current.element))
            temp = current.next                                         # Hold the current node temporarily
            print("temp var is {}".format(temp.element))
            current.next = new_node                                     # Set the next node of the current one to the new_node being created
            print("new next {}".format(current.next.element))
            (current.next).next = temp.next                             # Skip a node so that the specified index is gone thus pointing its next node

        return None



    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)







# The Node class
class Node:
    """doc"""

    def __init__(self, element):
        """doc"""

        self.element = element
        self.next = None



class LinkedListIterator:
    """doc"""

    def __init__(self, head):
        """doc"""

        self.current = head


    def __next__(self):
        """doc"""

        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    
        


