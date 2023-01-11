import sys
import pygame
from models2 import MonsterCard, LootCard, Deck, Player

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
monster_cards = [MonsterCard("Goblin", 1), MonsterCard("Troll", 3), MonsterCard("Dragon", 5), MonsterCard("Orc", 2), MonsterCard("Undead", 1)]
monster_deck = Deck("Monsters", monster_cards)
loot_cards = [LootCard("Helm", 2), LootCard("Potion", 1), LootCard("Shield", 3), LootCard("Sword", 2),LootCard("Boots", 1)]
loot_deck = Deck("Loot", loot_cards)
monster_deck.shuffle()
loot_deck.shuffle()
player = Player("Shingo", monster_deck, loot_deck)
player.start()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create some monster and loot cards and decks
monster_cards = [MonsterCard("Goblin", 1), MonsterCard("Troll", 3),
                 MonsterCard("Dragon", 5), MonsterCard("Orc", 2),
                 MonsterCard("Undead", 1)]
monster_deck = Deck("Monsters", monster_cards)

loot_cards = [LootCard("Helm", 2), LootCard("Potion", 1),
              LootCard("Shield", 3), LootCard("Sword", 2),
              LootCard("Boots", 1)]
loot_deck = Deck("Loot", loot_cards)

# Shuffle the decks
monster_deck.shuffle()
loot_deck.shuffle()

# Create a player
player = Player("Shingo", monster_deck, loot_deck)
player.start()

# Create a screen
screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption("Monster Battle")

# Rectangle for the player field
player_rect = pygame.Rect(10, 10, 300, 100)

# Rectangle for the hand field
hand_rect = pygame.Rect(10, 125, 300, 100)

# Rectangle for the used cards field
used_cards_rect = pygame.Rect(10, 240, 300, 100)

# Rectangle for the battle field
battle_rect = pygame.Rect(320, 10, 300, 330)

def render_text(text, x, y, font_size):
    """ Helper function to render text on the screen"""
    font = pygame.font.Font(None, font_size)
    text = font.render(text, True, BLACK)
    screen.blit(text, (x, y))

def player_field():
    """ Function for rendering the player field"""
    pygame.draw.rect(screen, WHITE, player_rect)
    render_text("Игрок:", 20, 20, 30)
    render_text(player.name, 20, 40, 30)
    render_text("Level: " + str(player.level), 20, 60, 25)

def hand_field():
    """ Function for rendering the hand field"""
    pygame.draw.rect(screen, WHITE, hand_rect)
    render_text("Карты в руке:", 20, 125, 30)
    card_spacing = 20
    for i, card in enumerate(player.hand):
        card_text = str(card)
        render_text(card_text, 20, 145 + i * card_spacing, 25)

def using_card():
    """ Function for using cards"""
    pygame.draw.rect(screen, WHITE, used_cards_rect)
    render_text("Инвентарь:", 20, 240, 25)
    if player.use_card:
        card_spacing = 20
        for i, card in enumerate(player.inv):
            render_text(str(card), 20, 260 + i * card_spacing, 25)
    for event in pygame.event.get():
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


def battle_field():
    monster_name, monster_level, monster_obj = player.battle()
    pygame.draw.rect(screen, WHITE, battle_rect)
    render_text("Поле активного монстра:", 320, 20, 30)
    render_text("Имя монстра: " + monster_name, 320, 40, 25)
    render_text("Уровень монстра: " + str(monster_level), 320, 60, 25)

def draw_main_menu():
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw title
    title_text = "My Game"
    title_font = pygame.font.Font(None, 60)
    title_surface = title_font.render(title_text, True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(400, 100))
    screen.blit(title_surface, title_rect)

    # Draw play button
    global play_button
    play_button = pygame.Rect(300, 200, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), play_button)
    play_text = "Play"
    play_font = pygame.font.Font(None, 30)
    play_text_surface = play_font.render(play_text, True, (0, 0, 0))
    play_text_rect = play_text_surface.get_rect(center=play_button.center)
    screen.blit(play_text_surface, play_text_rect)

def game_loop():
    """ Main game loop"""
    running = True
    while running:
        # Draw main menu here
        player_field()
        hand_field()
        using_card()
        battle_field()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                    pass
                elif battle_rect.collidepoint(event.pos):
                    monster_name, monster_level, monster_obj = player.battle()
                    battle_field()


game_loop()



