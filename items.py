"""This script is used to create the items for the game"""
# Author: James Eaton
# Date: 2/16/20
# pylint: disable=C0301
# pylint: disable=R0903


class Item():
    """The base class for items"""
    def __init__(self, name, description, value):
        self._name = name
        self._description = description
        self._value = value
        self._looted = False

    def __str__(self):
        return "{}\n======\n{}\nValue: {}\n".format(self._name, self._description, self._value)

    def is_looted(self, looted):
        """Determines if an item has been looted from a tile or not"""
        self._looted = looted
        return self._looted


class Gold(Item):
    """Creates a golden coin item"""
    def __init__(self, amount):
        self._amount = amount
        super().__init__(name="Gold",
                         description="A round, shiny coin that may be worth something in town.\nThere is a {} print on its face.".format(self._amount),
                         value=self._amount)


class Health_Potion(Item):
    """Creates the health potion item"""
    def __init__(self, heal_amount):
        self._heal_amount = heal_amount
        super().__init__(name="Health Potion",
                         description="A curious looking vile. Try it, it may help!",
                         value=10)


class Weapon(Item):
    """Base class for all weapons in the game"""
    def __init__(self, name, description, value, damage):
        self._damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n======\n{}\nValue: {}\nDamage: {}\n".format(self._name, self._description, self._value, self._damage)


class Rock(Weapon):
    """Creates a rock weapon"""
    def __init__(self):
        super().__init__(name="Rock",
                         description="An average sized rock, able to be used to crush some skulls.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    """Creates the dagger weapon"""
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger, probably left behind by another adventurer.",
                         value=10,
                         damage=10)


class ShortSword(Weapon):
    """Creates the short sword weapon"""
    def __init__(self):
        super().__init__(name="Shortsword",
                         description="A rusted longsword. Looks like it's been here for some time, though it looks like it can cut a limb off still.",
                         value=20,
                         damage=15)


class BroadSword(Weapon):
    """Creates the broadsword weapon"""
    def __init__(self):
        super().__init__(name="Broadsword",
                         description="A polished looking broadsword. Its owner must've been here recently...",
                         value=50,
                         damage=25)


# Dungeon Boss killer
class DiamondSword(Weapon):
    """Creates the diamond sword weapon"""
    def __init__(self):
        super().__init__(name="Diamond sword",
                         description="A gleaming sword that looks deadly. This weapon looks like it can cut rocks in half.",
                         value=300,
                         damage=100)
