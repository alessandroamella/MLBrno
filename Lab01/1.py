"""
Author: Alessandro Amella
Date: 05/03/2024
"""

# 1.1
n = 5
for i in range(n):
    print("X " * (i+1))
for i in range(n-1):
    print("X " * (n-i-1))

# 1.2
# write a script that will sum all the digits in a string
input_str = "n45as29@#8ss6"
sum = sum(int(i) for i in input_str if i.isdigit())
print(sum)

# 1.3
# write a script that converts a number to binary without using the bin() function
n = 0
binary = ''
while n > 0:
    binary = str(n % 2) + binary # add the remainder to the left of the string
    n = n // 2 # integer division
print(binary or 0)

# 1.4
# Create a function that takes an integer as an input and returns a list that contains all Fibonacci numbers smaller than the input integer
def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2]) # compute fib(n+1) = fib(n) + fib(n-1
    return fib[:-1]
print(fibonacci(100))

# 1.5
"""
Rock, Paper, Scissors is a well-known and simple game. If you do not know the rules, google them. Our task will be to write a code for this game when the user plays against a random computer. The code can be written into one function *rock_paper_scissors*.

Notes:
- This implementation uses the **random** library to enable the computer to make a random choice.
- Keyword **Input** may be useful, check it
- After the function is run, the program will ask you about your movement, which you type in
- The game is case-insensitive for user input (e.g., "rock", "Rock", and "ROCK" are all valid).
- This script plays one round of the game.
- The script prints the result ('You lose', 'You win', 'It is a tie')

"""
import random

def rock_paper_scissors() -> int:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    user = None
    while user not in choices:
        user = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"Computer chose {computer}")
    if user == computer:
        print("It is a tie")
        return 0
    elif user == 'rock' and computer == 'scissors' or user == 'scissors' and computer == 'paper' or user == 'paper' and computer == 'rock':
        print("You win")
        return 1
    else:
        print("You lose")
        return -1

rock_paper_scissors()

# 1.5.1
"""
Extend the Rock, Paper, Scissors game to be able to play *n* rounds.
Use the previous function to play *n* rounds of the game.

Notes: 
- The scrips will contain two counters, one for the current use score and one for the current computer score.
- After each run, the script prints the current scores and current round.
- When the number of rounds is reached, the script prints the result ('You lose', 'You win', 'It is a tie')
"""
def rock_paper_scissors_n_rounds(n: int) -> int:
    user_score = 0
    computer_score = 0
    for i in range(n):
        print(f"Round {i+1}")
        result = rock_paper_scissors()
        if result == 1:
            user_score += 1
        elif result == -1:
            computer_score += 1
        print(f"User score: {user_score}, Computer score: {computer_score}")
    if user_score > computer_score:
        print("You win")
    elif user_score < computer_score:
        print("You lose")
    else:
        print("It is a tie")
        
rock_paper_scissors_n_rounds(2)