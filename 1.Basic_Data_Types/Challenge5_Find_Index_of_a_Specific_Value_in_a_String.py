# Problem Statement
# Given a string, find the first occurences of "b" and "ccc" in the string.

def findOccurences(s):
    return [s.find('b'), s.find('ccc')]


if __name__ == '__main__':
    s = input('Enter a string:')
    print(findOccurences(s))
