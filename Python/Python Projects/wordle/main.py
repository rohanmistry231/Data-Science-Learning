from app import LetterState
from wordle import Wordle
from colorama import Fore, Back, Style, init
import random

# initializing colorama
init()

# main function
def main():
    print(Fore.GREEN + "... HELLO WORDLE ..." +Fore.RESET)
    # reading the words from a text file
    wordle_words = load_word_set("data\wordle_words.txt")
    secret = random.choice(list(wordle_words))

    wordle = Wordle(secret)

    # checking the correct input
    while wordle.can_attempt:
        w = input("\nEnter your word:  ").upper()
        if len(w) != wordle.word_length:
            print(Fore.RED + f"\nWord length must be {wordle.word_length} charcters long!" + 
            Fore.RESET)
            continue
        if w.isdigit():
            print(Fore.RED + f"\nNot a word. Enter a string!" + 
            Fore.RESET)
            continue
        if not w in wordle_words:
            print(Fore.RED + f"\nNot a correct word in the list!" + 
            Fore.RESET)
            continue
        
 
        wordle.attempt(w)
        # result= wordle.guess(w)
        # print(*result, sep='\n')
        display_result(wordle)

    if wordle.is_solved:
        print(Fore.LIGHTBLUE_EX + f"\nYou solved the puzzle.. in {len(wordle.attempts)} attempts! "+Fore.RESET)
    else:
        print(Fore.RED + "\nYou failed to solved the puzzle!"+Fore.RESET)
        print(f"\nThe Secret word was {Fore.LIGHTMAGENTA_EX}{wordle.secret}{Fore.RESET}")


# loading the words list 
def load_word_set(path: str):
    words_set = set()
    with open(path,'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            words_set.add(word)
    return words_set

# displaying results after each attempt
def display_result(wordle: Wordle):
    print(f"\n {Fore.LIGHTBLUE_EX} Your result so far.. .{Fore.RESET}\n")
    
    for word in wordle.attempts:
        result = wordle.guess(word)
        converted_result = convert_result_to_color(result)
        print(converted_result)
    for _ in range(wordle.remaining_attempts):
        print("_ " * wordle.word_length) 

# useing colors in command line
def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.char+ Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)



if __name__=="__main__":
    main()