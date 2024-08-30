from app import LetterState

# main class wordle
class Wordle:

    max_attempts = 6
    word_length = 5


    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    # counting attempts
    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    # guessing the word
    def guess(self, word:str):
        word = word.upper()
        result = []

        for i in range(self.word_length):
            k = word[i]
            letter = LetterState(k)
            letter.is_in_word = k in self.secret
            letter.is_in_position = k == self.secret[i]
            result.append(letter)

        return result


    @property  
    # checking the attempts
    def is_solved(self):
        return len(self.attempts) > 0 and  self.attempts[-1] == self.secret

    
    @property
    # remaing attempts to guess the word
    def remaining_attempts(self) -> int:
        return self.max_attempts - len(self.attempts)

    @property
    # allowing to attempt
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
        
