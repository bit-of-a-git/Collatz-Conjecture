import time

integer = input("I will attempt the Collatz Conjecture using any number you give me. Please enter an integer.\n")
while not integer.isdigit():
    integer = input("Please enter an integer.\n")
# Turns the string input into an integer.
integer = int(integer)


def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)
        # Puts a half second pause between numbers
        time.sleep(.5)


collatz(integer)
