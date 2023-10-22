# Problem Statement
# Write the necessary sequence of operations to transform the string in such a way that every literal is tripled​ respectively.

# Sample Input
# abc

# Sample Output
# aaabbbccc

# Explanation
# The first literal a is tripled, the second literal b is tripled and the third literal c is tripled.

def getStr():
    return input('Enter the string: ')


def triplets():
    s = getStr()
    return ''.join([c*3 for c in s])


if __name__ == '__main__':
    print(triplets())
