#!/usr/bin/env python

# Create a random number array of random size between 2 and 20 integers
# and use insertion sort to arrange the elements into order from smallest
# to largest. Print size of the array and the array to terminal.

import numpy as np

# Create the array
n = np.random.random_integers(2,20,1) # Size of array
x = np.random.random_integers(1,20,n) # Actual array

# Print starting position
print "\n Number of elements: ", x.size, "\n"
print "Random array: ", x, "\n"

# Sort the array using insertion sort
for i in range(1,n):
    j = i-1
    y = x[i]                    # Element to be re-assigned
    
    # Go through all preivous elements behind y that are larger than or
    # equal to y, and move them up by one spot.
    while (j>=0) and (x[j]>=y): 
        x[j+1] = x[j]
        j = j-1
    x[j+1] = y                  # Relocate y to its proper place

# Print sorted array
print "sorted array is: ", x, "\n"
    
    
    

    
    
