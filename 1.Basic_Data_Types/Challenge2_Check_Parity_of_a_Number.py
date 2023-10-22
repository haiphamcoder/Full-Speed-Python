# Problem Statement
# Write a function that takes a number and returns a string that states whether the number is even or odd.

def checkParity(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == '__main__':
    num = int(input('Enter the number: '))
    print(f'{num} is {checkParity(num)}')
