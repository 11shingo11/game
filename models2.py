class Card:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def use(self):
        pass

class Deck:
    def __init__(self, name):
        self.name = name
        self.card = []
