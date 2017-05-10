# this solution only works for positive integers

def isPrime():
    n = getInt()

    lst = []

    lst.append(1)
    if (n == 1):
        pass
    else:
        for x in range(2, n+1):
            if (n % x == 0):
                lst.append(x)

    if (len(lst) == 1 or len(lst) >= 3 or n == 0):
        print(str(n) + " is not a prime.")
    else:
        print(str(n) + " is a prime.")

def getInt():
    return int(input("Enter a number: "))

isPrime()
