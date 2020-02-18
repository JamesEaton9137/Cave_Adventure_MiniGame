"""This script is used to create the player for the game"""
# __author__ = James Eaton
# __date__ = 2/16/20
# pylint: disable=C0301
# pylint: disable=R0903

import random
import items
import world

class Player():
    """Base set of rules for the player"""
    def __init__(self):
        self._inventory = [items.Gold(15), items.Rock()]
        self._health_points = 100
        self._location_x, self._location_y = world.STARTING_POSITION
        self._victory = False

    def is_alive(self):
        return self._health_points > 0

    def print_inventory(self):
        for item in self._inventory:
            print(item, '\n')

    def get_items(self):
        item_list = []
        for item in self._inventory:
            item_list.append(item._name)
        return item_list

    def move(self, dx, dy):
        self._location_x += dx
        self._location_y += dy
        print(world.tile_exists(self._location_x, self._location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_damage = 0
        # Searches your inventory for your highest damaging weapon
        for i in self._inventory:
            if isinstance(i, items.Weapon):
                if i._damage > max_damage:
                    best_weapon = i
                    max_damage = i._damage

        print("You use {} against {}!".format(best_weapon._name, enemy._name))
        enemy._health_points -= best_weapon._damage
        if not enemy.is_alive():
            print("You've killed {}!".format(enemy._name))

        else:
            print("The {} isn't dead yet. It has {} health remaining. Keep fighting!".format(enemy._name, enemy._health_points))

    def do_action(self, action, **kwargs):
        print(action)
        action_method = getattr(self, action._method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
