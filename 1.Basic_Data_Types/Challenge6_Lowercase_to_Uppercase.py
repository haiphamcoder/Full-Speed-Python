# Problem Statement
# Given a string, convert it into lowercase and uppercase

def changeCase(s):
    return [s.lower(), s.upper()]


if __name__ == '__main__':
    s = input('Enter a string: ')
    print(changeCase(s))
