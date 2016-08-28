'''
rev: 2
title: binary tree
class: CSC102
author: jonathan reiter
description: used as the constructor for tree objects.  added method of doing a breadth listing of the queue
'''


from queue_class import Queue


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


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    

    def breadth(self):
        """
        1 Add the root node of the tree to a queue
        2 While the queue is not empty Do
        3 ...Remove the first node E from the queue
        4 ...Print the element field of E
        5 ...Add to the queue the children nodes of E
        """

        q = Queue()
        the_root = self.root
        #print("the_root:", the_root.element)

        #1
        q.enqueue(the_root)

        #2
        while not q.isEmpty():
            #3
            deld = q.dequeue()

            #4
            print("{}Removed {}{}{} from the queue{}".format(BLU, GRN, deld.element, BLU, NC))

            if deld.left:
                print("Left:",deld.left.element, end='')
            else:
                print("Left: None\t", end='')

            #5
            if deld.right:
                print("Right:",deld.right.element, end='\n\n')
                q.enqueue(deld.right)
            else:
                print("Right: None\t", end='')

        print()
        print("\n{}Queue is empty{}".format(WHT_RED, NC_NC))

 
    def search(self, e):
        """Return True if the element is in the tree"""
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False

 
    def insert(self, e):
        """Insert element e into the binary search tree. Return True if the element is inserted successfully"""
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        list = []
        current = self.root # Start from the root

        while current != None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element: 
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left     

        self.size -= 1
        return True # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None
