# Problem Statement
# Create a function that squares the even numbers in a list 0..20 and prints the result.

def evenSquareSum():
    return sum([i ** 2 for i in range(21) if i % 2 == 0])


if __name__ == "__main__":
    print(f'Sum of Squares of Even Numbers: {evenSquareSum()}')
    