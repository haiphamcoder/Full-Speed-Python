# Problem Statement
# Create a function that takes a list of numbers as input and returns a list of even and odd numbers.

def ListOfEvenOdds(l):
    return [i for i in l if i % 2 == 0], [i for i in l if i % 2 != 0]


if __name__ == "__main__":
    l = [i for i in range(21)]
    print(l)
    even, odd = ListOfEvenOdds(l)
    print(f'Even: {even}')
    print(f'Odd: {odd}')
