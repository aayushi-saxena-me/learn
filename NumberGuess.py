# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    print(f"Hello, {name}! You are {age} years old.")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

for i in range(5):
    print(i)

def greet(name):
    return f"Hi, {name}!"

friends = ["Alice", "Bob", "Charlie"]
for friend in friends:
    print(greet(friend))

import random

secret = random.randint(1,100)
guess = 0
while guess != secret:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("You got it!")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
