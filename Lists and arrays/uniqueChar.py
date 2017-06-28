# Determine if a given string has all unique characters. User input string,
# cannot be bothered to set limits. Return True or False.

# Method for this checking
def unique(s):

    chars = []
    for i in range(len(s)):
        if s[i] not in chars: chars.append(s[i])
        elif s[i] in chars: return False

    return True

# User input
s = raw_input('\n Give a string:')

# Check
if unique(s): print '\n String has all unique characters! \n'
else: print '\n String has duplicates and whatnot... \n'
