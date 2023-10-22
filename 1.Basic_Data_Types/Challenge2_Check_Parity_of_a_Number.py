def checkParity(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == '__main__':
    num = int(input('Enter the number: '))
    print(f'{num} is {checkParity(num)}')
