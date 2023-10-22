# Problem Statement
# Create a function that appends a value to the end of a list. The original list should be altered and returned, not a copy.
# The output should be the same list object, not a new list object.
# The function should accept any data type of value to be appended.

def AppendToList(l, value):
    l.append(value)
    return l


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    AppendToList(l, 6)
    print(l)