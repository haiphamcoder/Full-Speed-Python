# Problem Statement
# Create a function that squares the even numbers in a list 0..20 and not divisible by 3 and prints the result.

def getSquares():
    return [i ** 2 for i in range(21) if i % 2 == 0 and i % 3 != 0]


if __name__ == "__main__":
    print(f'Squares of Even Numbers not divisible by 3: {getSquares()}')
