# Problem Statement
# Create a function that removes a sublist from a list

def RemoveSublist(l, l2):
    for i in l2:
        l.remove(i)
    return l


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6]
    l2 = [1, 2, 3]
    RemoveSublist(l, l2)
    print(l)
