def LRD_Loop(lst):
    tmp = []
    for x in lst:
        if (x not in tmp):
            tmp.append(x)

    return tmp

def LRD_Sets(lst):
    return sorted(set(lst))

myList = [1, 5, 3, 1, 2, 6, 7, 7, 8, 5]

print(LRD_Loop(myList))
print(LRD_Sets(myList))
