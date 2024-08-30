# Number Guessing App with upper and lower bound and error handling 

import random
from datetime import datetime 

"""
RoadMap

Ask for user input - Name
User input for lower and upper range
Get a random number

Main function
    - input guess
    - checking guess
        - if correct, return something
        - if incorrect, prompt again
Function for file handling.
Function to write a text string 
"""

def create_text_string(name, gueses, lowest, highest):
    now = datetime.now()
    now = datetime.strftime(now, format="%H:%M:%S %d-%B-%Y")
    score_string = f"\nPlayer: {name}. Guess: {gueses}. Given {highest-lowest} number choices. At {now}\n"
    return score_string

def write_score_file(filename, text, mode='a'):
    with open(filename, mode=mode) as file:
        file.write(text)


def get_user_input_range():
    current_attempts = 0
    attempts_to_valid_guess = 3

    while current_attempts < attempts_to_valid_guess:
        current_attempts += 1
        try:
            low_number = int(input("Enter a lower bound: "))
            upper_number = int(input("Enter the upper bound: "))
        except ValueError:
            print("Invalid Format!")
            continue
        else:
            if low_number < upper_number:
                return low_number, upper_number
            else:
                print("Low bound must be less than upper bound.")
                continue
    else:
        print("Attempts exceeded. Range set to 1 to 10")

        return (1,10)


def get_a_random_number(lower, upper):
    return random.randint(lower, upper)


def main_game(random_number, low, high):
    attempts = 1
    guess_lst = []
    guess = int(input("Enter your guess: "))

    while guess != random_number:
        attempts += 1
        # check in number is within range
        if guess <= high and guess >= low:
            # check for duplicate entry
            if guess not in guess_lst:
                guess_lst.append(guess)
            else:
                print(f"You have already tried number: {guess}")
        else:
            print(f"Your guess must be within defined range of [{low, high}]")


        if guess > random_number:
            try:
                guess = int(input("Lower: "))
            except ValueError:
                print("Invalid entry!")
                continue
        elif guess < random_number:
            try:
                guess = int(input("Upper: "))
            except ValueError:
                print("Invalid entry!")
                continue
    
    else:
        print("\nCorrect Guess! Good Job.")
        return attempts





def main(filename):
    name = input("Enter your name: ").title()
    if not name:
        print("No name entered. try again.. ")
    

    low_number, upper_number = get_user_input_range()
    print(f"\nRange: Low: {low_number} | Upper: {upper_number}")

    random_number = get_a_random_number(low_number, upper_number)
    # print(f"Random Number: {random_number}")


    user_score = main_game(random_number, low_number, upper_number)
    print(f"You took {user_score} attempts to get the correct number {random_number}")

    score_string = create_text_string(name, user_score, low_number, upper_number)
    print(score_string)

    write_score_file(filename, score_string)


if __name__=='__main__':
    filename='scores.txt'
    main(filename)