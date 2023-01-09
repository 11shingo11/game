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

    def shuffle(self):
        pass

    def draw(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass


class Player:
    def __init__(self,name, level, hand):
        self.hand = hand
        self.level = level
        self.name = name

    def start(self):
        pass