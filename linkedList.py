# Linked list module. It has two classes, the Node-class, which is what it
# sounds like, and the linkedList-class.
#
# Linked list object has the following attributes and methods:
# self.size                      length of the list
# addNode(data, n)               add data to postion n
# delNode(n)                     delete node n
# isPalindrome()                 checks if the current list is palindrome
# printList()                    prints the list to terminal


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


    # Method for checking if list is palindrome. 
    def isPalindrome(self):

        # Need to variables, fast goes throug the list twice as fast as slow
        fast, slow = self.head, self.head
        rev = Node(None, None) # This will house the revesed porition

        # Run to the middle of the list
        while fast and fast.next_n:
            fast = fast.next_n.next_n
            # Always add the new node to the front of rev. Also advane slow
            rev, rev.next_n, slow = slow, rev, slow.next_n

        # If the list is odd
        if fast:
            slow = slow.next_n

        # Compare values from rev and the latter half of the list
        while slow:
            if slow.data!=rev.data:
                return False
            else:
                slow, rev = slow.next_n, rev.next_n

        # If no exeptions are raised, return True
        return True
        
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

# Testing adding and deleting nodes
#list = linkedList()
#print "\n Adding nodes 0 1 2 3 4 to four nodes and printing the list. \n" 
#list.addNode(0,0)
#list.addNode(1,0)
#list.addNode(2,2)
#list.addNode(3,0)
#list.addNode(4,list.size)
#print "\n List size:", list.size, "\n"
#print "Printing list:\n"
#list.printList()
#print "\n Deleting some nodes. \n"
#list.delNode(0)
#list.delNode(1)
#list.delNode(3)
#list.delNode(list.size)
#list.printList()
#print "\n List size now:", list.size, "\n"

# Testing palindrome method

#print "\n Is list palindrome?\n"
#if list.isPalindrome():
#    print "Yes it is!\n"
#else:
#    print "No it's not!\n"

#print "Make new list:\n"
#list2 = linkedList()
#list2.addNode(0,0)
#list2.addNode(1,1)
#list2.addNode(2,2)
#list2.addNode(1,3)
#list2.addNode(0,4)
#list2.printList()
#print "\n Is this list palindrome?\n"
#if list2.isPalindrome():
#    print "Yes it is!\n"
#else:
#    print "No it's not!\n"





