class Hangman:
    def __init__(self, word: str, chances=6):
        self.word = word
        self.guessed = ['.'] * len(word)
        self.chances = chances
        self.gameover = False
        self.won = False

    def __repr__(self):
        if self.won:
            return f"Congratulations! You have guessed the word!\n{self.word}"
        if self.gameover:
            return f"Oops, you have been hung.\n{self.word}"
        return f"You have {self.chances} more chance{'' if self.chances == 1 else 's'}.\n{''.join(self.guessed)}"

    def guessLetter(self, guess: str):
        if self.gameover:
            print("Sorry, the game is over.")
        else:
            assert isinstance(guess, str) and guess.isalpha() and len(guess) == 1, "argument is not a letter"
            guess, word = guess.lower(), self.word.lower()
            assert guess not in "".join(self.guessed).lower(), "letter has already been guessed"
            if guess in word:
                self.guessed = [self.word[i] if guess == letter else self.guessed[i] for i, letter in enumerate(word)]
                self.won = self.gameover = '.' not in self.guessed
                print(f"Correct: letter {guess} occurs {word.count(guess)} times in the word.\n{self!r}")
            else:
                self.chances -= 1
                self.gameover = self.chances == 0
                print(f"Wrong: letter {guess} does not occur in the word.\n{self!r}")


h = Hangman('strawberry', chances=3)
print(h)
h.guessLetter('a')
h.guessLetter('b')
h.guessLetter('c')
h.guessLetter('y')
h.guessLetter('e')
h.guessLetter('f')
h.guessLetter('h')
