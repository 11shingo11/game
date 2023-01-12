import pygame
from models2 import MonsterCard, LootCard, Deck, Player
import sys


pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
monster_cards = [MonsterCard("Goblin", 1), MonsterCard("Troll", 3),
                 MonsterCard("Dragon", 5), MonsterCard("Orc", 2),
                 MonsterCard("Undead", 1)]
loot_cards = [LootCard("Helm", 2), LootCard("Potion", 1),
              LootCard("Shield", 3), LootCard("Sword", 2),
              LootCard("Boots", 1)]
loot_deck = Deck("Loot", loot_cards)
monster_deck = Deck("Monsters", monster_cards)
monster_deck.shuffle()
loot_deck.shuffle()
hand_rect = pygame.Rect(10, 125, 300, 100)
player_rect = pygame.Rect(10, 10, 300, 100)
used_cards_rect = pygame.Rect(10, 240, 300, 100)
battle_rect = pygame.Rect(320, 10, 300, 330)
result_rect = pygame.Rect(10, 350, 610, 100)
player = Player("Bob", monster_deck, loot_deck)
player.start()
screen = pygame.display.set_mode((800, 640))


def create_mdeck():
    monster_cards = [MonsterCard("Goblin", 1), MonsterCard("Troll", 3),
                     MonsterCard("Dragon", 5), MonsterCard("Orc", 2),
                     MonsterCard("Undead", 1)]
    monster_deck = Deck("Monsters", monster_cards)
    monster_deck.shuffle()
    player.monster_deck = monster_deck



def render_text(text, x, y, font_size):
    font = pygame.font.Font(None, font_size)
    text = font.render(text, True, BLACK)
    screen.blit(text, (x, y))


def player_field():
    pygame.draw.rect(screen, WHITE, player_rect)
    render_text("Игрок:", 20, 20, 30)
    render_text(player.name, 20, 40, 30)
    render_text("Level: " + str(player.level), 20, 60, 25)


def hand_field():
    pygame.draw.rect(screen, WHITE, hand_rect)
    render_text("Карты в руке:", 20, 125, 30)
    card_spacing = 20
    for i, card in enumerate(player.hand):
        card_text = str(card)
        render_text(card_text, 20, 145 + i * card_spacing, 25)


def using_card():
    pygame.draw.rect(screen, WHITE, used_cards_rect)
    render_text("Инвентарь:", 20, 240, 25)
    if player.use_card:
        card_spacing = 20
        for i, card in enumerate(player.inv):
            render_text(str(card), 20, 260 + i * card_spacing, 25)


def battle_field():
    pygame.draw.rect(screen, WHITE, battle_rect)
    render_text("Поле активного монстра:", 320, 20, 30)


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
                if len(player.hand) != 0:
                    for i, card in enumerate(player.hand):
                        card_rect = pygame.Rect(20, 130 + i * card_spacing, 200, 30)
                        card_rects.append(card_rect)
                        if card_rect.collidepoint(event.pos):
                            player.use_card(index)
                        index += 1
                else:
                    pygame.draw.rect(screen, WHITE, result_rect)
                    render_text('Сообщение:', 20, 360, 25)
                    render_text("Нет карт в руке", 20, 390, 25)

            if battle_rect.collidepoint(event.pos):
                if len(player.monster_deck.cards) != 0:
                    monster_name, monster_level, monster_obj = player.battle()
                    battle_field()
                    render_text("Имя монстра: " + monster_name, 320, 40, 25)
                    render_text("Уровень монстра: " + str(monster_level), 320, 60, 25)
                    pass
                else:
                    create_mdeck()
                    battle_field()
                    pygame.draw.rect(screen, WHITE, result_rect)
                    render_text('Упс!', 20, 360, 25)
                    render_text('Больше нет монстров.Замешаем новую колоду!', 20, 390, 25)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pygame.draw.rect(screen, WHITE, result_rect)
                player.fight(monster_obj)
                render_text('Результат:', 20, 360, 25)
                render_text(player.text, 20, 390, 25)
