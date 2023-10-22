# Problem Statement
# Create a function that averages the values in a list. The original list should not be altered in any way.
# The output should be a float.

def getAverage(l):
    return sum(l)/len(l)


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    print(l)
    print(f'Average: {getAverage(l)}')
