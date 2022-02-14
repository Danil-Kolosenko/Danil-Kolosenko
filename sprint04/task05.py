class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False


    def play(self, word: str):
        if not self.words:
            self.words.append(word)

        elif word in self.words:
            self.game_over = True
            return "game over"

        elif self.words[-1][-1] != word[0]:
            self.game_over = True
            return "game over"

        else:
            self.words.append(word)

        return self.words

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"
