import random
from typing import List


class Card:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def __str__(self):
        return f"{self.name}\nLevel: {self.level}"


class Deck:
    def __init__(self, name: str, cards: List[Card]):
        self.name = name
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, count: int = 1) -> Card | list[Card]:
        if count == 1:
            return self.cards.pop()
        else:
            return [self.cards.pop() for _ in range(count)]

    def add(self, card: Card):
        self.cards.append(card)

    def remove(self, card: Card):
        self.cards.remove(card)


class LootCard(Card):
    def __init__(self, name, level):
        super().__init__(name, level)

    def use(self, player):
        player.level += self.level


class MonsterCard(Card):
    def __init__(self, name, level):
        super().__init__(name, level)

    def use(self, player):
        player.level += self.level

    def draw(self):
        return self


class Player:
    def __init__(self, name, monster_deck, loot_deck):
        self.loot_deck = loot_deck
        self.monster_deck = monster_deck
        self.hand = []
        self.level = 1
        self.name = name

    def start(self):
        self.hand = self.loot_deck.draw(2)

    def fight(self, monster):
        if self.level >= monster.level:
            print(f"{self.name} has won the fight against {monster.name}!")
            self.hand.append(self.loot_deck.draw())
        else:
            print(f"{self.name} has lost the fight against {monster.name}.")

    def battle(self):
        monster = self.monster_deck.draw()
        self.fight(monster)

    def use_card(self, index):
        card = self.hand[index]
        card.use(self)
