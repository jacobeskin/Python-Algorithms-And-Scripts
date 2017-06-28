#!/usr/bin/env python

# Create a random number vector of random size between 2 and 20 intgers
# and use heapsort to arange the elements into order from largest to
# smallest. Print size of array and the array to terminal. Binary heaps!

import numpy as np

# Function to build the heap, largest value at root
def heapify(x, i, j):

    # The children of node i
    leftchild = i*2+1
    rightchild = i*2+2
    # j is the last node index

    # Letting the smallest element "float" to the bottom of the heap
    smallest = leftchild # Starting guess
    while (smallest<=j):

        k = i
        
        if (x[k]<x[smallest]):
            k = smallest
        
        if (rightchild<j) and (x[k]<x[rightchild]):
            k = rightchild
            
        if (k!=i):
            tmp = x[k]
            x[k] = x[i]
            x[i] = tmp
            smallest = k*2+1
        else:
            return

    return x

# Function to build the heap
def buildheap(x):

    # Size of heap
    heap = x.size-1
    parent = int(heap/2)

    for i in range(parent, -1, -1):
        heapify(x, i, heap)

    return x

#Create the array
n = np.random.random_integers(2,20,1) # Size of array
x = np.random.random_integers(1,20,n) # Actual array

# Print starting position
print "\n Number of elements: ", x.size, "\n"
print "Random array: ", x, "\n"

# Sort the array using heapsort
heap = x.size-1
x = buildheap(x)
for i in range(heap, 0, -1):
    if x[0]<x[i]:
        tmp = x[i]
        x[i] = x[0]
        x[0] = tmp
        x = heapify(x, 0, i-1)
        
# Print sorted array
print "Sorted array is: ", x, "\n"
