from random import randint

count = 0
n = randint(0, 9)
exit = ""

while True:
    guess = input("Guess a number: ")
    if (guess == "exit"):
        break

    count += 1
    if (int(guess) == n):
        print("Correct! You took " + str(count) + " guesses.")
        break
