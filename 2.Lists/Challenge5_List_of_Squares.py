# Problem Statement
# Create a function that squares the values in a list 1..10 and prints the result.

def getSquare(l):
    return [i*i for i in l]


if __name__ == "__main__":
    l = [i for i in range(1, 11)]
    print(l)
    print(f'Squares: {getSquare(l)}')
