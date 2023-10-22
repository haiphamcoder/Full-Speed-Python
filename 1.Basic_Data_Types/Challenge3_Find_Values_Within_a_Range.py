# Problem Statement
# Write a function that takes two numbers and returns a boolean value based on whether the first number is less than 1/3 and the second number is greater than 1/3.

def inRange(x, y):
    return x < 1/3 < y


if __name__ == '__main__':
    x = float(input('Enter the first number: '))
    y = float(input('Enter the second number: '))
    print(f'{x} < 1/3 < {y} is {inRange(x, y)}')
