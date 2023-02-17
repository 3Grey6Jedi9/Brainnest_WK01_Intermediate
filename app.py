from hangman.game import Game

if __name__ == "__main__":

    game = Game()

    game.create_phrases()

    game.get_random_phrase()

    game.start()

