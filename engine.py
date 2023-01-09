import sys
from models2 import *
import random
from testmodels import *
import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
monster_cards = [MonsterCard("Goblin", 1), MonsterCard("Troll", 3), MonsterCard("Dragon", 5), MonsterCard("Orc", 2), MonsterCard("Undead", 1)]
monster_deck = Deck("Monsters", monster_cards)
loot_cards = [LootCard("Helm", 2), LootCard("Potion", 1), LootCard("Shield", 3), LootCard("Sword", 2),LootCard("Boots", 1)]
loot_deck = Deck("Loot", loot_cards)
monster_deck.shuffle()
loot_deck.shuffle()
player = Player("Bob", monster_deck, loot_deck)
player.start()


def player_field():
    player_rect = pygame.Rect(10, 10, 300, 100)
    pygame.draw.rect(screen, white, player_rect)

    player_name = pygame.font.Font(None, 30).render(player.name, True, black)
    player_level = pygame.font.Font(None, 25).render("Level: " + str(player.level), True, black)

    screen.blit(player_name, (20, 20))
    screen.blit(player_level, (20, 50))

def hand_field():
    hand_rect = pygame.Rect(10, 120, 300, 100)
    pygame.draw.rect(screen, white, hand_rect)

    card_spacing = 30
    for i, card in enumerate(player.hand):
        card_text = pygame.font.Font(None, 25).render(str(card), True, black)
        screen.blit(card_text, (20, 130 + i * card_spacing))

def using_card():
    used_cards_rect = pygame.Rect(10, 240, 300, 100)
    pygame.draw.rect(screen, white, used_cards_rect)
    if player.use_card:
        card_spacing = 30
        for i, card in enumerate(player.inv):
            card_text = pygame.font.Font(None, 25).render(str(card), True, black)
            screen.blit(card_text, (20, 260 + i * card_spacing))
def battle_field():
    battle_rect = pygame.Rect(320, 10, 300, 300)
    pygame.draw.rect(screen, white, battle_rect)




screen = pygame.display.set_mode((800, 640))
while True:

    player_field()
    hand_field()
    using_card()
    battle_field()



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.use_card(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.battle()

