#!/usr/bin/env python

# Create a random number array of random size between 2 and 20 integers
# and use mergesort to arrange the elements into order from smallest to
# largest. Print size of the array and the array to terminal.

import numpy as np

# Need a function for mergin
def merge(x1, x2):

    i = 0 # index for x1
    j = 0 # index for x2
    l = 0 # index for y

    n1 = x1.size
    n2 = x2.size
    y = np.zeros(n1+n2, dtype=np.int)
    
    # Go through both subarrays
    while (i<n1) or (j<n2):

        # When both x1 and x2 are in play
        if (i<n1) and (j<n2):
        
            if (x1[i]<x2[j]):
                y[l] = x1[i]
                i += 1
                l += 1
            else:
                y[l] = x2[j]
                j += 1
                l += 1

        # When one of them is already done
        if (i<n1) and (j>=n2):
            y[l:] = x1[i:]
            i = n1
        elif (i>=n1) and (j<n2):
            y[l:] = x2[j:]
            j = n2

    return y    
            
    
# Since mergesort uses recursion, lets define it as a function
def mergesort(x):

    s = x.size

    if s>1: # No sence in sorting an arroy of one element

        # Split the array in half and do mergesort to them
        k = int(s/2)
        x1 = x[:k]
        x2 = x[k:]
        x1 = mergesort(x1)
        x2 = mergesort(x2)

        # Now that x1 and x2 are sorted, lets merge them
        x = merge(x1, x2)

    return x
        
        

# Create the array
n = np.random.random_integers(2,20,1) # Size of array
x = np.random.random_integers(1,20,n) # Actual array

print "\n Number of elements: ", x.size, "\n"
print "Random array: ", x, "\n"

y = mergesort(x)

print "Sorted array is :", y, "\n"



