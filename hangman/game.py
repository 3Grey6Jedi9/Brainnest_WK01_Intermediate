from hangman import phrase
import random
import string

class Game():

    def __init__(self):

        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = []

    def create_phrases(self):

        a = phrase.Phrase('May the force be with you')
        b = phrase.Phrase('Darth is back')
        c = phrase.Phrase('It is the Matrix')
        d = phrase.Phrase('Hacking Time')
        e = phrase.Phrase('If you read this you are pretty cool')
        self.phrases = [a,b,c,d,e]

    def get_random_phrase(self):

        self.active_phrase = random.choice(self.phrases)

        return self.active_phrase

    def welcome(self):
        print("""   *** ----------------------------------------------- ***
   WELCOME LADIES AND GENTLEMEN TO HANGMAN!!!
   -------------------------------------------------------""")

    def start(self):

        self.welcome()
        while self.missed < 6 and self.active_phrase.check_complete(self.guesses) == False:
            print("\nYou have {} tries left\n".format(6-self.missed))
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            if user_guess not in self.guesses:
                self.guesses.append(user_guess)
            self.active_phrase.check_guess(user_guess)
            if self.active_phrase.check_guess(user_guess):
                print("\nYAY!!!")
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            print('\nUsed letters: {}'.format(self.guesses))
        self.game_over()


    def game_over(self):

        if self.missed >= 6:
            print("\nI'm sorry you've missed too many letters\n")
            self.active_phrase.display(self.guesses)
        else:
            print('\nwell done!!! you got it!!, you guessed the correct phrase: \n')
            self.active_phrase.display(self.guesses)

        while ValueError:
            try:

                play_again = input('would you like to play again[y/n]? ').lower()

                if play_again != 'y' and play_again != 'n':
                    raise ValueError("Please enter 'y' (yes) or 'n' (no)")

            except ValueError as err:
                print ('{}'.format(err))

            else:
                if play_again == 'y':
                    self.restart_game()
                else:
                    print("""Alright as you wish...
                GAME OVER""")
                break



    def get_guess(self):

        while ValueError:

            try:
                answer = input('Guess a letter: ').lower()


                if (set(answer) <= set(string.ascii_lowercase)) == False:
                    raise ValueError('You must enter only a letter, try again please')
                elif len(list(answer)) > 1:
                    raise ValueError('You must enter only a letter, try again please')

            except ValueError as err:

                print('{}'.format(err))

            else:

                return answer


    def restart_game(self):

        game = Game()

        game.create_phrases()

        game.get_random_phrase()

        game.start()