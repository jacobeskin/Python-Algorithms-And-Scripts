# Linked list module. It has two classes, the Node-class, which is what it
# sounds like, and the linkedList-class. Rest will be explained in the comments.

import sys

#-------------------------------------------------------------------------------
# First, the class Node()
class Node(object):

    # Constructor
    def __init__(self, data, next_n):
        self.data = data
        self.next_n = next_n

#-------------------------------------------------------------------------------
# Next, the actual linked list class
class linkedList(object):

    # Constructor
    def __init__(self):
        self.head = None
        self.size = 0

    # Method for retrieveing the size of the list
    def size(self):
        return self.size

    # Method for adding a node at point n
    def addNode(self,data, n):
        
        new_node = Node(data, self.head) # New node

        # Check if list bounds are being respected
        if n>self.size:
            sys.exit("Error! List index exeeded for linkedList.addNode().")
            return 

        # Case of empty list and n==0
        if n==0:
            self.head = new_node
            self.size += 1
            return

        # Get the (n-1)th node 
        prev_node = Node(data, self.head) 
        for i in range(n):                  
            prev_node = prev_node.next_n

        # Set new node pointing in the right direction and the previous
        # node pointing at the new node
        new_node.next_n = prev_node.next_n
        prev_node.next_n = new_node    
        self.size += 1
        return

    # Method for deleting a node at place n
    def delNode(self, n):

        # Check if list is already empty or that list bounds are respected
        if self.size==0:
            print "List is already empty."
            return
        if n>self.size or n<0:
            sys.exit("Error! Element to be deleted out of bounds.")
            

        # If only one node in list
        if self.size==1:
            self.head = None
            self.size -= 1
            return

        # If deleted node is the first node
        if n==0:
            temp_node = self.head
            self.head = temp_node.next_n
            self.size -= 1
            return

        # If deleted node is between 0 and n, go to the (n)th node
        if 0<n<list.size:
            temp_node1 = self.head # Will be the deleted node
            temp_node2 = self.head # Node before the deleted node
            for i in range(n):
                temp_node2 = temp_node1
                temp_node1 = temp_node1.next_n

                # Set (n-1)th node to point in the .next_n of (n)th node
                temp_node2.next_n = temp_node1.next_n
                
                self.size -= 1 # The list shrinks
                return
                
        # If the last node is to be deleted
        if n==list.size:
            temp_node = self.head
            for i in range(n-2): # Go to the second to last node
                temp_node = temp_node.next_n

            temp_node.next_n = None # Set the second to last node pointer
            self.size -= 1
            return


    # Method for printing out the list
    def printList(self):

        # If list is empty
        if list.size==0:
            print "List is empty"
            return

        temp_node = self.head
        while temp_node!=None:
            print(temp_node.data)
            temp_node = temp_node.next_n

        return


#------------- For testing purposes--------
#list = linkedList()
#print "\n Adding nodes 0 1 2 3 4 to four nodes and printing the list. \n" 
#list.addNode(0,0)
#list.addNode(1,0)
#list.addNode(2,2)
#list.addNode(3,0)
#list.addNode(4,list.size)
#print "\n List size:", list.size, "\n"
#list.printList()
#print "\n Deleting some nodes. \n"
#list.delNode(0)
#list.delNode(1)
#list.delNode(3)
#list.delNode(list.size)
#list.printList()
#print "\n List size now:", list.size, "\n"




