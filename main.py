from models import *
#карты лута
l1 = LootCard('Щит', 1)
l2 = LootCard('Меч', 2)
l3 = LootCard('Наручи', 1)
l4 = LootCard('Шлем', 2)
l5 = LootCard('Броня', 3)
#карты монстров
m1 = MonsterCard('Дракон', 4)
m2 = MonsterCard('Орк', 2)
m3 = MonsterCard('Гоблин', 1)
m4 = MonsterCard('Скелет', 1)
m5 = MonsterCard('Некромант', 3)
#создание колоды лута
loot_deck = LootDeck("Treasure")
loot_deck.add_loot(l1)
loot_deck.add_loot(l2)
loot_deck.add_loot(l3)
loot_deck.add_loot(l4)
loot_deck.add_loot(l5)
#создание колоды монстров
monster_deck = MonstersDeck("Monsters")
monster_deck.add_monster(m1)
monster_deck.add_monster(m2)
monster_deck.add_monster(m3)
monster_deck.add_monster(m4)
monster_deck.add_monster(m5)
#перемешивание карт колод лута и монстров
loot_deck.shuffle()
monster_deck.shuffle()

##игрок берет две карты
##hand = loot_deck.draw(2)
'''
print(hand[0])
print(hand[1])
print(len(loot_deck.cards))
'''


player = Player("Alice", 10, loot_deck)
player.start()
print(player.hand[0])