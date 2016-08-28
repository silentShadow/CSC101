class Stack:
    def __init__(self):
        """Initializer"""
        self.__elements = []


    def isEmpty(self):
        """Return true if the tack is empty"""
        return len(self.__elements) == 0
    

    def peek(self):
        """Returns the element at the top of the stack without removing it from the stack."""
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]


    def push(self, value):
        """Stores an element into the top of the stack"""
        self.__elements.append(value)


    def pop(self):
        """Removes the element at the top of the stack and returns it"""
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop() 
    

    def getSize(self):
        """Return the size of the stack"""
        return len(self.__elements)
