import random


class Player:
    def __init__(self, name, loot_deck, health=1, level=1):
        self.name = name
        self.health = health
        self.strength = level
        self.loot_deck = loot_deck
        self.hand = []

    def start(self):
        self.hand = self.loot_deck.draw(2)

    def get_level(self):
        level = 1
        for card in self.hand:
            level += card.level
        return level


class LootCard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name}\nLVL = {self.level}"


class MonsterCard:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.strength = self.health

    def __str__(self):
        return f"{self.name}\nhp = {self.health} / str = {self.strength}"


class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, count=1):
        if count > len(self.cards):
            count = len(self.cards)
        draw_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return draw_cards

    def remove(self, card):
        pass


class LootDeck(Deck):
    def __init__(self, name):
        super().__init__(name)

    def add_loot(self, loot_card):
        self.cards.append(loot_card)

    def remove_loot(self, loot_card):
        self.cards.remove(loot_card)

    def __str__(self):
        return f"{self.name} deck with {len(self.cards)} cards"


class MonstersDeck(Deck):
    def __init__(self, name):
        super().__init__(name)

    def add_monster(self, monster_card):
        self.cards.append(monster_card)

    def remove_monster(self, monster_card):
        self.cards.remove(monster_card)

    def __str__(self):
        return f"{self.name} deck with {len(self.cards)} cards"

