"""This script is used to create the enemies in the game"""
# __author__ = James Eaton
# __date__ = 2/16/20
# pylint: disable=C0301
# pylint: disable=R0903


class Enemies():
    """Initalize the enemies
    :param name: Name of the enemy
    :param health_points: The enemy's health
    :param damage: The damage of the enemy
    """
    def __init__(self, name, health_points, damage):
        self._name = name
        self._health_points = health_points
        self._damage = damage

    def is_alive(self):
        """Determines if the enemy is alive or not"""
        return self._health_points > 0


class GiantSpider(Enemies):
    """Initalizes the giant spider"""
    def __init__(self):
        super().__init__(name="Giant Spider",
                         health_points=10,
                         damage=2)


class CaveBat(Enemies):
    """Initalizes the cave bat"""
    def __init__(self):
        super().__init__(name="Cave Bat",
                         health_points=10,
                         damage=3)


class Bandit(Enemies):
    """Initalizes the bandit"""
    def __init__(self):
        super().__init__(name="Bandit",
                         health_points=15,
                         damage=7)


class Ogre(Enemies):
    """Initalizes the ogre"""
    def __init__(self):
        super().__init__(name="Ogre",
                         health_points=30,
                         damage=15)


# Dungeon Boss
class CaveDragon(Enemies):
    """Initalizes the cave dragon"""
    def __init__(self):
        super().__init__(name="Cave Dragon",
                         health_points=100,
                         damage=40)
