# Problem Statement
# Create a function that cubes the values in a list 1..20 and prints the result.

def getCube():
    return [i**3 for i in range(1, 21)]


if __name__ == "__main__":
    print(f'Cubes: {getCube()}')
