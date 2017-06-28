# Rotate a nxn matrix clocwise. In place rotation, meaning no matrix
# multiplication. Random integer matrix is generated, and before and after
# states are printed out.
#
# The idea is that four elements switch place at a time (i=row, j=column):
# a[i][j] --> a[j][n-1-i]
# a[j][n-1-i] --> a[n-1-i][n-1-j]
# a[n-1-i] --> a[n-1-j][i]
# a[n-1-j] --> a[i][j]
#
# where i goes from 0 to n/2 and j from i to n-1-i.

import numpy as np

# Define the method that does the rotation
def rotation(a):

    n = len(a)
    for i in range(n/2):
        for j in range(i,n-1-i):

            # Need 3 placeholders
            place1 = a[j][n-1-i]
            place2 = a[n-1-i][n-1-j]
            place3 = a[n-1-j][i]

            # Do the switch
            a[j][n-1-i] = a[i][j]
            a[n-1-i][n-1-j] = place1
            a[n-1-j][i] = place2
            a[i][j] = place3

    return(a)

# Create a random integer matrix
n = np.random.random_integers(1,7,1)
n = int(n)
a = np.random.randint(10, size=(n,n))

# Print the array before rotation
print "\n Array before rotation: \n"
print(a)

# Rotate array
a = rotation(a)

# Print array after rotation
print "\n Array after rotation: \n"
print(a)
