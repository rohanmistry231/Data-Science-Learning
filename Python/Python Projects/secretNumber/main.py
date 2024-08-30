import random 

num_digits = 3
max_guess = 10

def main():
    print("Begals, Fermi, Pico Math Game with Python")
    print(f"""
    I am thinking of a {num_digits} digit number with no repeated digits. Try to guess
    what it is. Here are few clues:\n
    if messages is 'Pico', Your one digit is correct but on the wrong place.
    if message is 'Fermi', One digit is correct, and on the right place.
    And if message is, 'Bagels', No digit is correct.\n

    So, if the secret number is 456 and your guess is 651, message would be, "Fermi Pico ..
    """)

    while True:
        secretNum = getSecretNum()
        print("I have a scret nuber for you to guess.")
        print(f"You have {max_guess} to guess it!")

        numGusses = 1
        while numGusses <= max_guess:
            guess = ""
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess {numGusses}')
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGusses += 1

            if guess == secretNum:
                break 
            if numGusses > max_guess:
                print("No more guesses allowed! Try Again...")
                print(f"\nThe Answer was {secretNum}")

        print("\nDo you want to play again? [yes or no]")
        if not input("> ").lower().startswith('y'):
            break
    print("Thanks for playing!")


def getSecretNum():
    numbers = list('012345789')
    random.shuffle(numbers)
    secretNum= ""
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "You Got It!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == "__main__":
    main()
















