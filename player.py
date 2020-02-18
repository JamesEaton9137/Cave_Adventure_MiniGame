"""This script is used to create the player for the game"""
# Author: James Eaton
# Date: 2/16/20
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
        """Determines if player is alive or not"""
        return self._health_points > 0

    def print_inventory(self):
        """Prints the player's inventory"""
        for item in self._inventory:
            print(item, '\n')

    def get_items(self):
        """Method to see if you have an item in your inventory already"""
        item_list = []
        for item in self._inventory:
            item_list.append(item._name)
        return item_list

    def move(self, dx, dy):
        """Method to move around
        :param dx: Change in X
        :param dy: Change in Y
        """
        self._location_x += dx
        self._location_y += dy
        print(world.tile_exists(self._location_x, self._location_y).intro_text())

    def move_north(self):
        """Method to move north"""
        self.move(dx=0, dy=-1)

    def move_south(self):
        """Method to move south"""
        self.move(dx=0, dy=1)

    def move_east(self):
        """Method to move east"""
        self.move(dx=1, dy=0)

    def move_west(self):
        """Method to move west"""
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        """Method to attack an enemy"""
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

    def flee(self, tile):
        """Method to flee from combat"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def do_action(self, action, **kwargs):
        """Method to perform one of the above actions"""
        print(action)
        action_method = getattr(self, action._method.__name__)
        if action_method:
            action_method(**kwargs)
