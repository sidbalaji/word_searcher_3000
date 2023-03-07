
class Word:
    def __init__(self, text):
        self.text = text
        self.characters = [_ for _ in text]
        self.word_length = len(self.characters)



