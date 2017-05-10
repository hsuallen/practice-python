string = input("Enter a string: ")
lower = string.lower()
palindrome = lower[::-1]

if (lower == palindrome):
    print(string + " is a palindrome.")
else:
    print(string + " is not a palindrome.")
