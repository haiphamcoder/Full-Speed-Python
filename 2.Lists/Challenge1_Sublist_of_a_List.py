# Problem Statement
# Given a list, return a sublist of the list

def getSublist(l, pivot):
    return [l[:pivot], l[pivot:]]


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    pivot = int(input('Enter the pivot: '))
    print(getSublist(l, pivot))
