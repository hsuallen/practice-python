lst = [1, 4, 65, 123, 99, 2, 7, 99, 8]

n = int(input("Enter a number: "))

print(list(filter(lambda x: x < n, lst)))
