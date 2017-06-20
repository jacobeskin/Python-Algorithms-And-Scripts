# A function that finds the first (or only) duplicate element in an array of
# inetgers. The array has a random size between 1 and 20 integers. Print size,
# array and the result on the terminal. Restriction for the array elements is
# 0<=a[i]<=a.length-1. Print value -1 if no duplicates.

import numpy as np

# Define the method for finding the first duplicate
def firstDuplicate(array):

    # Return value y is -1 by default
    y = -1

    # Start the search only if array.length>1
    z = 0 # For handling zero
    i = 0
    if len(array)>1:

        while (y==-1):
            if i==len(a):
                break
            x = array[abs(array[i])]
            print x
            if x>0:  # Element being pointed to is positive
                array[abs(array[i])] = -1*array[abs(array[i])]
            elif x==0: # Special case of zero
                z = z+1
                if z>1:
                    y = abs(array[i])
                    break
            elif x<0: # We have pointed to this elemet
                y = abs(array[i])
                break
            i = i+1
            
    return(y)

# Create the array
n = np.random.random_integers(1,20,1)  # Size of the array
a = np.random.random_integers(0,n-1,n) # The actual array

# Print the array
print "\n The array: ", a, "\n"

# Call the method firstDuplicate()

y = firstDuplicate(a)

print "\n Result: ", y
