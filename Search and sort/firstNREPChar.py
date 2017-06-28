# Find the first character in a string that is not repeated. Input from the
# command line is any string, print the string and result on screen. If no
# such character exists, print "-".

import string

# Define the method that finds the character
def fstNonRepChar(string):

    # Default return value is "-"
    y = "-"

    # Define two character lists, one that has the non-repeated characters and
    # one that has repeated characters
    norep = []
    rep = []

    # Loop through the string
    for c in string:

        # If c has not been encountered before
        if (c not in rep) and (c not in norep):
            norep.append(c)

        # If c has been encouneterd before
        elif c in norep:
            norep.remove(c)
            if c not in rep:
                rep.append(c)

    # If norep has characters, then there is non-repeating characters and
    # the first one is the first non-repeating
    if len(norep)!=0:
        y = norep[0]

    return(y)

# Main body of the code. Read string from comamnd line
s = raw_input("\n Give a string please: ")

# Call the method
y = fstNonRepChar(s)

# Print the result

print "\n The result is: \n"
print(y)
            
