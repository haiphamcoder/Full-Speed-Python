def MathOp(a, b):
    classic_division = a/b
    floor_division = a//b
    modulus = a % b
    power = a**b
    return [classic_division, floor_division, modulus, power]


if __name__ == '__main__':
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    [classic_division, floor_division, modulus, power] = MathOp(a, b)
    print(f'{a} divided by {b} is {classic_division}')
    print(f'{a} floor divided by {b} is {floor_division}')
    print(f'{a} modulus {b} is {modulus}')
    print(f'{a} to the power of {b} is {power}')
