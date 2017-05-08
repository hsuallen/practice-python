name = input("Enter your name: ")
age = int(input("Enter your age: "))
num = int(input("How many times would you like to print? "))

msg = ""
if (age >= 100):
    msg = "You are already 100 years old!\n"
else:
    msg = "You will turn 100 years old in " + str(100 - age)

if (100 - age == 1):
    msg = msg + " year."
else:
    msg = msg + " years."

for x in range(num):
    print(msg)
