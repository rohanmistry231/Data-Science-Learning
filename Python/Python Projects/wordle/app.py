from colorama import Fore, Back, Style, init
init()

# object to show current state of the lettes in word
class LetterState:

    def __init__(self, char: str):
        self.char: str = char
        self.is_in_word: bool = False
        self.is_in_position: bool = False 

    def __repr__(self):
        return f"[{self.char}, is_in_word: {Fore.YELLOW}{self.is_in_word}{Fore.RESET}, is_in_position: {Fore.YELLOW}{self.is_in_position}{Fore.RESET}]"
