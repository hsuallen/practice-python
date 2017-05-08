raw = input("Enter a number: ")
num = int(raw)

if (num % 4 == 0):
    print(raw + " is divisible by 4 and is even.")
elif (num % 2 == 0):
    print(raw + " is even.")
else:
    print(raw + " is odd.")
