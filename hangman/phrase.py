class Phrase():

    def __init__(self, phrase):

        self.phrase = phrase.lower()

    def display(self, guesses):

        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end="")
            elif letter == ' ':
                print(" ", end="")
            else:
                print("_", end=" ")

        print('\n')

    def check_guess(self, guess):

        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):

        for letter in self.phrase:
            if letter not in guesses:
                return False
            else:
                guesses.append(' ')
                if set(guesses) >= set(self.phrase):
                    return True
                else:
                    return False
