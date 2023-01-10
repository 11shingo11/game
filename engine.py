import sys
from models2 import MonsterCard, LootCard, Deck, Player
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

hand_rect = pygame.Rect(10, 125, 300, 100)


def hand_field():
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

battle_rect = pygame.Rect(320, 10, 300, 330)


def battle_field():
    pygame.draw.rect(screen, white, battle_rect)
    monster_name_text = pygame.font.Font(None, 30).render(monster_name, True, black)
    monster_level_text = pygame.font.Font(None, 25).render("Level: " + str(monster_level), True, black)
    screen.blit(monster_name_text, (430, 20))
    screen.blit(monster_level_text, (430, 60))



def result():
    battle_rect = pygame.Rect(10, 350, 610, 100)
    pygame.draw.rect(screen, white, battle_rect)
    result_text = pygame.font.Font(None, 30).render(player.text, True, black)
    screen.blit(result_text, (40, 400))


screen = pygame.display.set_mode((800, 640))
while True:
    player_field()
    hand_field()
    using_card()

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hand_rect.collidepoint(event.pos):
                card_rects = []
                card_spacing = 30
                index = 0
                for i, card in enumerate(player.hand):
                    card_rect = pygame.Rect(20, 130 + i * card_spacing, 200, 30)
                    card_rects.append(card_rect)
                    if card_rect.collidepoint(event.pos):
                        selected_card = card
                        player.use_card(index)
                    index += 1
            if battle_rect.collidepoint(event.pos):
                monster_name, monster_level, monster_obj = player.battle()
                battle_field()

            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                monster_name, monster_level, monster_obj = player.battle()
                battle_field()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.fight(monster_obj)
                result()
