import sys

# not the best solution but

n = int(input("Enter a number: "))

lst = []
if (n == 0):
    print("0 is a horrible choice.")
    sys.exit()

lst.append(1)
if (n == 1):
    pass
else:
    for x in range(2, n+1):
        if (n % x == 0):
            lst.append(x)

print(lst)
